import numpy as np
import random
import sys

def winner64(seed):
	r = random.random()
	chance = [.999, .943548387, .838709677, 798387097, .645161290, .653225806, .612903226, .508064516]
	return r <= chance[seed - 1]

def winner32(seed1, seed2):
	r = random.random()
	chance = [.21572581, .15927419, .12701613, .11491935, .08266129, .08266129, .04435484, .02419355, .01008065, .04435484, .03629032, .04032258, .01209677, .00403226, .00201613, .0001]
	return r <= chance[seed1 - 1] / (chance[seed1 - 1] + chance[seed2 - 1])

def winner16(seed1, seed2):
	r = random.random()
	chance = [.34274194, .23387097, .12096774, .08064516, .03225806, .05241935, .03225806, .03225806, .008060452, .02822581, .02419355, .00403226, .0001, .00001, .000001]
	return r <= chance[seed1 - 1] / (chance[seed1 - 1] + chance[seed2 - 1])

def winner8(seed1, seed2):
	r = random.random()
	chance = [.48387097, .25, .12903226, .11290323, .05645161, .04838710, .02419355, .04838710, .01612903, .01, .02419355, .0001, .00001, .000001, .0000001]
	return r <= chance[seed1 - 1] / (chance[seed1 - 1] + chance[seed2 - 1])

def winner4(seed1, seed2):
	r = random.random()
	chance = [.56451613, .24193548, .16129032, .04838710, .04838710, .04838710, .01612903, .06451613, .001, .0001, .00001, .00001, .000001, .0000001, .00000001]
	return r <= chance[seed1 - 1] / (chance[seed1 - 1] + chance[seed2 - 1])

def winner2(seed1, seed2):
	r = random.random()
	chance = [.70967742, .16129032, .16129032, .03225806, .01, .06451613, .03225806, .03225806, .001, .001, .0001, .0001, .00001, .000001, .0000001]
	return r <= chance[seed1 - 1] / (chance[seed1 - 1] + chance[seed2 - 1])

script, teams = sys.argv
seeds = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
f = open(teams)

i = 0
r64 = []
for line in f:
	r64.append([seeds[i % 16], line.rstrip()])
	i += 1


finalFourSum = 0
highestSweetSixteen = 0
highestEliteEight = 0
while finalFourSum <= 6 or finalFourSum >= 15 or highestSweetSixteen < 10 or highestEliteEight < 7:
	r32 = []
	for x in range(32):
		pickFirst = winner64(r64[2*x][0])
		if pickFirst:
			r32.append(r64[2*x])
		else:
			r32.append(r64[2*x + 1])

	r16 = []
	for x in range(16):
		pickFirst = winner32(r32[2*x][0], r32[2*x+1][0])
		if pickFirst:
			r16.append(r32[2*x])
		else:
			r16.append(r32[2*x + 1])
	
	r8 = []
	for x in range(8):
		pickFirst = winner16(r16[2*x][0], r16[2*x+1][0])
		if pickFirst:
			r8.append(r16[2*x])
		else:
			r8.append(r16[2*x + 1])

	r4 = []
	for x in range(4):
		pickFirst = winner8(r8[2*x][0], r8[2*x+1][0])
		if pickFirst:
			r4.append(r8[2*x])
		else:
			r4.append(r8[2*x + 1])

	r2 = []
	for x in range(2):
		pickFirst = winner4(r4[2*x][0], r4[2*x+1][0])
		if pickFirst:
			r2.append(r4[2*x])
		else:
			r2.append(r4[2*x + 1])

	r1 = []
	pickFirst = winner2(r2[0][0], r2[1][0])
	if pickFirst:
		r1.append(r2[0])
	else:
		r1.append(r2[1])
	
	highestSweetSixteen = max(r16[1][0], r16[2][0], r16[3][0], r16[4][0], r16[5][0], r16[6][0], r16[7][0], r16[8][0], r16[9][0], r16[10][0], r16[11][0], r16[12][0], r16[13][0], r16[14][0], r16[15][0], r16[0][0])
	highestEliteEight = max(r8[0][0], r8[1][0], r8[2][0], r8[3][0], r8[4][0], r8[5][0], r8[6][0], r8[7][0])
	finalFourSum = r4[0][0] + r4[1][0] + r4[2][0] + r4[3][0]

print "Second Round:"
print r32
print "Sweet Sixteen:"
print r16
print "Elite Eight:"
print r8
print "Final Four:"
print r4
print "National Championship:"
print r2
print "National Champion:"
print r1
