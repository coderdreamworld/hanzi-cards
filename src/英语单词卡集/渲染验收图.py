#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""使用系统SVG渲染，分组每页9张生成可辨认的插画验收图与逐页词图清单。"""
import argparse
import html
import importlib.util
import json
import subprocess
import time
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('en_build',HERE/'构建.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--groups',nargs='*')
    args=parser.parse_args()
    groups,art,_,_=mod.resolve_deck(partial=True)
    dest=HERE/'验收'
    dest.mkdir(exist_ok=True)
    records=[]
    for group in groups:
        if args.groups and group['id'] not in args.groups:continue
        for start in range(0,len(group['cards']),9):
            cards=group['cards'][start:start+9]; rows=(len(cards)+2)//3
            width,height=1200,1200
            parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',f'<rect width="1200" height="{height}" fill="#fdf8ec"/>',f'<text x="18" y="35" font-size="22" fill="#4a3226" font-family="Arial">{html.escape(group["id"])} / {start+1}–{start+len(cards)}</text>']
            for i,c in enumerate(cards):
                x,y=18+(i%3)*394,58+(i//3)*292
                parts.append(f'<rect x="{x}" y="{y}" width="380" height="278" rx="16" fill="#fffaf0" stroke="#ead9ac"/>')
                parts.append(f'<g transform="translate({x+8} {y+8}) scale(.478)">{art[c["w"]]}</g>')
                parts.append(f'<text x="{x+190}" y="{y+260}" text-anchor="middle" font-size="19" font-weight="bold" fill="#4a3226" font-family="Arial">{html.escape(c["w"])}</text>')
            parts.append('</svg>')
            name=f'{group["id"]}_{start//9+1:02d}.svg'
            svg=dest/name; content=''.join(parts)
            if not svg.exists() or svg.read_text()!=content:
                svg.write_text(content,encoding='utf-8')
            png=dest/(name+'.png')
            if not png.exists() or png.stat().st_mtime<svg.stat().st_mtime:
                subprocess.run(['qlmanage','-t','-s','1600','-o',str(dest),str(svg)],capture_output=True,check=True)
            assert png.exists(), str(png)
            records.append({'group':group['id'],'page':start//9+1,'png':str(png),'words':cards})
    if not args.groups:
        (dest/'清单.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'pages':len(records),'cards':sum(len(r['words']) for r in records),'files':[r['png'] for r in records]},ensure_ascii=False))


if __name__=='__main__':main()
