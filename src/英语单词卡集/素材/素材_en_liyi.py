#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""礼貌10卡：同伴互动、动作与情境配合；气泡里只有图形。"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from 动作组件_en import *
GROUP_CARDS=[{'w':w,'cn':cn} for w,cn in [('hello','你好'),('hi','嗨'),('bye','再见'),('yes','是/对'),('no','不/不是'),('OK','好/行'),('please','请'),('welcome','欢迎'),('thank you','谢谢'),('sorry','对不起')]]


def wave(x,shirt,s=1):
    y=435;sho=y-168*s;hc=sho-70*s
    return person(x=x,y=y,s=s,shirt=shirt,hands=([(x-66*s,sho+78*s)],[(x+94*s,sho-20*s),(x+100*s,hc-12*s)]))+hand(x+100*s,hc-42*s,0,.32*s)


def drawing(w):
    g=ground()
    if w=='hello':return g+wave(356,TEAL)+flower5(566,403,26,PINK)+L(566,420,566,444,GREEN,6)+P('M 512 124 Q 544 150 512 176',stroke=YEL,w=7)
    if w=='hi':return g+person(x=276,y=436,s=.92,shirt=YEL,hands=([(210,343)],[(368,213),(380,188)]))+person(x=485,y=436,s=.92,shirt=BLUE,hands=([(393,213),(380,188)],[(549,343)]))+star5(380,150,24,RED)
    if w=='bye':return g+R(282,263,100,99,22,YEL)+R(265,264,25,83,10,YEL_D)+wave(352,RED)+P('M 515 390 L 618 390 M 599 373 L 619 390 L 599 407',stroke=TEAL,w=7)+R(560,343,53,31,7,WOOD)
    if w=='yes':return g+person(shirt=BLUE,hands=([(284,282)],[(477,282)]))+R(270,257,31,47,10,SKIN)+R(269,236,13,34,6,SKIN)+R(463,257,31,47,10,SKIN)+R(463,236,13,34,6,SKIN)+P('M 519 126 Q 551 151 520 177 M 520 177 L 520 154 M 520 177 L 541 174',stroke=TEAL,w=7)+check(216,161,40)
    if w=='no':return g+person(shirt=RED,hands=([(289,266)],[(474,266)]))+hand(286,251,-14,.4)+hand(478,251,14,.4)+P('M 292 105 Q 380 66 469 105 M 292 105 L 312 86 M 292 105 L 319 112 M 469 105 L 447 85 M 469 105 L 443 111',stroke=TEAL,w=6)
    if w=='OK':return g+person(shirt=YEL,hands=([(312,340)],[(480,240)]))+E(486,207,27,24,SKIN)+E(486,207,13,11,PAGE)+R(486,157,11,35,5,SKIN)+R(505,168,11,32,5,SKIN)+R(519,182,10,26,5,SKIN)+check(239,194,44)
    if w=='please':return g+person(x=287,y=436,s=.95,shirt=TEAL,hands=([(220,322),(353,323)],[(367,303),(421,323)]))+R(350,295,92,54,10,WOOD_L)+apple(397,278,.43)+person(x=549,y=437,s=.72,shirt=PINK)
    if w=='welcome':return g+R(114,117,184,323,8,WOOD_D)+R(129,133,152,305,5,'#f8e3ac')+PG([(129,133),(204,175),(204,438),(129,438)],WOOD)+C(188,302,8,YEL)+person(x=419,y=438,s=.96,shirt=YEL,hands=([(321,302)],[(517,302)]))+person(x=623,y=438,s=.65,shirt=BLUE)
    if w=='thank you':return g+person(x=260,y=438,s=.91,shirt=BLUE,hands=([(200,340)],[(356,308)]))+person(x=500,y=438,s=.91,shirt=RED,hands=([(399,306)],[(566,300),(438,322)]))+apple(384,286,.55)+heart(488,116,28,PINK)
    if w=='sorry':return g+person(x=314,y=438,s=.98,shirt=TEAL,face='sad',arms='clap')+R(499,365,109,66,13,RED)+C(516,439,17,INK)+C(599,434,17,INK)+C(650,438,18,INK)+L(615,421,640,420,WOOD_D,6)+bubble(554,166,heart(554,165,42,PINK))
    raise KeyError(w)


def arts():return {c['w']:drawing(c['w']) for c in GROUP_CARDS}
