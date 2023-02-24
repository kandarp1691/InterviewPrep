package Easy;

import java.util.ArrayList;
import java.util.HashMap;

public class FindDuplicates {

    public static ArrayList<Integer> getDups(int[] arr){
        HashMap<Integer, Integer> dups = new HashMap<>();
        if(arr.length == 0 || arr.length == 1)
            return null;
        for(int i=0; i < arr.length ; i++){
            if(dups.containsKey(arr[i]))
                dups.put(arr[i], dups.get(arr[i]) + 1);
            else
                dups.put(arr[i], 1);
        }
        ArrayList<Integer> res = new ArrayList<>();

        dups.forEach((k,v) -> {
            if(v > 1)
                res.add(k);
        });

        return res;
    }

    public static void main(String[] args) {
        int arr[] = {1,2,3,4,1,1,4,0,2,3};
        System.out.println(getDups(arr));
    }

}
