"""
author: ayelet.avraham@mail.huji.ac.il
"""

class HashMap:

    def __init__(self, size):
        """
        Constructor.
        """
        self.size = size
        self.hashTable = self.createBuckets()

    def createBuckets(self):
        res = []
        for i in range(self.size):
            res.append([])
        return res

    def insert(self, key, val):
        hashedKey = hash(key) % self.size # get the index from the key using hash function.
        self.hashTable[hashedKey] = val

    def get(self, key):
        hasedKey = hash(key) % self.size
