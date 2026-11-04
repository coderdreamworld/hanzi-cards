#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""方位21卡，共用橘猫和纸箱，改变空间关系而非只换文案。"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from 动作组件_en import *
GROUP_CARDS=[{'w':w,'cn':cn} for w,cn in [('in','在里面'),('on','在上面'),('under','在下面'),('above','在上方'),('behind','在后面'),('beside','在旁边'),('between','在中间'),('near','在近处'),('far','在远处'),('up','向上'),('down','向下'),('left','左'),('right','右'),('through','穿过'),('around','绕着'),('forward','向前'),('backward','向后'),('outside','在外面'),('here','这里'),('there','那里'),('middle','中间')]]


def cat(x,y,s=1,flip=1):
    g=P('M 44 7 Q 112 2 93 -66',stroke=YEL_D,w=20)+E(0,0,52,73,YEL)+E(-20,66,30,13,YEL_D)+E(28,66,25,13,YEL_D)
    g+=C(0,-85,52,YEL)+PG([(-46,-103),(-44,-153),(-13,-126)],YEL)+PG([(13,-126),(45,-153),(47,-103)],YEL)+PG([(-38,-111),(-37,-139),(-20,-122)],PINK)+PG([(22,-123),(38,-140),(40,-110)],PINK)
    g+=E(-20,-88,6,9,INK)+E(20,-88,6,9,INK)+C(-22,-91,2,WHITE)+C(18,-91,2,WHITE)+PG([(-7,-70),(7,-70),(0,-63)],RED_D)+P('M 0 -63 Q -10 -48 -19 -57 M 0 -63 Q 10 -48 19 -57',stroke=INK,w=3)
    for yy in (-71,-62):g+=L(-37,yy,-77,yy-8,INK,3)+L(37,yy,77,yy-8,INK,3)
    return f'<g transform="translate({x} {y}) scale({s*flip} {s})">{g}</g>'


def carton(x,y,w=190,h=140):
    return R(x-w/2,y-h,w,h,12,WOOD)+R(x-w/2,y-h,w,21,9,WOOD_D)+R(x-12,y-h+22,24,h-22,2,WOOD_L)+L(x-w/2+17,y-h+42,x-w/2+58,y-h+42,WOOD_D,5)


def arrow(x1,y1,x2,y2,color=TEAL):
    import math
    a=math.atan2(y2-y1,x2-x1);r=20
    return L(x1,y1,x2,y2,color,9)+PG([(x2,y2),(x2-r*math.cos(a-.55),y2-r*math.sin(a-.55)),(x2-r*math.cos(a+.55),y2-r*math.sin(a+.55))],color)


def fish(x,y,s=1):
    g=E(0,0,42,22,BLUE)+PG([(32,0),(65,-23),(65,23)],BLUE_D)+C(-22,-5,5,INK)
    return f'<g transform="translate({x} {y}) scale({s})">{g}</g>'


def drawing(w):
    g=ground()
    if w=='in':return g+E(380,319,111,32,WOOD_D)+cat(380,326,.78)+R(267,339,226,92,9,WOOD)+R(369,340,22,90,2,WOOD_L)+PG([(268,319),(241,353),(268,370)],WOOD_L)+PG([(492,319),(520,353),(492,370)],WOOD_L)
    if w=='on':return g+carton(380,438,230,153)+cat(380,225,.75)
    if w=='under':return g+R(180,220,405,36,12,WOOD)+R(199,255,29,180,8,WOOD_D)+R(540,255,29,180,8,WOOD_D)+cat(380,376,.63)
    if w=='above':return g+carton(380,438,238,141)+E(380,139,49,62,RED)+P('M 380 201 Q 355 231 381 259',stroke=WOOD_D,w=3)+PG([(375,201),(386,201),(381,211)],RED_D)
    if w=='behind':return g+cat(405,340,.9)+carton(367,438,250,181)
    if w=='beside':return g+carton(305,438,207,165)+cat(518,370,.85)
    if w=='between':return g+carton(180,438,170,175)+carton(578,438,170,175)+cat(380,369,.87)
    if w=='near':return g+carton(280,438,217,168)+cat(464,370,.85)+L(382,441,414,441,TEAL,6)
    if w=='far':return g+carton(236,438,238,183)+cat(606,221,.44)+P('M 381 410 Q 493 390 529 273',stroke=TEAL_L,w=6)+E(610,258,65,10,GROUND)
    if w in ('up','down'):
        for i in range(4):g+=R(147+i*117,375-i*69,118,67+i*69,5,WOOD_L)+R(147+i*117,375-i*69,118,15,5,WOOD)
        if w=='up':return g+cat(405,200,.68)+arrow(208,305,560,102)
        return g+cat(327,305,.68,-1)+arrow(584,101,217,304)
    if w in ('left','right'):
        g+=R(372,155,15,280,4,WOOD_L)
        if w=='left':return g+cat(254,367,.82,-1)+fish(133,318,.58)+arrow(544,171,204,171)
        return g+cat(505,367,.82)+fish(625,318,.58)+arrow(213,171,554,171)
    if w=='through':return g+R(215,225,320,204,80,WOOD)+E(229,327,78,101,WOOD_D)+cat(242,370,.7)+E(539,328,60,101,WOOD_L)+P('M 528 244 Q 455 226 406 244',stroke=WOOD_D,w=4)+arrow(600,171,163,171)
    if w=='around':return g+tree_round(380,437,.9)+P('M 241 346 C 90 430 600 490 606 356 C 601 313 551 295 510 300',stroke=TEAL_L,w=8)+cat(234,374,.66)+arrow(562,412,603,364)
    if w in ('forward','backward'):
        g+=R(545,273,86,147,12,WOOD)+PG([(530,273),(588,230),(647,273)],RED)+fish(590,319,.45)
        if w=='forward':return g+cat(356,367,.84)+arrow(226,155,504,155)
        return g+cat(356,367,.84)+arrow(504,155,226,155)+P('M 254 350 L 225 350 M 264 377 L 235 377',stroke=TEAL_L,w=5)
    if w=='outside':return g+R(112,206,250,233,10,WHITE)+PG([(90,206),(235,111),(382,206)],RED)+R(164,260,135,111,9,WBLUE)+cat(234,333,.4)+cat(549,369,.86)+L(405,433,646,433,GREEN,6)
    if w=='here':return g+person(x=294,y=438,s=.92,shirt=YEL,arms='point',point_at=(425,391))+cat(456,386,.52)
    if w=='there':return g+person(x=246,y=438,s=.92,shirt=TEAL,arms='point',point_at=(588,279))+cat(592,290,.46)+arrow(413,241,521,241)
    if w=='middle':return g+apple(174,373,.7)+apple(600,373,.7)+cat(380,365,.88)+L(380,124,380,176,TEAL,7)+PG([(380,194),(366,174),(394,174)],TEAL)
    raise KeyError(w)


def arts():return {c['w']:drawing(c['w']) for c in GROUP_CARDS}
