package Easy;

import java.util.Arrays;
import java.util.HashMap;

public class TwoSumIndex {

    public static int[] twoSumIndices(int[] arr, int target){
        HashMap<Integer, Integer> hmap = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            int diff = target - arr[i];
            if(hmap.containsKey(diff))
                return new int[]{i, hmap.get(diff)};
            else
                hmap.put(arr[i], i);

        }
        return null;
    }

    public static void main(String[] args) {
        int[] arr = {2,5,7,11};
        int[] res = twoSumIndices(arr, 9);
        System.out.println(res);
    }


}
