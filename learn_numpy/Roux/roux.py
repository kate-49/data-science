import numpy as np

class Roux:
    def __init__(self, number):
        self.number = number

    def run(self):
        if self.number % 2 == 0:
            length = self.number / 2
        else:
            length = (self.number + 1) / 2
        array = np.arange(start=int(length), stop=0, step=-1)
        array = (np.power(array, 2))

        if self.number % 2 == 0:
            array = np.insert(array, 0, 0, axis=0)
            index = 2
        else:
            index = 1

        for x in array:
            current_length = array.size
            if index < current_length:
                array = np.insert(array, index, 0, axis=0)
                index += 2

        print(array)
        return np.array(array)