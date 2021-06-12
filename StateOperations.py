import math
from variables import *


class State:

    def __init__(self, stones, mancalas, turn):
        self.stones = stones
        self.mancalas = mancalas
        self.turn = turn

    def __eq__(self, other):
        return self.stones == other.stones and self.mancalas == other.mancalas and self.turn == other.turn

    def isFinal(self):
        return all([x == 0 for x in self.stones[0]]) or all([x == 0 for x in self.stones[1]])


def getInitialState():
    stones1 = [initialNumberOfStones for _ in range(0, numberOfHoles)]
    stones2 = [initialNumberOfStones for _ in range(0, numberOfHoles)]
    mancalas = [0, 0]
    return State([stones1, stones2], mancalas, turnHuman)


def getFinalScores(state: State):
    return [state.mancalas[0] + sum(state.stones[0]), state.mancalas[1] + sum(state.stones[1])]


def displayState(state: State):

    mancalaFormat = '{:10s}'
    stoneFormat = '{:5s}'

    print(f"Player's {state.turn} turn\n")

    print('Player 2' + ('*: ' if state.turn == 2 else ' : '), end='')
    print(mancalaFormat.format(str(state.mancalas[1])), end='')
    for i in range(0, len(state.stones[1])):
        print(stoneFormat.format(str(state.stones[1][i])), end='')
    print('')

    print('Player 1' + ('*: ' if state.turn == 1 else ' : '), end='')
    print('{0: ^10}'.format(''), end='')
    for i in range(0, len(state.stones[0])):
        print(stoneFormat.format(str(state.stones[0][i])), end='')
    print('{0: ^10}'.format(str(state.mancalas[0])), end='')

    print('\n')


def evaluateState(state: State, newState: State):

    if newState.isFinal():
        scores = getFinalScores(newState)
        if scores[1] > scores[0]:
            return math.inf
        elif scores[1] < scores[0]:
            return -math.inf

    if state.turn == turnAI:
        score = newState.mancalas[1] - state.mancalas[1]
        if state.turn == newState.turn:
            score *= 2
        return score
    else:
        score = state.mancalas[0] - newState.mancalas[0]
        if state.turn == newState.turn:
            score *= 2
        return score

if __name__ == '__main__':
    displayState(getInitialState())
