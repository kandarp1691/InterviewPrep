package Easy;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class RemoveVowelsFromString {

    public static String removeVowelsFromString(String testString){
        StringBuilder sb = new StringBuilder();
        ArrayList<Character> vowels = new ArrayList<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        for(int i=0 ; i < testString.length(); i++){
            if(!vowels.contains(testString.charAt(i))){
                sb.append(testString.charAt(i));
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        String testString = "abracadabra";
        System.out.println(removeVowelsFromString(testString));
    }
}
