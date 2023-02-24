package Easy;

import java.util.PriorityQueue;

public class FindKthLargestSmallest {

    public static int ksmallest(int[] arr, int k){
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int x: arr){
            x =  x*-1;
            if(heap.size() < k || x >= heap.peek()){
                heap.offer(x);
            }
            if(heap.size() > k)
                heap.poll();

        }
        return heap.peek()*-1;
    }

    public static void main(String[] args) {
        int[] arr = new int[]{3,2,1,4,6,4};
        int k = 4;
        System.out.println(ksmallest(arr, k));
    }

}
