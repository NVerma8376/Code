import java.util.*;

public class AmstrongChecker {
    public void main() {

        String num1;
        char[] nums;
        double num2 = 0;
        double power;
        double ans = 0;

        try (Scanner my_scan = new Scanner(System.in)) {
            System.out.print("Enter a number: ");
            num1 = my_scan.nextLine();
        }

        num2 = Integer.parseInt(num1);

        for (int i = 0; i < num1.length(); i++) {
            power = num1.length();
            nums = num1.toCharArray();
            ans = Math.pow(Double.parseDouble(String.valueOf(nums[i])), power) + ans;
        }

        if (ans == num2) {
            System.out.println("it is amstrong");
        } else {
            System.out.println("it is not amstrong");
        }

    }
}