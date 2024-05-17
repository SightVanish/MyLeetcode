class LRUNode:
    def __init__(self, key, value, pre=None, next=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict() # key-node
        self.head = LRUNode(0, 0)
        self.tail = LRUNode(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        # check whether node is in cache
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            # put the node to the head 
            self.moveNodeToHead(node)
            # return value
            return node.value
            
    def put(self, key: int, value: int) -> None:
        # check whether node is in cache
        if key in self.cache:
            # update the value
            node = self.cache[key]
            node.value = value
            # put the node to the head
            self.moveNodeToHead(node)
        else:
            # check capacity
            if len(self.cache) >= self.capacity:
                # remove the last node
                delete_node = self.tail.pre
                delete_node.pre.next = self.tail
                self.tail.pre = delete_node.pre
                # remove the node from cache
                self.cache.pop(delete_node.key)
                # free the memory space
                del delete_node


            # create a new node
            new_node = LRUNode(key, value)
            # put the node to the head
            new_node.next = self.head.next
            new_node.pre = self.head
            self.head.next = new_node
            new_node.next.pre = new_node
            # put the node to the cache
            self.cache[new_node.key] = new_node

        

    def moveNodeToHead(self, node):
        pre_node = node.pre
        nex_node = node.next
        pre_node.next = nex_node
        nex_node.pre = pre_node

        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node


def printCache(lRUCache):
    print(lRUCache.cache)
    print(lRUCache.head.next.value, end = ' ')
    print(lRUCache.head.next.next.value)

# use OrderedDict -- based on hashmap and linked list
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = OrderedDict()
    
    def get(self, key: int) -> int:
        if key in self.values:
            self.values.move_to_end(key, last=True)
            return self.values[key]
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.values: 
            self.values.move_to_end(key, last=True)
            self.values[key] = value
        else:
            if len(self.values.keys()) >= self.capacity: self.values.popitem(last=False)
            self.values[key] = value
                

lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)


printCache(lRUCache)

lRUCache.put(3, 3)
printCache(lRUCache)

lRUCache.get(2)
lRUCache.put(4, 4)

