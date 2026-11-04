#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""交付门：500词条/顺序/音频/字母/逐图XML/唯一图稿/产物JS语法。"""
import collections
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('en_build',HERE/'构建.py');build=importlib.util.module_from_spec(spec);spec.loader.exec_module(build)
groups,art,aud,problems=build.resolve_deck(False)
assert not problems,problems
ciku=build.load_ciku().GROUPS
wanted=[w['w'] for g in ciku for w in g['words']]
assert len(wanted)==500 and len(set(w.casefold() for w in wanted))==500
html=(HERE/'english-words.html').read_text(encoding='utf-8')

def read_const(name):
    offset=html.index('const '+name+' = ')+len('const '+name+' = ')
    return json.JSONDecoder().raw_decode(html[offset:])[0]

cards,product_art,product_audio=map(read_const,['CARDS','ART','AUD'])
assert [c['w'] for c in cards]==wanted,'成品卡序偏离锁版词表'
assert len(read_const('GROUPS'))==25
assert set(product_art)==set(wanted)
for card in cards:
    assert product_art[card['key']]==art[card['key']]
    assert product_audio[card['key']]==aud[card['key']]
    for kind in ('w','s'):
        meta=aud[card['key']][kind]
        assert meta['dur']>0 and meta.get('mean_db',-99)>-45,(card['key'],kind,meta)
for letter in 'abcdefghijklmnopqrstuvwxyz':
    f=HERE/'audio'/f'en_letter_{letter}.m4a'
    assert f.is_file() and f.stat().st_size>512,letter
hashes=collections.defaultdict(list)
for w,svg in art.items():hashes[hashlib.sha256(svg.encode()).hexdigest()].append(w)
duplicates=[ws for ws in hashes.values() if len(ws)>1]
assert not duplicates,('不同词条不能共用完全相同图稿',duplicates)
# 数字系列实际红色主苹果圆与数字一一对应。
import xml.etree.ElementTree as ET
for n,w in enumerate(['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']):
    root=ET.fromstring('<svg>'+art[w]+'</svg>')
    actual=sum(1 for e in root.iter() if e.tag.rsplit('}',1)[-1]=='circle' and e.get('fill')=='#e8663c')
    assert actual==n,(w,actual,n)
js=html.split('<script>',1)[1].split('</script>',1)[0]
script=HERE/'页面语法检查.js';script.write_text(js,encoding='utf-8')
subprocess.run(['node','--check',str(script)],check=True)
report={'words':500,'groups':25,'artworks':500,'word_audio':1000,'letter_audio':26,'duplicate_artworks':duplicates,'numbers':'0-12 all exact','js_syntax':'pass','html_sha256':hashlib.sha256(html.encode()).hexdigest()}
(HERE/'验收'/'结构验收.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
