class Queue:
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0
    
    def isEmpty(self):
        return self._qhead is None
    
    def __len__(self):
        return self._count
    
    def add(self, item):
        node = _QueueNode(item)
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node
        self._qtail = node
        self._count += 1
    
    def pop(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._count -= 1
        return node.item
    
    def lst_all(self):
        lst = []
        while not self.isEmpty():
            it = self.pop()
            lst.append(it)
        return lst

class _QueueNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None
