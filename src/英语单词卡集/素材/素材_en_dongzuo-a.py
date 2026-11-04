#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""身体动作22卡：动作本身、接触点和方向是主视觉。"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from 动作组件_en import *

GROUP_CARDS=[{'w':w,'cn':cn} for w,cn in [('run','跑'),('walk','走'),('jump','跳'),('climb','爬'),('swim','游泳'),('fly','飞'),('fall','摔/落'),('sit','坐'),('stand','站'),('look','看'),('listen','听'),('dance','跳舞'),('sing','唱歌'),('clap','拍手'),('wave','挥手'),('point','指'),('kick','踢'),('push','推'),('pull','拉'),('throw','扔/投'),('catch','接住'),('hug','拥抱')]]


def bird(x,y,s=1):
    g=E(0,0,70,42,BLUE)+C(-62,-12,32,BLUE)+PG([(-91,-10),(-121,1),(-91,13)],YEL)
    g+=P('M -12 -7 Q 10 -112 87 -88 Q 40 -25 14 1 Z',BLUE_D)+PG([(62,0),(116,-40),(107,12)],BLUE)+C(-68,-17,5,INK)
    return f'<g transform="translate({x} {y}) scale({s})">{g}</g>'


def drawing(w):
    g=ground()
    if w=='run':return g+motion(145,270)+person(pose='sprint',arms='pump',shirt=RED)+L(310,455,425,455,TEAL,5)
    if w=='walk':return g+person(pose='stride',arms='swing',shirt=TEAL)+E(300,446,26,9,WOOD_L)+E(470,446,26,9,WOOD_L)
    if w=='jump':return g+E(380,444,70,14,TEAL_L,.6)+person(y=360,shirt=YEL,arms='up',face='open')+L(270,380,257,419,TEAL,6)+L(490,380,503,419,TEAL,6)
    if w=='climb':
        g+=L(430,115,430,450,WOOD,20)+L(560,115,560,450,WOOD,20)
        for yy in (150,215,280,345,410):g+=L(430,yy,560,yy,WOOD_L,13)
        g+=person(x=387,y=420,s=.85,pose='stride',shirt=BLUE,hands=([ (431,288) ],[(478,217)]))+C(473,218,11,SKIN)
        return g
    if w=='swim':
        g+=R(80,295,600,145,42,'#bce3ec')
        swimmer=person(x=340,y=420,s=.9,pose='sprint',shirt=RED,hands=([(245,272)],[(488,270)]))
        g+=f'<g transform="rotate(-72 340 300)">{swimmer}</g>'
        g+=P('M 80 333 Q 160 306 230 335 T 380 335 T 530 335 T 680 335 L 680 445 L 80 445 Z',WBLUE)
        for xx in (130,280,460,585):g+=P(f'M {xx} 382 Q {xx+24} 365 {xx+48} 382',stroke=WHITE,w=6)
        return g
    if w=='fly':return g+cloud_p(180,220,.9,'#e4eff2')+cloud_p(600,135,.8,'#e4eff2')+bird(385,250,1.6)+P('M 520 355 Q 590 340 620 275',stroke=TEAL_L,w=6)
    if w=='fall':return g+f'<g transform="rotate(-57 370 319)">{person(x=370,y=409,pose="sit",face="o",shirt=TEAL,arms="up")}</g>'+star5(515,366,28,YEL)+star5(244,392,21,YEL)+P('M 242 155 Q 194 260 257 313',stroke=TEAL,w=7)
    if w=='sit':return g+R(320,358,150,24,9,WOOD)+R(335,380,21,58,7,WOOD_D)+R(440,380,21,58,7,WOOD_D)+person(y=438,pose='sit',shirt=BLUE)
    if w=='stand':return g+person(shirt=YEL,hands=([(305,288),(333,321)],[(455,288),(427,321)]))+L(298,453,462,453,TEAL_D,6)
    if w=='look':return g+person(shirt=RED,hands=([(304,342)],[(479,248),(429,160)]))+hand(405,160,90,.29)+P('M 475 181 L 605 160 M 477 198 L 610 214',stroke=TEAL_L,w=5)+tree_round(625,405,.4)
    if w=='listen':return g+person(shirt=TEAL,hands=([(311,340)],[(480,272),(450,196)]))+hand(457,177,10,.29)+P('M 550 172 Q 588 203 550 235 M 580 151 Q 640 203 580 256',stroke=YEL,w=7)
    if w=='dance':return g+f'<g transform="rotate(-12 380 430)">{person(y=417,pose="stride",arms="up",shirt=PINK,face="open")}</g>'+P('M 190 360 Q 135 288 210 218 M 552 235 Q 622 306 551 367',stroke=YEL,w=8)+star5(238,170,18,TEAL)+star5(545,150,24,RED)
    if w=='sing':return g+person(shirt=BLUE,face='open',hands=([(313,340)],[(455,300),(474,296)]))+L(474,336,474,253,INK,11)+E(474,246,22,29,INK)+P('M 536 200 Q 570 221 536 244 M 570 170 Q 630 221 570 274',stroke=TEAL,w=7)
    if w=='clap':return g+person(shirt=YEL,arms='clap')+P('M 350 274 L 334 251 M 380 265 L 380 238 M 410 274 L 426 251',stroke=RED,w=6)
    if w=='wave':return g+person(shirt=TEAL,hands=([(314,340)],[(482,251),(484,171)]))+hand(484,140,0,.34)+P('M 543 119 Q 570 147 543 175 M 568 100 Q 610 146 568 193',stroke=YEL,w=6)
    if w=='point':return g+person(x=305,shirt=BLUE,arms='point',point_at=(575,217))+E(580,194,27,19,PINK)+E(620,194,27,19,YEL)+E(581,225,20,15,PINK)+E(620,225,20,15,YEL)+L(600,191,600,230,INK,8)
    if w=='kick':return g+person(x=320,y=410,pose='sprint',arms='pump',shirt=RED)+ball(519,388,62,YEL,YEL_D,SUN_L)+P('M 466 405 Q 529 326 604 315',stroke=TEAL,w=5)
    if w=='push':return g+box(520,282,190,145,False)+person(x=310,shirt=TEAL,pose='stride',hands=([(389,305),(420,335)],[(392,288),(424,312)]))+motion(577,332,1,YEL)
    if w=='pull':return g+R(480,333,160,68,16,YEL)+C(507,420,22,INK)+C(615,420,22,INK)+L(478,351,348,315,WOOD_D,12)+person(x=286,shirt=BLUE,pose='stride',hands=([(224,342)],[(350,315)]))
    if w=='throw':return g+person(x=300,shirt=YEL,hands=([(235,340)],[(400,247),(455,202)]))+ball(554,177,42,RED,RED_D,PINK)+P('M 458 197 Q 509 100 596 170',stroke=TEAL,w=5)
    if w=='catch':return g+person(x=365,shirt=TEAL,hands=([(283,225),(295,190)],[(447,225),(435,190)]))+ball(365,120,53,YEL,YEL_D,SUN_L)+P('M 370 30 L 370 51 M 385 39 L 385 61',stroke=RED,w=5)
    if w=='hug':return g+person(x=325,y=430,s=.94,shirt=RED,hands=([(292,314),(390,314)],[(412,288),(417,320)]))+person(x=428,y=430,s=.94,shirt=TEAL,hands=([(346,289),(340,320)],[(463,314),(366,314)]))+heart(380,95,26)
    raise KeyError(w)


def arts():return {c['w']:drawing(c['w']) for c in GROUP_CARDS}
