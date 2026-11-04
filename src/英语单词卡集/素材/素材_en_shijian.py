#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""时间季节21卡：相同时间轴标记当天，连环情境解释相对日期。"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from 动作组件_en import *
GROUP_CARDS=[{'w':w,'cn':cn} for w,cn in [('day','白天'),('night','夜晚'),('morning','早晨'),('noon','中午'),('afternoon','下午'),('evening','傍晚'),('today','今天'),('tomorrow','明天'),('yesterday','昨天'),('early','早的'),('late','晚的'),('spring','春天'),('summer','夏天'),('autumn','秋天'),('winter','冬天'),('birthday','生日'),('holiday','假期'),('weekend','周末'),('calendar','日历'),('alarm clock','闹钟'),('season','季节')]]


def sunshine(x,y,r=44):
    import math
    g=C(x,y,r,SUN)
    for i in range(10):
        a=i*math.pi/5;g+=L(x+(r+11)*math.cos(a),y+(r+11)*math.sin(a),x+(r+25)*math.cos(a),y+(r+25)*math.sin(a),SUN,6)
    return g


def moon(x,y,r=45):return P(f'M {x} {y-r} A {r} {r} 0 1 0 {x+r*.7} {y+r*.75} A {r*.85} {r*.85} 0 0 1 {x} {y-r} Z',YEL)


def field(sky='#d9eef1'):return R(94,78,572,365,30,sky)+P('M 94 369 Q 270 329 382 368 Q 533 330 666 365 L 666 443 L 94 443 Z',GROUND)


def calendar(x=380,y=273,s=1,active=10):
    g=R(-220,-157,440,318,24,WHITE)+R(-220,-157,440,65,23,RED)+R(-220,-122,440,30,2,RED)+L(-133,-180,-133,-134,WOOD_D,13)+L(133,-180,133,-134,WOOD_D,13)
    for row in range(4):
        for col in range(7):
            xx=-179+col*59;yy=-59+row*55
            g+=R(xx-19,yy-18,39,37,7,PINK if col>=5 else '#e1eee8')
            if row*7+col==active:g+=C(xx,yy,25,YEL)+star5(xx,yy,14,WHITE)
    return f'<g transform="translate({x} {y}) scale({s})">{g}</g>'


def day_triptych(which):
    g=''
    for i in range(3):
        x=120+i*190;g+=R(x,169,165,219,20,'#e3ece9')+sunshine(x+82,214,24)+E(x+82,360,58,13,GROUND)
        if i==1:g+=person(x=x+82,y=364,s=.4,shirt=TEAL)
        elif i==0:g+=P(f'M {x+66} 319 L {x+83} 332 L {x+114} 296',stroke=TEAL,w=9)
        else:g+=R(x+52,298,61,59,10,YEL)+R(x+76,298,13,59,3,RED)
        if i==which:g+=R(x-5,163,175,8,4,YEL)+R(x-5,386,175,8,4,YEL)+R(x-5,163,8,230,4,YEL)+R(x+162,163,8,230,4,YEL)
    g+=L(224,116,598,116,TEAL,7)+PG([(615,116),(590,102),(590,130)],TEAL)
    g+=L(392,397,392,425,TEAL,6)+C(392,434,9,TEAL)
    return g


def drawing(w):
    g=ground()
    if w=='day':return g+field()+sunshine(565,143)+person(x=324,y=423,s=.8,pose='stride',shirt=YEL)+ball(454,388,42)
    if w=='night':return g+field('#536575')+moon(540,137,48)+star5(210,131,14,WHITE)+star5(371,164,13,YEL)+kid(x=332,y=400,s=1.25,pose='sleep',shirt=BLUE)
    if w=='morning':return g+field('#f9e8c2')+C(190,307,62,SUN)+P('M 94 330 Q 252 298 387 334 L 666 365 L 666 443 L 94 443 Z',GROUND)+R(368,274,91,89,20,RED)+person(x=409,y=426,s=.78,pose='stride',shirt=TEAL)+R(563,262,57,171,7,WOOD)
    if w=='noon':return g+field()+sunshine(380,129,43)+E(380,434,50,9,TEAL_D,.45)+person(x=380,y=428,s=.79,shirt=YEL)
    if w=='afternoon':return g+field()+sunshine(578,246,36)+P('M 344 426 L 171 433 Q 140 435 162 445 L 344 437 Z','#91b4ab')+person(x=355,y=430,s=.8,pose='stride',shirt=RED)
    if w=='evening':return g+field('#f4c29e')+C(566,349,58,RED)+L(172,192,172,430,INK,11)+PG([(139,183),(205,183),(220,227),(124,227)],YEL)+person(x=376,y=431,s=.8,pose='stride',shirt=BLUE)
    if w=='today':return g+day_triptych(1)+person(x=380,y=118,s=.25,shirt=TEAL)
    if w=='tomorrow':return g+day_triptych(2)+P('M 421 409 Q 511 455 580 403',stroke=TEAL,w=6)+PG([(591,396),(565,398),(579,418)],TEAL)
    if w=='yesterday':return g+day_triptych(0)+P('M 359 409 Q 272 455 204 403',stroke=TEAL,w=6)+PG([(192,396),(204,418),(218,398)],TEAL)
    if w=='early':return g+field('#f6ddb9')+C(552,345,51,SUN)+person(x=342,y=427,s=.83,shirt=TEAL)+R(289,253,105,19,7,RED)+R(334,273,37,96,9,RED)+cloud_p(208,137,.6,'#e7d1c0')
    if w=='late':return g+field('#c3b9bd')+C(568,371,52,RED)+person(x=341,y=421,s=.8,pose='sprint',arms='pump',shirt=YEL)+R(541,280,91,153,7,WOOD)+PG([(529,281),(587,236),(646,281)],RED_D)+motion(155,306)
    if w=='spring':
        g+=tree_round(385,437,1.04,leaf='#e5a8bb',leaf_l='#f5c9d5')
        for xx,yy in ((317,182),(427,146),(478,229),(348,281),(285,236)):g+=flower5(xx,yy,22,'#f9dbe4',YEL)
        return g+P('M 145 180 Q 186 147 212 180 Q 239 147 277 180 M 212 180 L 212 208',stroke=INK,w=7)
    if w=='summer':return g+sunshine(544,131,50)+person(x=335,y=436,s=.9,shirt=YEL)+E(337,337,103,43,TEAL)+E(337,337,71,23,PAGE)+E(565,409,74,26,RED)+P('M 491 409 Q 565 475 639 409',stroke=GREEN,w=9)
    if w=='autumn':return g+tree_round(380,438,1.08,leaf=RED,leaf_l=YEL)+E(191,292,24,12,RED)+E(572,336,24,13,YEL)+E(245,414,24,12,RED_D)+P('M 570 208 Q 605 272 567 302',stroke=WOOD_L,w=4)
    if w=='winter':return g+field('#d5e8ed')+C(501,362,72,WHITE)+C(501,265,49,WHITE)+C(483,259,5,INK)+C(518,259,5,INK)+PG([(500,270),(544,280),(499,285)],YEL)+person(x=275,y=430,s=.84,shirt=BLUE)+R(226,285,100,26,10,RED)+R(283,311,28,58,8,RED)+star5(571,119,26,WHITE)+star5(216,119,22,WHITE)
    if w=='birthday':
        g+=R(226,251,309,157,30,PINK)+E(380,253,154,39,WHITE)+P('M 226 261 Q 254 310 275 269 Q 298 302 320 267 Q 345 301 367 270 Q 389 300 412 268 Q 440 300 462 267 Q 500 311 535 260',stroke=WHITE,w=22)
        for xx in (300,380,460):g+=R(xx-8,183,16,65,4,TEAL)+drop(xx,165,14,YEL)
        return g+R(565,329,94,89,10,TEAL)+R(600,326,16,92,3,YEL)+star5(171,179,25,YEL)
    if w=='holiday':return g+R(154,210,250,211,31,TEAL)+R(235,179,89,41,12,TEAL_D)+L(249,187,308,187,PAGE,10)+R(190,235,18,155,9,TEAL_L)+R(351,235,18,155,9,TEAL_L)+C(207,432,14,INK)+C(350,432,14,INK)+R(456,294,183,112,18,INK)+C(548,350,41,BLUE)+C(548,350,25,INK)+R(478,279,53,22,6,INK)+sunshine(560,153,37)
    if w=='weekend':return g+calendar(227,264,.52,5)+person(x=521,y=438,s=.8,shirt=RED,arms='up')+PG([(578,85),(622,133),(578,181),(534,133)],YEL)+L(579,182,556,261,WOOD_D,2)+P('M 575 181 Q 622 218 591 245',stroke=TEAL,w=5)+flower5(377,410,20,PINK)
    if w=='calendar':return g+calendar()
    if w=='alarm clock':return g+C(380,290,131,TEAL)+C(380,290,111,WHITE)+E(271,150,60,33,YEL)+E(489,150,60,33,YEL)+L(300,390,275,437,TEAL_D,21)+L(460,390,485,437,TEAL_D,21)+L(380,180,380,148,INK,8)+L(359,143,401,143,INK,8)+L(380,290,380,215,INK,10)+L(380,290,438,318,INK,10)+C(380,290,13,YEL)+P('M 193 182 Q 150 150 191 116 M 567 116 Q 610 150 567 182',stroke=RED,w=7)
    if w=='season':
        for i,(col,leaf) in enumerate((('#f4e7eb',PINK),('#deedce',GREEN),('#f5dfba',RED),('#dbe9ec',WHITE))):
            xx=119+i*137;g+=R(xx,132,128,292,14,col)+tree_round(xx+64,410,.38,leaf=leaf,leaf_l=leaf)
        return g
    raise KeyError(w)


def arts():return {c['w']:drawing(c['w']) for c in GROUP_CARDS}
