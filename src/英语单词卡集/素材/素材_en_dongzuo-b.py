#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生活动作22卡。每张图画出手、工具和正在发生的变化。"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from 动作组件_en import *
GROUP_CARDS=[{'w':w,'cn':cn} for w,cn in [('eat','吃'),('drink','喝'),('sleep','睡觉'),('wake up','起床'),('brush','刷'),('wash','洗'),('comb','梳头'),('bath','洗澡'),('open','打开'),('close','关上'),('cut','剪'),('write','写'),('draw','画'),('read','读'),('count','数'),('color','涂色'),('fold','折'),('build','搭'),('cook','做饭'),('sweep','扫地'),('plant','种'),('pick','摘')]]


def meal_table():return R(145,340,430,26,10,WOOD)+R(172,364,26,76,8,WOOD_D)+R(522,364,26,76,8,WOOD_D)


def paint_scene(fill):
    g=R(102,140,275,252,12,WOOD)+R(118,156,243,220,8,WHITE)+L(140,390,120,448,WOOD,14)+L(334,390,352,448,WOOD,14)
    g+=C(228,243,58,fill)
    for xx,yy in ((228,164),(228,321),(150,243),(306,243),(174,189),(282,189),(174,297),(282,297)):
        g+=L(xx,yy,xx+(xx-228)*.16,yy+(yy-243)*.16,YEL,7)
    g+=person(x=493,y=438,s=.9,shirt=TEAL,hands=([(414,299),(346,268)],[(551,340)]))+L(348,268,297,248,RED,10)
    return g


def drawing(w):
    g=ground()
    if w=='eat':return g+person(x=390,y=438,pose='sit',shirt=RED,face='open',hands=([(312,303)],[(470,285),(412,224)]))+meal_table()+bowl(274,331,62)+spoon(412,224,428,220,True)
    if w=='drink':
        g+=person(shirt=TEAL,hands=([(313,338)],[(470,263),(418,228)]))
        vessel=R(-30,-25,60,78,10,BLUE)+R(-22,-17,43,14,7,WBLUE)+R(-22,-8,9,40,5,WHITE,.7)
        return g+f'<g transform="translate(420 222) rotate(-30)">{vessel}</g>'
    if w=='sleep':
        g+=R(120,340,530,82,18,WOOD)+R(135,321,500,47,15,WHITE)+R(144,415,24,32,8,WOOD_D)+R(600,415,24,32,8,WOOD_D)
        g+=kid(x=322,y=377,s=1.3,pose='sleep',shirt=BLUE)+R(285,320,250,62,20,BLUE)
        return g+P('M 575 102 A 50 50 0 1 0 626 161 A 43 43 0 0 1 575 102 Z',YEL)+star5(656,114,15,YEL)
    if w=='wake up':return g+R(165,335,430,93,18,WOOD)+R(178,326,407,60,16,BLUE)+person(x=367,y=400,s=.85,pose='sit',arms='up',shirt=YEL,face='open')+C(590,140,49,SUN)+L(590,67,590,80,SUN,8)+L(661,140,677,140,SUN,8)
    if w=='brush':return g+person(face='open',shirt=BLUE,hands=([(313,337)],[(484,260),(417,224)]))+L(418,224,365,218,TEAL,12)+R(349,201,36,17,5,WHITE)+C(364,224,12,WHITE)+C(385,225,9,WHITE)+C(353,238,9,WHITE)
    if w=='wash':return g+person(x=470,y=439,s=.93,shirt=YEL,arms='reach')+R(125,310,265,46,20,TEAL)+R(140,354,25,87,8,TEAL_D)+L(235,185,235,276,WBLUE,15)+P('M 286 176 L 286 149 Q 286 132 260 132 L 235 132 L 235 178',stroke='#a4afb6',w=18)+L(276,119,302,119,INK,9)+C(252,293,15,WHITE)+C(280,303,14,WHITE)+C(317,294,10,WHITE)
    if w=='comb':return g+person(shirt=TEAL,hands=([(312,337)],[(479,218),(433,141)]))+f'<g transform="translate(426 127) rotate(25)">'+R(-45,-8,90,16,7,WOOD)+''.join(R(-40+i*15,4,8,31,3,WOOD_D) for i in range(6))+'</g>'
    if w=='bath':return g+person(y=428,s=.9,arms='up',shirt=BLUE)+R(155,301,450,130,55,TEAL)+R(142,290,476,33,16,TEAL_L)+E(380,301,211,28,WHITE)+C(288,283,32,WHITE)+C(335,282,25,WHITE)+C(478,285,34,WHITE)+C(211,235,19,WHITE)+C(548,191,24,WHITE)+C(565,240,13,WHITE)
    if w in ('open','close'):
        g+=R(390,119,186,318,9,WOOD_D)+R(407,135,153,301,4,'#fbe8ab')
        if w=='open':g+=PG([(408,135),(492,175),(492,438),(408,436)],WOOD)+C(473,295,9,YEL)+P('M 540 252 Q 574 277 542 309',stroke=TEAL,w=6)
        else:g+=R(407,135,153,301,5,WOOD)+R(429,164,109,111,6,WOOD_L)+C(535,304,9,YEL)+P('M 610 252 L 570 277 M 610 304 L 570 277',stroke=TEAL,w=7)
        return g+person(x=267,y=438,s=.9,shirt=RED if w=='open' else BLUE,hands=([(208,338)],[(361,295),(409,303)]))
    if w=='cut':return g+person(x=499,y=438,s=.88,shirt=YEL,hands=([(414,306),(392,300)],[(549,342)]))+R(132,245,250,124,6,PINK)+P('M 275 245 L 275 321',stroke=WHITE,w=4)+L(360,300,250,240,'#c9cdd1',17)+L(360,300,249,338,'#a4afb6',17)+E(392,278,34,20,TEAL)+E(390,322,34,20,TEAL)+C(360,301,9,WOOD_D)
    if w=='write':return g+person(x=420,y=438,s=.9,pose='sit',shirt=BLUE,hands=([(342,319)],[(490,296),(427,313)]))+meal_table()+R(273,317,164,24,7,WHITE)+L(426,313,455,264,YEL,9)+P('M 300 327 Q 323 317 339 327 T 380 327',stroke=INK,w=3)
    if w=='draw':return g+paint_scene(YEL)
    if w=='read':return g+person(y=438,pose='sit',shirt=RED,hands=([(301,299)],[(459,299)]))+book(380,301,.83,TEAL)
    if w=='count':return g+person(x=250,y=438,s=.92,shirt=TEAL,hands=([(182,310)],[(345,300)]))+R(419,345,72,79,8,RED)+R(500,345,72,79,8,BLUE)+R(456,259,75,78,8,YEL)+L(356,298,391,299,SKIN,13)
    if w=='color':
        scene=paint_scene('#fbf0c2')
        scene+=P('M 228 185 A 58 58 0 0 1 286 243 L 228 243 Z',YEL)+L(298,248,273,243,YEL,17)
        return g+scene
    if w=='fold':return g+person(x=492,y=438,s=.88,shirt=YEL,hands=([(417,307),(348,330)],[(543,304),(407,337)]))+R(110,355,337,23,8,WOOD)+PG([(160,348),(365,348),(300,219)],BLUE)+PG([(300,219),(300,348),(365,348)],TEAL_L)+P('M 300 220 L 300 348',stroke=BLUE_D,w=4)
    if w=='build':return g+person(x=240,y=438,s=.93,shirt=RED,hands=([(181,336)],[(341,258),(432,210)]))+R(435,355,165,72,9,TEAL)+R(462,277,110,72,9,YEL)+R(485,199,65,72,8,BLUE)+L(432,210,475,211,SKIN,17)
    if w=='cook':return g+person(x=270,y=438,s=.95,shirt=TEAL,hands=([(203,338)],[(370,281),(460,294)]))+R(213,125,115,30,10,WHITE)+C(235,119,23,WHITE)+C(272,109,26,WHITE)+C(309,119,23,WHITE)+R(415,315,220,96,20,RED)+E(525,316,110,23,RED_D)+L(460,294,529,354,WOOD,13)+P('M 524 275 Q 548 256 528 238 M 582 272 Q 606 250 584 232',stroke='#d2cabc',w=6)
    if w=='sweep':return g+person(x=340,y=438,s=.95,shirt=BLUE,hands=([(271,303),(340,320)],[(414,287),(400,295)]))+L(378,262,453,375,WOOD,15)+PG([(423,359),(479,346),(531,423),(428,441)],YEL)+''.join(L(435+i*14,370,444+i*20,430,YEL_D,4) for i in range(4))+C(551,434,8,WOOD_D)+C(591,426,6,WOOD_D)+C(569,407,5,WOOD_D)
    if w=='plant':return g+person(x=263,y=439,s=.9,pose='sit',shirt=YEL,hands=([(187,336)],[(365,310),(443,358)]))+E(505,422,116,23,WOOD_D)+L(502,403,502,303,GREEN,12)+E(467,326,44,21,GREEN)+E(538,301,44,21,GREEN_L)+P('M 434 352 L 478 360 L 466 396 L 430 386 Z',TEAL)+P('M 474 364 L 502 376 L 492 394 Z',TEAL)+L(498,392,500,414,WBLUE,5)
    if w=='pick':return g+tree_round(500,436,1.04)+apple(463,245,.48)+apple(580,251,.46)+person(x=281,y=435,s=.9,shirt=RED,hands=([(223,341)],[(373,225),(412,206)]))+apple(421,195,.45)+R(167,381,118,54,14,WOOD_L)
    raise KeyError(w)


def arts():return {c['w']:drawing(c['w']) for c in GROUP_CARDS}
