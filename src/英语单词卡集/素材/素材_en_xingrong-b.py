#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""形容对比下20卡：状态变化、可见触感和数量参照。"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from 动作组件_en import *
GROUP_CARDS=[{'w':w,'cn':cn} for w,cn in [('wet','湿的'),('dry','干的'),('clean','干净的'),('dirty','脏的'),('empty','空的'),('full','满的'),('bright','明亮的'),('dark','黑暗的'),('loud','响的'),('quiet','安静的'),('straight','直的'),('curly','卷的'),('sweet','甜的'),('sour','酸的'),('spicy','辣的'),('salty','咸的'),('delicious','好吃的'),('many','许多'),('few','少量'),('broken','坏的')]]


def plate():return E(380,383,236,56,WHITE)+E(380,380,207,42,'#e2e8e5')+E(380,379,183,34,WHITE)


def room(dark=False):
    bg='#536774' if dark else '#f6e5b9'
    g=R(103,113,554,322,24,bg)+R(465,151,134,125,8,'#a2b1c1' if dark else WBLUE)+L(532,151,532,275,WHITE,7)+L(466,215,598,215,WHITE,7)
    if dark:g+=P('M 560 165 A 24 24 0 1 0 578 202 A 22 22 0 0 1 560 165 Z',YEL)+star5(490,180,10,WHITE)
    g+=L(275,206,275,417,INK,10)+E(275,421,69,14,INK)+PG([(222,173),(328,173),(353,249),(197,249)],'#aeb6b6' if dark else YEL)
    if not dark:g+=PG([(212,251),(338,251),(423,425),(128,425)],'#f9d977')+L(180,167,156,148,YEL,7)+L(370,167,395,146,YEL,7)
    return g


def drawing(w):
    g=ground()
    if w=='wet':
        g+=cloud_p(380,108,1.7,'#bdc8d0')+person(shirt=BLUE,face='sad')
        for xx,yy in ((220,184),(278,268),(471,194),(521,310),(317,363),(446,387)):g+=drop(xx,yy,12,WBLUE)
        return g+E(380,444,145,20,WBLUE,.65)
    if w=='dry':return g+L(126,194,646,194,WOOD,8)+L(139,194,139,439,WOOD_D,12)+L(635,194,635,439,WOOD_D,12)+PG([(243,214),(286,215),(310,256),(283,274),(278,359),(208,359),(208,274),(184,257),(211,214)],YEL)+PG([(427,213),(472,213),(498,253),(474,272),(471,357),(397,357),(398,272),(374,253),(401,213)],PINK)+R(224,182,13,48,5,WOOD_L)+R(432,182,13,48,5,WOOD_L)+C(572,107,42,SUN)
    if w=='clean':return g+person(shirt=TEAL,arms='up')+star5(259,177,30,YEL)+star5(507,271,22,YEL)+R(153,349,106,71,15,WHITE)+C(163,325,18,WBLUE)+C(228,302,12,WBLUE)
    if w=='dirty':return g+E(380,423,240,30,WOOD_D)+E(377,316,160,101,PINK)+C(235,294,73,PINK)+E(185,315,43,30,'#e88c82')+C(172,316,7,RED_D)+C(195,316,7,RED_D)+C(236,282,7,INK)+PG([(224,244),(223,195),(266,240)],PINK)+R(297,385,25,51,10,PINK)+R(469,385,25,51,10,PINK)+E(333,320,61,36,WOOD_D)+E(439,283,42,22,WOOD_D)+C(222,333,18,WOOD_D)
    if w=='empty':return g+plate()+P('M 229 325 L 231 298 M 215 312 L 245 312',stroke=YEL,w=6)+E(380,377,83,12,'#f4f3eb')
    if w=='full':
        g+=plate()
        for xx,yy in ((233,346),(332,350),(432,350),(527,346),(289,267),(387,267),(479,267),(342,189),(433,191),(388,125)):g+=apple(xx,yy,.56)
        return g
    if w=='bright':return g+room(False)
    if w=='dark':return g+room(True)
    if w=='loud':return g+R(260,255,240,143,35,RED)+E(380,255,120,35,WHITE)+E(380,397,120,24,RED_D)+L(267,158,361,244,WOOD,13)+L(493,156,402,242,WOOD,13)+C(267,158,20,YEL)+C(493,156,20,YEL)+P('M 190 255 Q 135 312 190 368 M 562 254 Q 619 312 562 370 M 151 220 Q 70 312 151 405 M 606 220 Q 687 312 606 405',stroke=TEAL,w=8)
    if w=='quiet':return g+person(x=272,shirt=TEAL,hands=([(205,337)],[(355,267),(283,222)]))+R(277,206,11,37,6,SKIN)+kid(x=521,y=409,s=.8,pose='sleep',shirt=BLUE)+P('M 580 167 A 36 36 0 1 0 610 212 A 31 31 0 0 1 580 167 Z',YEL)
    if w=='straight':
        g+=PG([(239,437),(521,437),(430,119),(330,119)],'#a9b5bb')
        for yy,hh in ((150,30),(209,37),(282,43),(365,52)):g+=R(375,yy,10,hh,3,WHITE)
        return g+tree_round(164,401,.4)+tree_round(603,400,.4)
    if w=='curly':
        g+=person(shirt=YEL)
        for xx,yy in ((325,143),(342,125),(365,118),(389,118),(412,125),(435,143)):g+=P(f'M {xx-10} {yy} C {xx-18} {yy-22} {xx+17} {yy-22} {xx+10} {yy} C {xx+3} {yy+13} {xx-7} {yy+9} {xx-5} {yy+1}',stroke=HAIR,w=10)
        return g+C(569,389,48,PINK)+P('M 550 379 Q 587 359 589 390 Q 585 419 554 402 Q 534 380 576 381 M 609 418 Q 641 448 663 413',stroke=RED_D,w=5)
    if w=='sweet':return g+person(x=260,shirt=YEL,hands=([(200,337)],[(353,280),(294,223)]))+R(442,273,160,151,32,'#e8b448')+R(432,258,180,28,10,WOOD)+E(524,320,54,29,SUN_L)+P('M 451 279 Q 425 332 444 360 Q 467 366 462 325',YEL_D)+heart(542,165,32,PINK)
    if w=='sour':return g+person(shirt=TEAL,eyes=P('M 344 181 L 357 188 L 344 196 M 417 181 L 404 188 L 417 196',stroke=INK,w=6),mouth=P('M 356 223 L 370 218 L 382 226 L 396 219',stroke=INK,w=6),hands=([(313,339)],[(463,264),(410,236)]))+E(425,239,37,23,YEL)+E(537,373,77,61,YEL)+P('M 476 373 Q 537 322 600 373',stroke=SUN_L,w=9)
    if w=='spicy':return g+person(shirt=RED,face='open',hands=([(305,291),(330,254)],[(461,286),(408,233)]))+P('M 394 228 Q 432 228 430 267 Q 406 264 394 228 Z',RED_D)+PG([(318,248),(255,210),(275,295)],TEAL)+P('M 524 367 Q 615 350 585 416 Q 560 440 547 434 Q 580 403 524 367 Z',RED)+L(525,367,512,346,GREEN,9)+drop(435,171,12,WBLUE)
    if w=='salty':return g+R(244,321,246,103,23,RED)+''.join(R(265+i*33,242-i%2*20,21,108,7,YEL) for i in range(6))+f'<g transform="translate(518 177) rotate(28)">'+R(-35,-48,70,98,12,WHITE)+R(-36,31,72,22,8,'#aab5b9')+C(-14,43,4,INK)+C(9,43,4,INK)+'</g>'+''.join(C(476+i*9,237+i*16,3,WHITE) for i in range(6))
    if w=='delicious':return g+person(shirt=BLUE,face='open',hands=([(300,291),(330,314)],[(460,291),(430,314)]))+bowl(380,311,82)+P('M 407 220 Q 422 227 410 238',stroke=PINK,w=9)+star5(535,188,26,YEL)+heart(228,160,26,PINK)
    if w in ('many','few'):
        g+=plate()
        coords=[(251,352),(333,350),(418,350),(501,352),(293,284),(378,284),(461,284),(337,216),(421,216),(378,149)] if w=='many' else [(330,352),(434,352)]
        for xx,yy in coords:g+=apple(xx,yy,.53)
        return g
    if w=='broken':return g+R(195,268,325,119,28,RED)+R(235,202,196,91,23,BLUE)+R(258,218,69,55,9,WBLUE)+R(342,218,69,55,9,WBLUE)+C(272,392,44,INK)+C(272,392,21,'#cbd1d2')+L(466,391,502,391,INK,13)+C(591,410,44,INK)+C(591,410,22,'#cbd1d2')+PG([(527,344),(542,357),(523,366)],RED)+PG([(546,383),(565,371),(564,394)],WOOD)
    raise KeyError(w)


def arts():return {c['w']:drawing(c['w']) for c in GROUP_CARDS}
