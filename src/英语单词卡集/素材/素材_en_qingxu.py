#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""情绪感受20卡：不同表情、身体姿态和具体情境共同表意。"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from 动作组件_en import *
GROUP_CARDS=[{'w':w,'cn':cn} for w,cn in [('happy','开心'),('sad','难过'),('angry','生气'),('cry','哭'),('laugh','大笑'),('smile','微笑'),('tired','累'),('sleepy','困'),('hungry','饿'),('thirsty','渴'),('scared','害怕'),('surprised','惊讶'),('bored','无聊'),('sick','生病'),('love','爱'),('like','喜欢'),('share','分享'),('help','帮助'),('brave','勇敢'),('proud','自豪')]]


def eyebrows(x=380,y=192,kind='sad'):
    if kind=='angry':return P(f'M {x-37} {y-43} L {x-8} {y-29} M {x+8} {y-29} L {x+37} {y-43}',stroke=HAIR,w=7)
    return P(f'M {x-37} {y-29} L {x-9} {y-43} M {x+9} {y-43} L {x+37} {y-29}',stroke=HAIR,w=6)


def shut(x=380,y=192):return P(f'M {x-34} {y-6} Q {x-22} {y+4} {x-10} {y-6} M {x+10} {y-6} Q {x+22} {y+4} {x+34} {y-6}',stroke=INK,w=7)


def drawing(w):
    g=ground()
    if w=='happy':return g+person(shirt=YEL,arms='up',face='open')+star5(225,140,28,RED)+star5(537,190,21,TEAL)+P('M 200 290 L 220 271 M 553 300 L 580 324',stroke=BLUE,w=9)
    if w=='sad':return g+person(shirt=BLUE,face='sad',brows=eyebrows(),hands=([(316,350)],[(444,350)]))+drop(347,222,9,WBLUE)+R(512,359,80,59,8,PINK)+P('M 512 359 L 551 329 L 592 359',stroke=RED_D,w=7)
    if w=='angry':return g+person(shirt=RED,face='sad',brows=eyebrows(kind='angry'),hands=([(300,309)],[(460,309)]))+C(316,309,19,SKIN)+C(460,309,19,SKIN)+P('M 270 130 Q 242 100 268 79 M 491 130 Q 519 100 493 79',stroke='#d4cbc0',w=9)+L(543,181,563,171,RED,6)
    if w=='cry':return g+person(shirt=TEAL,face='cry',brows=eyebrows(),mouth=E(380,224,22,29,'#6b3325'))+drop(343,251,11,WBLUE)+drop(420,270,12,WBLUE)+drop(338,293,9,WBLUE)+drop(422,312,9,WBLUE)
    if w=='laugh':return g+person(shirt=YEL,face='open',eyes=shut(),hands=([(305,320),(348,329)],[(455,320),(412,329)]))+P('M 235 178 Q 217 196 235 215 M 526 178 Q 544 196 526 215',stroke=RED,w=6)
    if w=='smile':return g+person(shirt=PINK,eyes=shut(),mouth=P('M 356 218 Q 380 234 404 218',stroke=INK,w=6))+heart(536,160,21,PINK)
    if w=='tired':return g+R(294,365,178,18,7,WOOD)+person(y=435,pose='sit',shirt=BLUE,face='o',eyes=shut(380,213),hands=([(304,363)],[(463,363)]))+drop(432,186,13,WBLUE)+L(274,404,252,420,TEAL_L,5)
    if w=='sleepy':return g+person(shirt=TEAL,eyes=shut(),face='o',mouth=E(380,223,19,24,'#6b3325'),hands=([(312,340)],[(473,280),(405,236)]))+P('M 539 111 A 34 34 0 1 0 570 158 A 31 31 0 0 1 539 111 Z',YEL)
    if w=='hungry':return g+person(x=331,shirt=YEL,hands=([(255,310),(301,329)],[(408,310),(358,329)]))+bubble(540,157,E(540,155,44,30,WOOD_D)+L(564,165,581,181,WHITE,13)+C(585,185,10,WHITE))+P('M 295 356 Q 329 374 364 356',stroke=INK,w=4)
    if w=='thirsty':return g+person(x=327,shirt=RED,face='open')+bubble(548,164,R(521,131,54,71,9,BLUE)+R(527,151,42,45,5,WBLUE))+drop(405,201,10,WBLUE)
    if w=='scared':return g+R(486,100,59,335,14,WOOD)+person(shirt=BLUE,face='o',brows=eyebrows(),hands=([(303,286),(488,283)],[(461,264),(490,302)]))+P('M 250 206 L 237 229 L 250 249 L 237 273 M 573 217 L 585 237 L 573 257 L 585 277',stroke=TEAL,w=6)
    if w=='surprised':return g+person(shirt=YEL,arms='up',face='o',mouth=E(380,223,17,24,'#6b3325'))+L(274,93,262,70,RED,8)+L(380,79,380,49,RED,8)+L(480,93,497,72,RED,8)
    if w=='bored':return g+person(y=438,pose='sit',shirt=TEAL,eyes=shut(380,216),mouth=P('M 356 246 L 404 246',stroke=INK,w=6),hands=([(310,270),(330,232)],[(455,330)]))+R(240,345,296,23,10,WOOD)+R(262,368,24,70,7,WOOD_D)+R(491,368,24,70,7,WOOD_D)
    if w=='sick':return g+R(139,331,485,100,15,WOOD)+R(151,315,461,40,14,WHITE)+kid(x=318,y=379,s=1.1,pose='sleep',shirt=BLUE)+R(295,322,237,64,17,BLUE)+R(207,273,63,18,7,TEAL_L)+L(557,231,557,308,WHITE,16)+C(557,311,16,RED)+L(557,268,557,304,RED,5)
    if w=='love':return g+person(shirt=PINK,hands=([(301,292),(336,313)],[(459,292),(424,313)]))+heart(380,307,92,RED)
    if w=='like':return g+person(shirt=BLUE,hands=([(315,341)],[(468,288)]))+R(455,260,32,52,10,SKIN)+R(455,237,13,36,6,SKIN)+heart(535,180,35,RED)
    if w=='share':return g+person(x=249,y=438,s=.9,shirt=YEL,hands=([(191,340)],[(345,313)]))+person(x=511,y=438,s=.9,shirt=TEAL,hands=([(416,312)],[(569,340)]))+apple(355,307,.6)+apple(421,305,.6)+P('M 366 248 L 410 248 L 397 235 M 410 248 L 397 261',stroke=TEAL_D,w=6)
    if w=='help':return g+person(x=255,y=437,s=.95,shirt=BLUE,hands=([(193,342)],[(359,295),(424,317)]))+person(x=482,y=434,s=.75,pose='sit',shirt=RED,hands=([(410,314)],[(549,379)]))+heart(392,145,31,PINK)
    if w=='brave':return g+R(298,392,169,46,12,WOOD)+person(y=391,s=.95,shirt=TEAL,hands=([(301,285),(327,248)],[(459,285),(435,248)]))+R(529,118,9,301,4,WOOD_D)+PG([(538,124),(625,145),(538,175)],RED)+star5(210,202,27,YEL)
    if w=='proud':return g+person(shirt=YEL,hands=([(302,268),(318,254)],[(458,268),(441,254)]))+P('M 322 240 L 438 240 Q 436 318 380 330 Q 324 318 322 240 Z',YEL_D)+P('M 324 256 Q 266 243 287 293 Q 300 314 334 307 M 436 256 Q 494 243 473 293 Q 460 314 426 307',stroke=YEL,w=12)+R(371,325,18,38,6,YEL_D)+R(342,356,77,15,6,YEL)+star5(380,283,23,SUN_L)
    raise KeyError(w)


def arts():return {c['w']:drawing(c['w']) for c in GROUP_CARDS}
