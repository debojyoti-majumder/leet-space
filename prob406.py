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
        self.tail:ListNode = None
        self.size:int = 0

    # TODO : Bug when the position of insert is head don't have logic 
    # to add head
    def insertNode(self, node:ListNode, pos:ListNode = None) -> ListNode:
        if self.head != None:
            # Append the data to the tail
            if pos == None:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                return self.tail

            prevNode:ListNode = pos.prev
            node.prev = prevNode
            pos.prev = node
            node.next = pos
            prevNode.next = node

            return node
        else:
            self.head = node
            self.tail = self.head
            self.tail.prev = self.head

            return self.head
    
    def getList(self) -> List[ListNode]:
        returnedList:List[ListNode] = []
        it:ListNode = self.head

        while it != None:
            returnedList.append(it)
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
        p = People(h,b)
        peopleNode = ListNode(p)
        indexNode:ListNode = None

        if b in self.indexMap:
            indexNode = self.indexMap[b]
        
        nd = self.constrctedQueue.insertNode(peopleNode, indexNode)
        self.indexMap[b] = nd

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))

        for hight, before in people:
            self.putPeople(hight, before)
            orderedList = self.constrctedQueue.getList()

        orderedList = self.constrctedQueue.getList()
        return []
    
sol = Solution()
sol.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])