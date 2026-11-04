#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将验收通过的英语卡与音频复制到现有Pages仓库，保留其他卡组文件。"""
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

HERE=Path(__file__).resolve().parent
REPO=HERE.parent/'微信传播方案'/'发布'/'github-pages'

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    for name in ('物品场景视觉问题.json','新卡视觉问题.json'):
        review=json.loads((HERE/'验收'/name).read_text())
        assert not review.get('fails'),f'{name}仍有未修复fail'
    subprocess.run(['python3',str(HERE/'构建.py')],cwd=HERE,check=True)
    subprocess.run(['python3',str(HERE/'检查英语卡.py')],cwd=HERE,check=True)
    page=HERE/'english-words.html'
    shutil.copy2(page,REPO/page.name)
    audio_files=list((HERE/'audio').glob('en_*.m4a'))
    assert len(audio_files)==1026,len(audio_files)
    for src in audio_files:
        dest=REPO/'audio'/src.name
        shutil.copy2(src,dest)
        assert digest(src)==digest(dest),src.name
    backup=REPO/'src'/'英语单词卡集'
    backup.mkdir(exist_ok=True)
    excluded={'页面语法检查.js','预览_en.html','预览验收页.html','英语单词卡_试点20词.html'}
    count=0
    for src in HERE.iterdir():
        if src.is_file() and src.suffix in {'.py','.md','.html'} and src.name not in excluded:
            shutil.copy2(src,backup/src.name);count+=1
    (backup/'素材').mkdir(exist_ok=True)
    for src in (HERE/'素材').glob('*.py'):
        shutil.copy2(src,backup/'素材'/src.name);count+=1
    (backup/'验收').mkdir(exist_ok=True)
    for src in (HERE/'验收').glob('*.json'):
        if src.name in {'清单.json','渲染日志.json','身体修复渲染.json'}:continue
        shutil.copy2(src,backup/'验收'/src.name);count+=1
    manifest={'html_sha256':digest(page),'audio_count':len(audio_files),'source_files':count,'audio_sha256':{p.name:digest(p) for p in audio_files}}
    (HERE/'验收'/'发布对账.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    print(f'OK 发布副本1页 + {len(audio_files)}音频，源码文档{count}份；HTML sha256={manifest["html_sha256"]}')

if __name__=='__main__':main()
