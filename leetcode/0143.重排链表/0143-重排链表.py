# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head:
            #�ҵ��м�ڵ�leftΪ[1,2]
            left=slow =fast=head            
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            #slow.nextָ��none��ֹ��
            node,slow.next = slow.next, None
            #��ת������ͷ���pre
            pre = None 
            while node:
                node.next,pre,node = pre,node,node.next 
            #����ƴ��,��߳��ȱ��ұߴ�1�����                    
            while pre:
                left.next,pre.next,left,pre = pre,left.next,left.next,pre.next
            
        
