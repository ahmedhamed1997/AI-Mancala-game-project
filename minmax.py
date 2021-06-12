import math
import random
from StateOperations import State, evaluateState
from transition import Transition, makeTransition, isTransitionValid
from variables import numberOfHoles, turnAI, maxMiniMaxDepth


def getBestAIDecision(currentState: State):
    scores = []
    children, transitions = buildStateChildren(currentState)
    for child in children:
        scores.append(minimax(child, maxMiniMaxDepth,
                              True, -math.inf, math.inf))
    maxScoreIndex = scores.index(max(scores))
    return transitions[maxScoreIndex].hole


def buildStateChildren(currentState: State):
    transitions = [Transition(i + 1) for i in range(0, numberOfHoles)
                   if isTransitionValid(currentState, Transition(i + 1))]
    possibleStates = [makeTransition(
        currentState, transition) for transition in transitions]
    return possibleStates, transitions


def minimax(currentState: State, limit, maximixing, alpha, beta):
    children, _ = buildStateChildren(currentState)

    if maximixing:
        value = -math.inf
        for child in children:
            if limit == 1:
                childValue = evaluateState(currentState, child)
            else:
                childValue = minimax(child, limit - 1, False, alpha, beta)
            value = max(value, childValue)
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = math.inf
        for child in children:
            if limit == 1:
                childValue = evaluateState(currentState, child)
            else:
                childValue = minimax(child, limit - 1, True, alpha, beta)
            value = min(value, childValue)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value
