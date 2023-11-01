from collections import deque
from math import floor

class hashtable:

    def __init__(self, size):
        self.__items = [deque() for _ in range(size)]
        self.__size = size
        self.__hashmod = 0.367843

    def hash(self, key):
        character_sum = 0
        # multiplication method hashing function based on the sum of character ascii values in the symbol (if string)
        if isinstance(key, str):
            for character in key:
                character_sum += ord(character) - ord('0')
            return floor(self.__size * (character_sum * self.__hashmod % 1))
        else:
            return floor(self.__size * (key * self.__hashmod % 1))

    def add(self, key):
        if self.contains(key):
            return self.getPosition(key)
        self.__items[self.hash(key)].append(key)
        return self.get_position(key)

    def contains(self, key):
        return key in self.__items[self.hash(key)]

    def remove(self, key):
        self.__items[self.hash(key)].remove(key)

    def __str__(self) -> str:
        result = "table: \n"
        for i in range(self.__size):
            result = result + str(i) + " -> " + str(self.__items[i]) + "\n"
        return result

    def get_position(self, key):
        list_position = self.hash(key)
        list_index = 0
        for item in self.__items[list_position]:
            if item != key:
                list_index += 1
            else:
                break
        return (list_position, list_index)