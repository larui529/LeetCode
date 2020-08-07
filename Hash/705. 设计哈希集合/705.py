class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket_size = 769
        self.buckets = Buckets()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket_index = self._hash(key)
        self.buckets[bucket_index].insert(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket_index = self._hash(key)
        self.buckets[bucket_index].remove(key)
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucket_index = self._hash(key)
        return self.buckets[bucket_index].exist(key)

    def _hash(self, key):
        return key % self.bucket_size
        

class Node(object):
    def __init__(self, value, nextNode = None):
        """
        Initialize linkedlist
        """
        self.value = value
        self.nextNode = nextNode

class Buckets(object):
    def __init__(self):
        self.

    def insert(self, )



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)