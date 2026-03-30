class ListNode:
    def __init__(self, key: int = -1, value: int = -1, next = None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode() for _ in range(10**4)]

    def hash(self, key):
        return key % len(self.hashmap)


    def put(self, key: int, value: int) -> None:
        hashkey = self.hash(key)
        cur = self.hashmap[hashkey]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = ListNode(key, value, None)
        

    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        cur = self.hashmap[hashkey]
        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        cur = self.hashmap[hashkey]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        
        
        

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)