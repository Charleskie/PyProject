import sys
sys.path.append(r'py/sortAlgorithm')
from py.sortAlgorithm.Bubble import *
from py.draw_algorithm.draw_normal_distribution import draw
from py.sortAlgorithm.insertSort import *
L = [2, 3, 7, 5, 6]
# Bubble(L)
insertSort(L)
print(L)
draw(L)

