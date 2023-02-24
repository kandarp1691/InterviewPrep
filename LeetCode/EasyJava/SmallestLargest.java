package Easy;

public class SmallestLargest {

    public static String[] smallestLargestString(String testString){
        int s = 10000;
        int l = 0;
        String[] split_string = testString.split(" ");
        String smallest = "";
        String largest = "";
        for(int i = 0; i < split_string.length; i++){
            if(split_string[i].length() > l){
                largest = split_string[i];
                l = largest.length();
            }
            if(split_string[i].length() < s){
                smallest = split_string[i];
                s = smallest.length();
            }
        }
        return new String[]{smallest, largest};
    }
    public static void main(String[] args) {
        String test = "this is a largest rhinoceros";
        System.out.println(smallestLargestString(test)[1]);
    }

}
