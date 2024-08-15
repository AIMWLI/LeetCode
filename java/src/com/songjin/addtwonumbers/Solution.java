package com.songjin.addtwonumbers;

/**
 * 将两个非空链表表示的非负整数相加。
 * 数字以逆序存储，每个节点包含一个数字。
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            int sum = carry;
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }

            current.next = new ListNode(sum % 10);
            current = current.next;
            carry = sum / 10;
        }

        return dummy.next;
    }

    public static void main(String[] args) {
        ListNode l1 = createList(new int[]{2, 4, 3});
        ListNode l2 = createList(new int[]{5, 6, 4});
        ListNode result = new Solution().addTwoNumbers(l1, l2);
        System.out.println("Test 1: " + printList(result));

        // 测试用例2
        l1 = createList(new int[]{0});
        l2 = createList(new int[]{0});
        result = new Solution().addTwoNumbers(l1, l2);
        System.out.println("Test 2: " + printList(result));

        // 测试用例3
        l1 = createList(new int[]{9, 9, 9, 9, 9, 9, 9});
        l2 = createList(new int[]{9, 9, 9, 9});
        result = new Solution().addTwoNumbers(l1, l2);
        System.out.println("Test 3: " + printList(result));
    }

    // 辅助方法：打印链表
    private static String printList(ListNode head) {
        StringBuilder sb = new StringBuilder();
        while (head != null) {
            sb.append(head.val);
            head = head.next;
            if (head != null) sb.append(" -> ");
        }
        return sb.toString();
    }

    // 辅助方法：创建链表
    private static ListNode createList(int[] arr) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        for (int val : arr) {
            current.next = new ListNode(val);
            current = current.next;
        }
        return dummy.next;
    }
}