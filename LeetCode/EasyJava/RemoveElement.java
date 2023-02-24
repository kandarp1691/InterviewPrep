package Easy;

import java.util.Arrays;

public class RemoveElement {

    public static int[] removeElement(int[] arr, int element) {
        int l = 0;
        int r = arr.length - 1;
        while (l < r) {
            if (arr[r] == element)
                r--;
            if (arr[l] == element) {
                int temp = arr[l];
                arr[l] = arr[r];
                arr[r] = temp;
                r--;
            }
            l++;
        }
        return Arrays.copyOfRange(arr, 0, l + 1);
    }

    public static void main(String[] args) {
        int[] arr = new int[] {0,1,2,2,3,0,4,2};
        int element = 2;
        removeElement(arr, element);
        System.out.println("Output");
    }
}
