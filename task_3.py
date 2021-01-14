from random import randint


class TestArray:
    def __init__(self, lenght, array):
        self.length = lenght
        self.array = array

    def creating_array(self):
        self.array = [randint(-1000, 1000) for self.i in range(self.length)]
        return self.array

    def find_first_max(self):
        self.first_max = 0
        for i in range(self.length):
            if self.array[i] > self.first_max:
                self.first_max = self.array[i]
        return self.first_max

    def find_second_max(self):
        self.second_max = 0
        self.tempo = 0
        for i in range(self.length):
            if self.array[i] > self.tempo:
                self.tempo = self.array[i]
        for i in range(self.length):
            if self.array[i] > self.second_max and self.array[i] != self.tempo:
                self.second_max = self.array[i]
        return self.second_max

