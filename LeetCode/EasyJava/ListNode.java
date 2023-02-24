package Easy;

import java.util.List;

public class ListNode {
         int val;
         ListNode next;
         ListNode() {}
         ListNode(int val) { this.val = val; }
         ListNode(int val, ListNode next) { this.val = val; this.next = next; }
      }

    class Solution {
        public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

            ListNode n = new ListNode();
            while (list1.next != null && list2.next != null){
                if(list1.val < list2.val) {
                    n.next = list1;
                    list1 = list1.next;
                }
                else {
                    n.next = list2;
                    list2 = list2.next;
                }

            }
            return n.next;

        }
    }

