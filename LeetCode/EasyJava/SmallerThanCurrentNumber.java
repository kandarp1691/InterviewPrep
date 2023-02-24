package Easy;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class SmallerThanCurrentNumber {

    public int[] smallerNumbersThanCurrent(int[] nums){
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        int[] copy = nums.clone();
        Arrays.sort(copy);
        for (int i = 0; i < nums.length; i++) {
            hashMap.putIfAbsent(copy[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            copy[i] = hashMap.get(nums[i]);
        }

        return copy;
    }

}
