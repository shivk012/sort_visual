import random
from typing import List, Tuple
import time


class Algorithm:
    def __init__(self, name, array) -> None:
        if array:
            self.array = array
        else:
            self.array = random.sample(range(512), 512)
        self.steps = []

    def run(self) -> Tuple[List, float]:
        """Run the sorter and time it"""
        self.start = time.time()
        self.algorithm()
        duration = time.time() - self.start

        return self.array, duration, self.steps



class BubbleSort(Algorithm):
    def __init__(self, array) -> None:
        super().__init__("BubbleSort", array)

    def algorithm(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j] , self.array[j+1] = self.array[j+1], self.array[j]
                    self.steps.append([j, j+1])

print(BubbleSort([1,2,4,3]).run())