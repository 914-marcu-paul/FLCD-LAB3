from hashtable import hashtable


class symtable:

    def __init__(self, size) -> None:
        self.__ht = hashtable(size)

    def __str__(self) -> str:
        return str(self.__ht)

    def add(self, key):
        return self.__ht.add(key)

    def contains(self, key):
        return self.__ht.contains(key)

    def remove(self, key):
        self.__ht.remove(key)

    def get_position(self, key):
        return self.__ht.get_position(key)