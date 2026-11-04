#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""形容对比20卡：同图保留参照物，让大小长短轻重看得出来。"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from 动作组件_en import *
GROUP_CARDS=[{'w':w,'cn':cn} for w,cn in [('big','大的'),('small','小的'),('long','长的'),('short','短的'),('tall','高的'),('high','高的（位置）'),('fat','胖的'),('thin','瘦的'),('heavy','重的'),('light','轻的'),('fast','快的'),('slow','慢的'),('hot','热的'),('cold','冷的'),('warm','温暖的'),('cool','凉爽的'),('new','新的'),('old','旧的'),('soft','软的'),('hard','硬的')]]


def elephant(x,y,s=1):
    g=E(0,0,160,93,'#a7b3bc')+C(-117,-44,68,'#a7b3bc')+E(-84,-35,49,67,'#c2ccd3')
    for xx in (-105,-51,61,110):g+=R(xx-15,52,31,83,10,'#94a1ac')
    g+=P('M -167 -46 Q -217 91 -165 100 Q -138 100 -139 65',stroke='#a7b3bc',w=36)+C(-144,-58,6,INK)+C(-146,-60,2,WHITE)
    return f'<g transform="translate({x} {y}) scale({s})">{g}</g>'


def mouse(x,y,s=1):
    g=E(0,0,60,37,'#acbac5')+C(-44,-21,31,'#acbac5')+C(-48,-56,24,'#acbac5')+C(-48,-56,15,PINK)+C(-59,-28,4,INK)+C(-75,-14,5,INK)+P('M 55 0 Q 102 -5 90 -49',stroke=PINK,w=6)+E(-21,31,17,8,'#94a1ac')+E(35,31,17,8,'#94a1ac')
    return f'<g transform="translate({x} {y}) scale({s})">{g}</g>'


def cat(x,y,s=1,body=95):
    g=E(0,0,body,95,YEL)+C(-body*.55,-82,49,YEL)+PG([(-body*.55-42,-104),(-body*.55-39,-151),(-body*.55-9,-119)],YEL)+PG([(-body*.55+8,-122),(-body*.55+42,-149),(-body*.55+42,-98)],YEL)
    g+=C(-body*.55-19,-85,6,INK)+C(-body*.55+19,-85,6,INK)+C(-body*.55,-65,5,INK)+P(f'M {body-8} 32 Q {body+97} 66 {body+59} -55',stroke=YEL_D,w=22)
    return f'<g transform="translate({x} {y}) scale({s})">{g}</g>'


def plush(x,y,worn=False):
    g=C(x-62,y-83,33,WOOD_D)+C(x+62,y-83,33,WOOD_D)+E(x,y+79,88,99,WOOD)+C(x,y-25,84,WOOD)+E(x,y+77,54,64,WOOD_L)+C(x-28,y-41,9,INK)+C(x+28,y-41,9,INK)+E(x,y-12,29,23,WOOD_L)+C(x,y-20,11,INK)+E(x-58,y+157,40,24,WOOD_D)+E(x+58,y+157,40,24,WOOD_D)
    if worn:g+=R(x-20,y+44,43,43,5,TEAL_L)+L(x-15,y+47,x+15,y+82,INK,3)+P(f'M {x-64} {y-110} L {x-40} {y-91}',stroke=PAGE,w=32)+L(x+48,y+105,x+64,y+121,INK,3)
    return g


def drawing(w):
    g=ground()
    if w=='big':return g+elephant(352,270,1.15)+mouse(641,405,.5)
    if w=='small':return g+E(517,315,135,109,BLUE)+mouse(271,392,.76)+E(195,406,20,12,WOOD_L)+L(180,406,210,406,WOOD_D,2)
    if w=='long':
        for i in range(4):
            xx=95+i*151;g+=R(xx,287,137,101,16,TEAL if i%2 else BLUE)+R(xx+14,305,43,35,6,WHITE)+R(xx+78,305,43,35,6,WHITE)+C(xx+30,401,23,INK)+C(xx+106,401,23,INK)
        return g+L(90,444,675,444,WOOD,8)
    if w=='short':return g+E(379,312,200,69,WOOD)+C(209,266,63,WOOD)+E(189,284,51,33,WOOD_L)+E(230,232,22,51,WOOD_D)+C(191,256,8,INK)+R(240,351,29,74,10,WOOD_D)+R(469,351,29,74,10,WOOD_D)+P('M 555 294 Q 610 253 604 221',stroke=WOOD,w=20)
    if w=='tall':return g+R(203,159,128,275,8,BLUE)+PG([(183,159),(267,83),(350,159)],RED)+R(411,322,147,112,8,TEAL)+PG([(399,322),(486,267),(570,322)],YEL)+R(246,300,43,133,5,WHITE)+L(130,143,130,431,TEAL_D,6)+PG([(130,122),(117,146),(143,146)],TEAL_D)
    if w=='high':return g+cloud_p(267,323,1.45,'#dfebed')+PG([(517,83),(577,149),(517,211),(458,149)],RED)+L(517,210,443,411,WOOD_D,3)+P('M 517 210 Q 612 218 589 291',stroke=TEAL,w=5)+person(x=405,y=439,s=.44,shirt=YEL)
    if w=='fat':return g+cat(347,331,1.05,145)+E(361,348,81,65,SUN_L,.5)+L(169,438,505,438,WOOD_L,4)
    if w=='thin':return g+L(364,296,338,429,YEL_D,9)+L(399,295,424,429,YEL_D,9)+E(381,247,39,76,WHITE)+P('M 384 202 Q 394 122 437 148',stroke=WHITE,w=28)+C(441,148,24,WHITE)+C(448,143,5,INK)+PG([(462,146),(527,151),(462,160)],YEL)+E(373,268,25,45,'#d9dfdd')
    if w=='heavy':return g+person(x=293,shirt=BLUE,face='sad',hands=([(200,210),(231,138)],[(386,210),(389,138)]))+R(141,61,431,69,32,WOOD_D)+E(571,95,28,35,WOOD_L)+P('M 520 274 L 520 381 M 501 360 L 520 383 L 540 360',stroke=RED,w=8)+drop(331,152,11,WBLUE)
    if w=='light':return g+P('M 280 371 Q 298 128 531 139 Q 530 322 280 371 Z',WHITE)+P('M 280 371 L 482 179',stroke='#c1d4d5',w=7)+P('M 341 308 L 347 225 M 375 282 L 441 284 M 404 251 L 412 184',stroke='#dce8e7',w=6)+P('M 212 397 Q 165 367 205 335 M 528 371 Q 568 339 545 301',stroke=TEAL_L,w=6)
    if w=='fast':return g+E(396,288,133,55,YEL)+C(258,267,46,YEL)+E(233,280,37,23,YEL)+C(248,256,6,INK)+P('M 311 315 L 242 404 M 330 317 L 398 378 M 462 314 L 526 395 M 475 286 Q 611 214 628 263',stroke=YEL,w=21)+''.join(C(x,y,7,INK) for x,y in [(340,272),(378,296),(412,264),(449,293),(482,280)])+motion(660,250,-1,TEAL)
    if w=='slow':return g+E(370,405,163,32,TEAL_L)+C(374,310,105,WOOD)+P('M 374 310 C 323 249 278 339 347 361 C 430 387 477 268 381 227',stroke=WOOD_D,w=9)+P('M 471 404 L 528 302 M 508 403 L 562 322',stroke=TEAL_L,w=16)+C(530,300,11,INK)+C(562,322,11,INK)
    if w=='hot':return g+bowl(380,363,123,False)+P('M 308 295 Q 337 260 311 219 M 378 285 Q 406 248 379 204 M 448 294 Q 476 256 449 217',stroke=RED,w=10)+C(581,137,49,SUN)
    if w=='cold':return g+C(380,348,95,WHITE)+C(380,227,66,WHITE)+R(319,157,122,26,8,BLUE)+R(337,110,88,52,12,BLUE)+R(322,268,115,30,10,RED)+R(388,284,31,74,8,RED)+C(358,217,7,INK)+C(400,217,7,INK)+PG([(374,232),(426,241),(373,247)],YEL)+star5(194,184,25,WBLUE)+star5(573,271,22,WBLUE)
    if w=='warm':return g+person(shirt=RED,hands=([(303,287),(350,294)],[(459,287),(413,294)]))+R(337,265,88,87,17,WOOD)+P('M 420 283 Q 468 293 422 327',stroke=WOOD,w=13)+P('M 363 245 Q 381 221 364 202 M 398 243 Q 415 218 399 199',stroke=YEL,w=5)+heart(555,174,29,PINK)
    if w=='cool':return g+tree_round(217,440,1.1)+person(x=491,y=439,s=.85,shirt=TEAL,hands=([(431,337)],[(565,295)]))+PG([(558,299),(533,219),(620,252)],YEL)+E(617,406,63,29,RED)+P('M 553 406 Q 617 468 681 406',stroke=GREEN,w=10)+P('M 520 161 Q 590 139 635 164',stroke=TEAL_L,w=7)
    if w=='new':return g+R(236,227,288,198,18,TEAL)+R(224,210,312,45,13,TEAL_D)+R(358,211,44,214,7,YEL)+P('M 380 208 C 249 201 279 119 342 154 L 380 194 C 459 89 523 181 380 208 Z',YEL)+star5(574,167,36,YEL)+star5(195,256,20,RED)
    if w=='old':return g+plush(380,239,True)+P('M 535 408 L 555 395 M 549 426 L 568 416',stroke=WOOD_D,w=4)
    if w=='soft':return g+R(213,229,335,181,57,PINK)+P('M 232 261 Q 380 294 526 258',stroke='#ef927c',w=7)+E(381,246,101,31,'#f9c3b0')+L(379,180,379,244,TEAL,9)+PG([(379,263),(363,238),(395,238)],TEAL)+P('M 570 213 Q 582 144 628 143 Q 629 198 570 213 Z',WHITE)
    if w=='hard':return g+P('M 226 402 L 204 313 L 283 216 L 429 194 L 543 306 L 518 416 Z','#aeb8c0')+PG([(283,216),(429,194),(543,306),(349,296)],'#c9d1d5')+L(391,143,391,215,TEAL,9)+PG([(391,237),(375,212),(407,212)],TEAL)+star5(184,276,20,YEL)
    raise KeyError(w)


def arts():return {c['w']:drawing(c['w']) for c in GROUP_CARDS}
