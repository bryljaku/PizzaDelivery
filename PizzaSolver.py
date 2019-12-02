from PizzaDelivery import *


def pathMerge(pathsList):
    for i in range(0, len(pathsList) - 1):
        if pathsList[i][-1] == pathsList[i+1][0]:  # in order not to duplicate vertices
            pathsList[i+1].pop(0)
    flatList = []
    for sublist in pathsList:
        for element in sublist:
            flatList.append(element)
    return flatList


def solvePizzaProblem(graph, start, deliveryList):
    ret = pizzaDelivery(graph, start, deliveryList)
    return pathMerge(ret)