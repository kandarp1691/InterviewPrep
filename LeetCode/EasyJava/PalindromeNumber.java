package Easy;

public class PalindromeNumber {

    public static boolean isPalindrome(int x){
        String stringValue = String.valueOf(x);
        if(stringValue.equals(reverse(stringValue)))
            return true;
        return false;
    }

    private static String reverse(String x){
        StringBuilder sb = new StringBuilder();
        for (int i = x.length()-1; i >= 0 ; i--) {
            sb.append(x.charAt(i));
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome(101));
    }
}
