package Easy;

public class MaxConsecutiveOnes {

    public int maxConsecutiveOnes(int[] arr){
        int res = 0;
        int count  = 0;
        for(int i = 1; i < arr.length ; i++){
            if (arr[i] == 0)
                count = 0;
            else{
                if (arr[i-1] == arr[i]){
                    count++;
                    res = Math.max(res, count);
                }

            }
        }
        return res;
    }

}
