package Easy;

import java.util.HashMap;

public class GoodPairs {

    public static int numIdenticalPairs(int[] nums){
//        int counter = 0;
//        for (int i = 0; i < nums.length ; i++){
//            for (int j = i+1; j < nums.length; j++) {
//                if (nums[i] == nums[j])
//                    counter++;
//            }
//        }
//        return counter;

        int counter = 0;
        HashMap<Integer, Integer> hm = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int count = hm.getOrDefault(nums[i], 0);
            counter = count+counter;
            hm.put(nums[i], count+1);
        }
        return counter;

    }

    public static void main(String[] args) {
        int[] nums = new int[]{1,2,3,1,1,3};
        System.out.println(numIdenticalPairs(nums));
    }
}
