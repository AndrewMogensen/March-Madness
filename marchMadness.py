import sys
import WinnerPredicting as winners

script, teamsFile = sys.argv
seeds = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
teams = open(teamsFile)

teamsInRoundOf64 = []
for index, team in enumerate(teams):
    teamsInRoundOf64.append([seeds[index % 16], team.rstrip()])

if index != 63:
    print "Incorrect number of teams in team listing file."
    quit()

finalFourSeedSum = 0
highestSweetSixteenSeed = 0
highestEliteEightSeed = 0
while finalFourSeedSum <= 6 or finalFourSeedSum >= 15 or highestSweetSixteenSeed < 10 or highestEliteEightSeed < 7:
    # while loop ensures some upsets occur. If not enough upsets, try again.
    teamsInRoundOf32 = winners.getTeamsInNextRoundFromCurrentTeams(teamsInRoundOf64)

    teamsInRoundOf16 = winners.getTeamsInNextRoundFromCurrentTeams(teamsInRoundOf32)

    teamsInRoundOf8 = winners.getTeamsInNextRoundFromCurrentTeams(teamsInRoundOf16)

    teamsInRoundOf4 = winners.getTeamsInNextRoundFromCurrentTeams(teamsInRoundOf8)

    teamsInRoundOf2 = winners.getTeamsInNextRoundFromCurrentTeams(teamsInRoundOf4)

    championTeam = winners.getTeamsInNextRoundFromCurrentTeams(teamsInRoundOf2)

    highestSweetSixteenSeed = max(teamsInRoundOf16[1][0], teamsInRoundOf16[2][0], teamsInRoundOf16[3][0], teamsInRoundOf16[4][0], teamsInRoundOf16[5][0], teamsInRoundOf16[6][0], teamsInRoundOf16[7][0], teamsInRoundOf16[8][0], teamsInRoundOf16[9][0], teamsInRoundOf16[10][0], teamsInRoundOf16[11][0], teamsInRoundOf16[12][0], teamsInRoundOf16[13][0], teamsInRoundOf16[14][0], teamsInRoundOf16[15][0], teamsInRoundOf16[0][0])
    highestEliteEightSeed = max(teamsInRoundOf8[0][0], teamsInRoundOf8[1][0], teamsInRoundOf8[2][0], teamsInRoundOf8[3][0], teamsInRoundOf8[4][0], teamsInRoundOf8[5][0], teamsInRoundOf8[6][0], teamsInRoundOf8[7][0])
    finalFourSeedSum = teamsInRoundOf4[0][0] + teamsInRoundOf4[1][0] + teamsInRoundOf4[2][0] + teamsInRoundOf4[3][0]

print "Second Round:"
print teamsInRoundOf32
print "Sweet Sixteen:"
print teamsInRoundOf16
print "Elite Eight:"
print teamsInRoundOf8
print "Final Four:"
print teamsInRoundOf4
print "National Championship:"
print teamsInRoundOf2
print "National Champion:"
print championTeam
