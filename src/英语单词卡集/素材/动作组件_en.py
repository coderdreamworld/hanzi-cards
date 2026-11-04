#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语动作卡本地助手：基于kid原生人体，替换指定手臂/五官而不叠出额外肢体。"""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from 识字卡片_素材库 import *


def person(x=380, y=430, s=1, pose="stand", shirt=BLUE, face="smile", arms="down", hands=None, eyes=None, brows=None, mouth=None, **kwargs):
    """hands为左右手端点，支持起点-肘-手三点。先移除原臂再装新臂，保持两条。"""
    root = ET.fromstring('<g>' + kid(x=x,y=y,s=s,pose=pose,shirt=shirt,face=face,arms=arms,**kwargs) + '</g>')
    children = list(root)
    shoulder = y-(152 if pose=="sit" else 168)*s
    hcy = shoulder-70*s
    if hands is not None:
        # kid躯干之后到耳朵之前是原臂组（line+手圆或point变换组）。
        body = next(i for i,e in enumerate(children) if e.tag=='path' and e.get('fill')==shirt)
        head = next(i for i,e in enumerate(children) if e.tag=='circle' and abs(float(e.get('r',0))-62*s)<.01)
        firstear = head-2
        for e in children[body+1:firstear]:
            root.remove(e)
        parts = ''
        for sign,points in zip((-1,1),hands):
            start=(x+sign*44*s,shoulder+6*s)
            pts=[start]+list(points)
            d='M '+' L '.join(f'{a} {b}' for a,b in pts)
            parts += P(d,stroke=SKIN,w=30*s)+C(*pts[-1],13*s,SKIN)
        insert = list(root).index(children[firstear])
        for e in ET.fromstring('<g>'+parts+'</g>'):
            root.insert(insert,e);insert+=1
    if eyes is not None or brows is not None or mouth is not None:
        # 原五官按几何坐标识别；眉毛和嘴都是小型path，位于脸部对应区。
        for e in list(root):
            tag=e.tag
            cx,cy=float(e.get('cx',0)),float(e.get('cy',0))
            if eyes is not None and tag in {'ellipse','circle'} and (abs(cx-(x-22*s))<.1 or abs(cx-(x+22*s))<.1) and hcy-20*s<cy<hcy:
                root.remove(e)
            if tag=='path' and e.get('fill')=='none' and e.get('stroke') in {HAIR,INK}:
                d=e.get('d','')
                import re
                ns=[float(v) for v in re.findall(r'-?\d+(?:\.\d+)?',d)]
                if len(ns)>=2:
                    py=ns[1]
                    if brows is not None and hcy-50*s<py<hcy-20*s:root.remove(e)
                    elif mouth is not None and hcy+15*s<py<hcy+50*s:root.remove(e)
            elif mouth is not None and tag in {'ellipse','path'} and e.get('fill') in {'#6b3325','#f0876f'}:
                root.remove(e)
        for drawing in (eyes,brows,mouth):
            if drawing:
                for e in ET.fromstring('<g>'+drawing+'</g>'):root.append(e)
    return ''.join(ET.tostring(e,encoding='unicode') for e in root)


def spot(x,y):
    return E(x,y,42,14,GROUND)


def motion(x,y,flip=1,color=TEAL):
    return ''.join(L(x+flip*12*i,y+22*i,x+flip*(66+12*i),y+22*i,color,6) for i in range(3))


def apple(x,y,s=1):
    g=P('M 0 -34 C -60 -75 -86 -16 -62 28 Q -30 80 0 60 Q 30 80 62 28 C 86 -16 60 -75 0 -34 Z',RED)
    g+=P('M 0 -35 Q -4 -64 10 -76',stroke=WOOD_D,w=10)+E(28,-68,24,12,GREEN)+E(-34,-12,11,20,PINK,.7)
    return f'<g transform="translate({x} {y}) scale({s})">{g}</g>'


def book(x,y,s=1,color=TEAL):
    g=P('M 0 -40 Q -60 -70 -114 -40 L -114 46 Q -60 15 0 48 Q 60 15 114 46 L 114 -40 Q 60 -70 0 -40 Z',color)
    g+=P('M 0 -34 Q -50 -58 -104 -35 L -104 35 Q -50 10 0 40 Q 50 10 104 35 L 104 -35 Q 50 -58 0 -34 Z',WHITE)+L(0,-32,0,40,WOOD_L,3)
    for dx in (-88,18):
        for yy in (-20,-4,12):g+=L(dx,yy,dx+66,yy,GROUND,4)
    return f'<g transform="translate({x} {y}) scale({s})">{g}</g>'


def bubble(x,y,content):
    return C(x,y,68,'#ffffff')+C(x-42,y+72,12,'#ffffff')+C(x-58,y+98,7,'#ffffff')+content
