import AVFoundation
import Foundation

struct Segment: Decodable {
    let text: String
    let ipa: String?
}

struct AudioItem: Decodable {
    let name: String
    let segments: [Segment]
}

guard CommandLine.arguments.count == 3 else {
    fputs("用法：swift 生成标准呼读音.swift <manifest.json> <输出目录>\n", stderr)
    exit(2)
}

let manifestURL = URL(fileURLWithPath: CommandLine.arguments[1])
let outputURL = URL(fileURLWithPath: CommandLine.arguments[2], isDirectory: true)
let items = try JSONDecoder().decode([AudioItem].self, from: Data(contentsOf: manifestURL))
try FileManager.default.createDirectory(at: outputURL, withIntermediateDirectories: true)

guard let voice = AVSpeechSynthesisVoice(identifier: "com.apple.voice.compact.zh-CN.Tingting") else {
    fputs("未找到 macOS 普通话语音 Tingting\n", stderr)
    exit(3)
}

for item in items {
    let text = item.segments.map(\.text).joined()
    let attributed = NSMutableAttributedString(string: text)
    var location = 0
    for segment in item.segments {
        let length = (segment.text as NSString).length
        if let ipa = segment.ipa {
            attributed.addAttribute(
                NSAttributedString.Key(rawValue: AVSpeechSynthesisIPANotationAttribute),
                value: ipa,
                range: NSRange(location: location, length: length)
            )
        }
        location += length
    }

    let destination = outputURL.appendingPathComponent("\(item.name).caf")
    try? FileManager.default.removeItem(at: destination)
    let hasIPA = item.segments.contains { $0.ipa != nil }
    let utterance = hasIPA
        ? AVSpeechUtterance(attributedString: attributed)
        : AVSpeechUtterance(string: text)
    utterance.voice = voice
    utterance.rate = 0.43
    utterance.volume = 1

    let synthesizer = AVSpeechSynthesizer()
    var complete = false
    var outputFile: AVAudioFile?
    var writeError: Error?
    synthesizer.write(utterance) { buffer in
        guard let pcm = buffer as? AVAudioPCMBuffer else { return }
        if pcm.frameLength == 0 {
            complete = true
            return
        }
        do {
            if outputFile == nil {
                outputFile = try AVAudioFile(forWriting: destination, settings: pcm.format.settings)
            }
            try outputFile?.write(from: pcm)
        } catch {
            writeError = error
            complete = true
        }
    }

    let deadline = Date().addingTimeInterval(20)
    while !complete && Date() < deadline {
        RunLoop.current.run(mode: .default, before: Date().addingTimeInterval(0.05))
    }
    if let error = writeError {
        fputs("写入失败 \(item.name)：\(error)\n", stderr)
        exit(4)
    }
    if !complete || !FileManager.default.fileExists(atPath: destination.path) {
        fputs("系统语音生成超时或无输出：\(item.name)\n", stderr)
        exit(5)
    }
    print("✓ \(item.name).caf")
    fflush(stdout)
}
