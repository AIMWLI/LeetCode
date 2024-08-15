# 定义链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        将两个非空链表表示的非负整数相加。
        数字以逆序存储，每个节点包含一个数字。
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


def create_list(arr):
    """辅助函数：创建链表"""
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def print_list(head):
    """辅助函数：打印链表"""
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    return ' -> '.join(result)


if __name__ == "__main__":
    solution = Solution()

    # 测试用例1
    l1 = create_list([2, 4, 3])
    l2 = create_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print("Test 1:", print_list(result))

    # 测试用例2
    l1 = create_list([0])
    l2 = create_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print("Test 2:", print_list(result))

    # 测试用例3
    l1 = create_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    print("Test 3:", print_list(result))
