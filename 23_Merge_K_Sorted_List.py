# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        input_len = len(lists)
        interval = 1
        
        if input_len == 0:
            return None
        
        while interval < input_len:
            for i in range(0, input_len - interval, 2 * interval):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]
         
        
    def merge2Lists(self, l1, l2):
        temp = ListNode(-23)
        result = temp
        
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            
            temp = temp.next
        if l1:
            temp.next = l1
        else:
            temp.next = l2
        
        return result.next