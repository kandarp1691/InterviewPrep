package Easy;

public class SearchInsertPosition {

    public static int searchInsert(int[] nums, int target){
        for (int i = 0; i < nums.length; i++) {
            if(nums[i] == target || nums[i] > target)
                return i;
        }
        if(nums[nums.length-1] < target)
            return nums.length;
        else
            return -1;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{1,3,5,6};
        int target = 7;
        System.out.println(searchInsert(nums, target));
    }
}
