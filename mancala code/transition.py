from StateOperations import State
from variables import numberOfHoles


class Transition:

    def __init__(self, hole):
        self.hole = hole


def makeTransition(state: State, transition: Transition):
    newStones1 = list(state.stones[0])
    newStones2 = list(state.stones[1])
    newMancalas = list(state.mancalas)
    stonesToMove = state.stones[state.turn - 1][transition.hole - 1]
    newTurn = state.turn % 2 + 1

    if state.turn == 1:
        # Player 1 is moving
        newStones1[transition.hole - 1] = 0

        # Initially, I start from transition.hole on my board
        i = transition.hole
        while stonesToMove > 0:
            # Put on player 1's board
            while i < numberOfHoles and stonesToMove > 0:
                newStones1[i] += 1
                stonesToMove -= 1
                i += 1

            # put on player 1's mancala
            if stonesToMove > 0:
                newMancalas[0] += 1
                stonesToMove -= 1
                if stonesToMove == 0:
                    # If, when placing the last stone, I place it in my Mancala, I take another turn
                    # so turn for the new state will be 1
                    newTurn = 1
                    break
            elif stonesToMove == 0 and newStones1[i - 1] == 1:
                # If, when placing the last stone, I place it on my board on an empty space, I capture the stones from the opposite side
                newMancalas[0] += newStones2[i - 1] + 1
                newStones1[i - 1] = 0
                newStones2[i - 1] = 0

            # put on player 2's board
            i = numberOfHoles - 1
            while i >= 0 and stonesToMove > 0:
                newStones2[i] += 1
                stonesToMove -= 1
                i -= 1

            # I have to go counter-clock wise, so I'm starting with the position 0 on Player 1's board
            i = 0
    else:
        # Player 2 is moving
        newStones2[transition.hole - 1] = 0

        # Initially, I start from transition.hole on my board
        i = transition.hole - 2
        while stonesToMove > 0:
            # Put on player 2's board
            while i >= 0 and stonesToMove > 0:
                newStones2[i] += 1
                stonesToMove -= 1
                i -= 1

            # put on player 2's mancala
            if stonesToMove > 0:
                newMancalas[1] += 1
                stonesToMove -= 1
                if stonesToMove == 0:
                    # If, when placing the last stone, I place it in my Mancala, I take another turn
                    # so turn for the new state will be 2
                    newTurn = 2
                    break
            elif stonesToMove == 0 and newStones2[i + 1] == 1:
                # If, when placing the last stone, I place it on my board on an empty space, I capture the stones from the opposite side
                newMancalas[1] += newStones1[i + 1] + 1
                newStones2[i + 1] = 0
                newStones1[i + 1] = 0

            # put on player 1's board
            i = 0
            while i < numberOfHoles and stonesToMove > 0:
                newStones1[i] += 1
                stonesToMove -= 1
                i += 1

            # I have to go counter-clock wise, so I'm starting with the last position on Player 2's board
            i = numberOfHoles - 1

    newState = State([newStones1, newStones2], newMancalas, newTurn)
    return newState


def isTransitionValid(state: State, transition: Transition):
    if transition.hole < 1 or transition.hole > numberOfHoles:
        return False
    if state.stones[state.turn - 1][transition.hole - 1] == 0:
        return False
    return True
