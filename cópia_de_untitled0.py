# -*- coding: utf-8 -*-
"""Cópia de Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18JjclIqDlo8b3YpXz8HYYraSGvBvaQCU
"""

!pip install pulp

from pulp import *

problema1 = LpProblem('entregas',LpMinimize)

x15 = LpVariable('x15', lowBound = 0)
x18 = LpVariable('x18', lowBound = 0)
x19 = LpVariable('x19', lowBound = 0)
x110 = LpVariable('x110', lowBound = 0)
x111 = LpVariable('x111', lowBound = 0)
x124 = LpVariable('x124', lowBound = 0)
x125 = LpVariable('x125', lowBound = 0)
x126 = LpVariable('x126', lowBound = 0)
x127 = LpVariable('x127', lowBound = 0)
x128 = LpVariable('x128', lowBound = 0)
x129 = LpVariable('x129', lowBound = 0)
x130 = LpVariable('x130', lowBound = 0)
x131 = LpVariable('x131', lowBound = 0)
x132 = LpVariable('x132', lowBound = 0)
x133 = LpVariable('x133', lowBound = 0)
x134 = LpVariable('x134', lowBound = 0)
x135 = LpVariable('x135', lowBound = 0)
x136 = LpVariable('x136', lowBound = 0)
x137 = LpVariable('x137', lowBound = 0)
x138 = LpVariable('x138', lowBound = 0)
x139 = LpVariable('x139', lowBound = 0)
x140 = LpVariable('x140', lowBound = 0)
x141 = LpVariable('x141', lowBound = 0)
x142 = LpVariable('x142', lowBound = 0)
x143 = LpVariable('x143', lowBound = 0)
x147 = LpVariable('x147', lowBound = 0)
x148 = LpVariable('x148', lowBound = 0)
x149 = LpVariable('x149', lowBound = 0)
x150 = LpVariable('x150', lowBound = 0)
x151 = LpVariable('x151', lowBound = 0)
x21 = LpVariable('x21', lowBound = 0)
x22 = LpVariable('x22', lowBound = 0)
x23 = LpVariable('x23', lowBound = 0)
x24 = LpVariable('x24', lowBound = 0)
x25 = LpVariable('x25', lowBound = 0)
x26 = LpVariable('x26', lowBound = 0)
x27 = LpVariable('x27', lowBound = 0)
x28 = LpVariable('x28', lowBound = 0)
x29 = LpVariable('x29', lowBound = 0)
x210 = LpVariable('x210', lowBound = 0)
x211 = LpVariable('x211', lowBound = 0)
x212 = LpVariable('x212', lowBound = 0)
x213 = LpVariable('x213', lowBound = 0)
x214 = LpVariable('x214', lowBound = 0)
x215 = LpVariable('x215', lowBound = 0)
x216 = LpVariable('x216', lowBound = 0)
x217 = LpVariable('x217', lowBound = 0)
x218 = LpVariable('x218', lowBound = 0)
x219 = LpVariable('x219', lowBound = 0)
x220 = LpVariable('x220', lowBound = 0)
x221 = LpVariable('x221', lowBound = 0)
x222 = LpVariable('x222', lowBound = 0)
x223 = LpVariable('x223', lowBound = 0)
x224 = LpVariable('x224', lowBound = 0)
x225 = LpVariable('x225', lowBound = 0)
x226 = LpVariable('x226', lowBound = 0)
x227 = LpVariable('x227', lowBound = 0)
x228 = LpVariable('x228', lowBound = 0)
x229 = LpVariable('x229', lowBound = 0)
x230 = LpVariable('x230', lowBound = 0)
x231 = LpVariable('x231', lowBound = 0)
x232 = LpVariable('x232', lowBound = 0)
x233 = LpVariable('x233', lowBound = 0)
x234 = LpVariable('x234', lowBound = 0)
x235 = LpVariable('x235', lowBound = 0)
x239 = LpVariable('x239', lowBound = 0)
x240 = LpVariable('x240', lowBound = 0)
x241 = LpVariable('x241', lowBound = 0)
x242 = LpVariable('x242', lowBound = 0)
x243 = LpVariable('x243', lowBound = 0)
x244 = LpVariable('x244', lowBound = 0)
x245 = LpVariable('x245', lowBound = 0)
x246 = LpVariable('x246', lowBound = 0)
x247 = LpVariable('x247', lowBound = 0)
x248 = LpVariable('x248', lowBound = 0)
x249 = LpVariable('x249', lowBound = 0)
x250 = LpVariable('x250', lowBound = 0)
x251 = LpVariable('x251', lowBound = 0)
x31 = LpVariable('x31', lowBound = 0)
x32 = LpVariable('x32', lowBound = 0)
x33 = LpVariable('x33', lowBound = 0)
x34 = LpVariable('x34', lowBound = 0)
x35 = LpVariable('x35', lowBound = 0)
x36 = LpVariable('x36', lowBound = 0)
x37 = LpVariable('x37', lowBound = 0)
x38 = LpVariable('x38', lowBound = 0)
x39 = LpVariable('x39', lowBound = 0)
x310 = LpVariable('x310', lowBound = 0)
x311 = LpVariable('x311', lowBound = 0)
x319 = LpVariable('x319', lowBound = 0)
x320 = LpVariable('x320', lowBound = 0)
x321 = LpVariable('x321', lowBound = 0)
x322 = LpVariable('x322', lowBound = 0)
x323 = LpVariable('x323', lowBound = 0)
x324 = LpVariable('x324', lowBound = 0)
x325 = LpVariable('x325', lowBound = 0)
x326 = LpVariable('x326', lowBound = 0)
x327 = LpVariable('x327', lowBound = 0)
x328 = LpVariable('x328', lowBound = 0)
x329 = LpVariable('x329', lowBound = 0)
x330 = LpVariable('x330', lowBound = 0)
x331 = LpVariable('x331', lowBound = 0)
x332 = LpVariable('x332', lowBound = 0)
x333 = LpVariable('x333', lowBound = 0)
x334 = LpVariable('x334', lowBound = 0)
x335 = LpVariable('x335', lowBound = 0)
x336 = LpVariable('x336', lowBound = 0)
x337 = LpVariable('x337', lowBound = 0)
x338 = LpVariable('x338', lowBound = 0)
x344 = LpVariable('x344', lowBound = 0)
x345 = LpVariable('x345', lowBound = 0)
x346 = LpVariable('x346', lowBound = 0)
x347 = LpVariable('x347', lowBound = 0)
x348 = LpVariable('x348', lowBound = 0)
x349 = LpVariable('x349', lowBound = 0)
x350 = LpVariable('x350', lowBound = 0)
x351 = LpVariable('x351', lowBound = 0)

problema1 += 0.26*x15+0.26*x18+0.27*x19+0.30*x110+0.27*x111+0.29*x124+0.25*x125+0.30*x126+0.28*x127+0.31*x128+0.33*x129+0.44*x130+0.29*x131+0.35*x132+0.60*x133+0.27*x134+0.27*x135+0.48*x136+0.47*x137+0.46*x138+0.57*x139+0.61*x140+0.58*x141+0.57*x142+0.61*x143+0.69*x147+0.72*x148+0.61*x149+0.69*x150+0.64*x151+0.57*x21+0.51*x22+0.44*x23+0.47*x24+0.51*x25+0.56*x26+0.53*x27+0.56*x28+0.43*x29+0.72*x210+0.38*x211+0.80*x212+0.77*x213+0.72*x214+0.84*x215+0.85*x216+0.84*x217+0.84*x218+0.70*x219+0.74*x220+0.77*x221+0.70*x222+0.75*x223+0.72*x224+0.64*x225+0.70*x226+0.73*x227+0.73*x228+0.76*x229+0.76*x230+0.70*x231+0.69*x232+0.68*x233+0.69*x234+0.70*x235+0.88*x239+0.98*x240+0.92*x241+0.91*x242+0.99*x243+0.64*x244+0.64*x245+0.65*x246+0.28*x247+0.29*x248+0.30*x249+0.36*x250+0.42*x251+0.43*x31+0.38*x32+0.38*x33+0.41*x34+0.41*x35+0.38*x36+0.43*x37+0.37*x38+0.48*x39+0.29*x310+0.56*x311+0.29*x319+0.28*x320+0.28*x321+0.29*x322+0.25*x323+0.30*x324+0.27*x325+0.29*x326+0.21*x327+0.31*x328+0.27*x329+0.30*x330+0.28*x331+0.27*x332+0.28*x333+0.29*x334+0.30*x335+0.72*x336+0.71*x337+0.70*x338+0.48*x344+0.49*x345+0.48*x346+0.90*x347+0.96*x348+1.05*x349+1.02*x350+1.09*x351

problema1 += x15 + x18 + x19 + x110 + x111 + x124 + x125 + x126 + x127 + x128 + x129 + x130 + x131 + x132 + x133 + x134 + x135 + x136 + x137 + x138 + x139 + x140 + x141 + x141 + x142 + x143 + x147 + x148 + x149 + x150 + x151 <= 90000000
problema1 += x21 + x22 + x23 + x24 + x25 + x26 + x27 + x28 + x29 + x210 + x211 + x212 + x213 + x214 + x215 + x216 + x217 + x218 + x219 + x220 + x221 + x222 + x223 + x224 + x225 + x226 + x227 + x228 + x229 + x230 + x231 + x232 + x233 + x234 + x235 + x239 + x24 + x241 + x242 + x243 + x244 + x245 + x246 + x247 + x248 + x249 + x250 + x251 <= 56000000
problema1 += x31 + x32 + x33 + x34 + x35 + x36 + x37 + x38 + x39 + x310 + x311 + x319 + x320 + x321 + x322 + x323 + x324 + x325 + x326 + x327 + x328 + x329 + x330 + x331 + x332 + x333 + x334 + x335 + x336 + x337 + x338 + x344 + x345 + x346 + x347 + x348 + x34 + x350 + x351 <= 90000000
problema1 += x21 + x31 == 2797800
problema1 += x22 + x32 == 1836600
problema1 += x23 + x33 == 1274700
problema1 += x24 + x34 == 2439900
problema1 += x15 + x25 + x35 == 5714100
problema1 += x26 + x36 == 2725500
problema1 += x27 + x37 == 2887500
problema1 += x18 + x28 + x38 == 3846300
problema1 += x19 + x29 + x39 == 7242300
problema1 += x110 + x210 + x310 == 4028400
problema1 += x111 + x211 + x311 == 6508200
problema1 += x212 == 1214700
problema1 += x213 == 9900
problema1 += x214 == 37200
problema1 += x215 == 1094100
problema1 += x216 == 939300
problema1 += x217 == 19200
problema1 += x218 == 1474200
problema1 += x219 + x319 == 2050200
problema1 += x220 + x320 == 26400
problema1 += x221 + x321 == 24000
problema1 += x222 + x322 == 2151000
problema1 += x223 + x323 == 18900
problema1 += x124 + x224 + x324 == 1571700
problema1 += x125 + x225 + x325 == 35100
problema1 += x126 + x226 + x326 == 4980600
problema1 += x127 + x227 + x327 == 1449300
problema1 += x128 + x228 + x328 == 5429400
problema1 += x129 + x229 + x329 == 1661400
problema1 += x130 + x230 + x330 == 1392300
problema1 += x131 + x231 + x331 == 5148000
problema1 += x132 + x232 + x332 == 59700
problema1 += x133 + x233 + x333 == 24900
problema1 += x134 + x234 + x334 == 3387900
problema1 += x135 + x335 == 3957000
problema1 += x136 + x336 == 1605300
problema1 += x137 + x337 == 2821500
problema1 += x138 + x338 == 2232600
problema1 += x139 + x239 == 41400
problema1 += x140 + x240 == 3410700
problema1 += x141 + x241 == 2381100
problema1 += x142 + x242 == 2795100
problema1 += x143 + x243 == 3715200
problema1 += x244 + x344 == 2419500
problema1 += x245 + x345 == 2129100
problema1 += x246 + x346 == 38100
problema1 += x147 + x247 + x347 == 4104300
problema1 += x148 + x248 + x348 == 3446400
problema1 += x149 + x249 + x349 == 37200
problema1 += x150 + x250 + x350 == 3924900
problema1 += x151 + x251 + x351 == 51300

problema1

problema1.solve()

for v in problema1.variables():
  print(v.name, "=",v.varValue)

print('entregas=',value(problema1.objective))

