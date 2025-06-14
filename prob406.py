# Leetcode problem URL 
# https://leetcode.com/problems/queue-reconstruction-by-height/?envType=problem-list-v2&envId=binary-indexed-tree
# ID : 406
# Difficuly : Medium

from typing import List

class ListNode:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head:ListNode = None
        self.size:int = 0

    def getAtIndex(self, idx:int) -> ListNode:
        nd:ListNode = self.head
        for _ in range(idx-1):
            nd = nd.next
        
        return nd

    # This function inserts data into a node, if position is sepcified by pos then the
    # node gets added in the left and if index is specified via `idx` then insertion
    # happens on right
    def insertNode(self, node:ListNode, pos:ListNode = None, idx:int=-1) -> ListNode:
        if self.head == None:
            self.head = node
            return self.head
 
        if pos == None:
            pos = self.getAtIndex(idx)
            nextNode = pos.next
            node.next = nextNode
            pos.next = node
            node.prev = pos

            if nextNode != None:
                nextNode.prev = node

            return node

        # Node gets added to the r
        prevNode:ListNode = pos.prev
        node.prev = prevNode
        pos.prev = node
        node.next = pos

        if prevNode != None:
            prevNode.next = node
        else:
            self.head = node

        return node
    
    def getList(self) -> List[any]:
        returnedList:List[any] = []
        it:ListNode = self.head

        while it != None:
            returnedList.append(it.data)
            it = it.next

        return returnedList


class People:
    def __init__(self, height, before):
        self.height = height
        self.before = before

class Solution:
    def __init__(self):
        self.constrctedQueue:LinkedList = LinkedList()
        self.indexMap:dict[int:ListNode] = {}

    def putPeople(self, h:int, b:int):
        peopleNode = ListNode([h,b])
        indexNode:ListNode = None

        if b in self.indexMap:
            indexNode = self.indexMap[b]
        
        nd = self.constrctedQueue.insertNode(peopleNode, indexNode, b)
        self.indexMap[b] = nd

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))

        for hight, before in people:
            self.putPeople(hight, before)

        return self.constrctedQueue.getList()
    
sol = Solution()
ret = sol.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
print(ret)

sol2 = Solution()
ret = sol2.reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]])
print(ret)

# [[6,0],[1,1],[8,0],[7,1],[9,0],[2,4],[0,6],[2,5],[3,4],[7,3]]
sol3 = Solution()
ret = sol3.reconstructQueue([[2,4],[3,4],[9,0],[0,6],[7,1],[6,0],[7,3],[2,5],[1,1],[8,0]])
print(ret)