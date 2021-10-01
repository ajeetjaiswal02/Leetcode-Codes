#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

#Merge all the linked-lists into one sorted linked-list and return it.

#Example 1
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
#Explanation: The linked-lists are:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#merging them into one sorted list:
# output  = 1->1->2->3->4->4->5->6

class Linkedlist:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        self.ans = []
        head = value = lists[0]
        for l in lists:
            while l:
                self.ans.append(l.val)
                l = l.next
        for x in sorted(self.ans):
            value.next = Linkedlist(x)
            value = value.next
        return head.next

p = Linkedlist()
p.mergeKLists([[1,4,5],[1,3,4],[2,6]])        