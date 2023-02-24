package Easy;

public class PlusOne {

    public static int[] plusOne(int[] digits){
        int last = digits[digits.length-1];
        if(last != 9) {
            digits[digits.length - 1] = last + 1;
            return digits;
        }
        return new int[]{-1};
    }

    public static void main(String[] args) {
        int[] digits = new int[]{9};
        System.out.println(plusOne(digits));
    }

}
