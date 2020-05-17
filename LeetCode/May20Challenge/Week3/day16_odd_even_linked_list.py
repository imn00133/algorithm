# https://leetcode.com/problems/odd-even-linked-list/
# Solved Date: 20.05.17.


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}, {self.next}'

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


class Solution:
    def odd_even_list(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd_prev = head
        even_head = head.next
        even_prev = head.next
        while even_prev is not None and even_prev.next is not None:
            odd_next = even_prev.next
            even_next = odd_next.next
            odd_prev.next = odd_next
            even_prev.next = even_next
            odd_prev = odd_next
            even_prev = even_next
        odd_prev.next = even_head
        return head

    def fast_odd_even_list(self, head:ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        even_head = head.next
        even = head.next
        while even is not None and even.next is not None:
            odd.next = even.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_head
        return head


def make_linked_list(values):
    head = ListNode(values[0])
    current_node = head
    for value in values[1:]:
        next_node = ListNode(value)
        current_node.next = next_node
        current_node = next_node
    return head


def main():
    values = [1, 2, 3, 4, 5, 6]
    head = make_linked_list(values)
    solution = Solution()
    head = solution.fast_odd_even_list(head)
    print(head)


if __name__ == '__main__':
    main()
