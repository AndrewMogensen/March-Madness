import numpy as np
import random
import sys


def shouldFirstTeamWinRoundOf64(seed):
    r = random.random()
    chance = [.999, .943548387, .838709677, 798387097, .645161290, .653225806, .612903226, .508064516]
    return r <= chance[seed - 1]


def shouldFirstTeamWinRoundOf32(seed1, seed2):
    r = random.random()
    chance = [.21572581, .15927419, .12701613, .11491935, .08266129, .08266129, .04435484, .02419355, .01008065, .04435484, .03629032, .04032258, .01209677, .00403226, .00201613, .0001]
    return r <= chance[seed1 - 1] / (chance[seed1 - 1] + chance[seed2 - 1])


def shouldFirstTeamWinRoundOf16(seed1, seed2):
    r = random.random()
    chance = [.34274194, .23387097, .12096774, .08064516, .03225806, .05241935, .03225806, .03225806, .008060452, .02822581, .02419355, .00403226, .0001, .00001, .000001]
    return r <= chance[seed1 - 1] / (chance[seed1 - 1] + chance[seed2 - 1])


def shouldFirstTeamWinRoundOf8(seed1, seed2):
    r = random.random()
    chance = [.48387097, .25, .12903226, .11290323, .05645161, .04838710, .02419355, .04838710, .01612903, .01, .02419355, .0001, .00001, .000001, .0000001]
    return r <= chance[seed1 - 1] / (chance[seed1 - 1] + chance[seed2 - 1])


def shouldFirstTeamWinRoundOf4(seed1, seed2):
    r = random.random()
    chance = [.56451613, .24193548, .16129032, .04838710, .04838710, .04838710, .01612903, .06451613, .001, .0001, .00001, .00001, .000001, .0000001, .00000001]
    return r <= chance[seed1 - 1] / (chance[seed1 - 1] + chance[seed2 - 1])


def shouldFirstTeamWinRoundOf2(seed1, seed2):
    r = random.random()
    chance = [.70967742, .16129032, .16129032, .03225806, .01, .06451613, .03225806, .03225806, .001, .001, .0001, .0001, .00001, .000001, .0000001]
    return r <= chance[seed1 - 1] / (chance[seed1 - 1] + chance[seed2 - 1])


def getTeamsInNextRoundFromCurrentTeams(teams):

    nextRoundTeams = []

    numberOfCurrentTeams = len(teams)
    numberOfGames = numberOfCurrentTeams / 2

    for i in range(numberOfGames):
        team1 = teams[2 * i]
        team1seed = team1[0]

        team2 = teams[2 * i + 1]
        team2seed = team2[0]

        if numberOfCurrentTeams == 64:
            shouldPickFirstTeam = shouldFirstTeamWinRoundOf64(team1seed)
        elif numberOfCurrentTeams == 32:
            shouldPickFirstTeam = shouldFirstTeamWinRoundOf32(team1seed, team2seed)
        elif numberOfCurrentTeams == 16:
            shouldPickFirstTeam = shouldFirstTeamWinRoundOf16(team1seed, team2seed)
        elif numberOfCurrentTeams == 8:
            shouldPickFirstTeam = shouldFirstTeamWinRoundOf8(team1seed, team2seed)
        elif numberOfCurrentTeams == 4:
            shouldPickFirstTeam = shouldFirstTeamWinRoundOf4(team1seed, team2seed)
        elif numberOfCurrentTeams == 2:
            shouldPickFirstTeam = shouldFirstTeamWinRoundOf2(team1seed, team2seed)
        else:
            print("ERROR, incorrect number of teams")
            return

        if shouldPickFirstTeam:
            nextRoundTeams.append(team1)
        else:
            nextRoundTeams.append(team2)

    return nextRoundTeams