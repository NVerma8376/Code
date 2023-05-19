import java.util.*;

public class palindrome {
    public void main() {
        String num1;
        char[] num2;
        char[] num3;

        try (Scanner my_scan = new Scanner(System.in)) {
            System.out.print("Enter something: ");
            num1 = my_scan.nextLine();
        }

        boolean palindrome = false;

        for (int i = 0; i < num1.length(); i++) {
            num2 = num1.toCharArray();
            for (int j = num1.length() - 1 - i; j >= 0; j--) {
                num3 = num1.toCharArray();
                if (i + j == num1.length() - 1) {
                    if (num2[i] == num3[j]) {
                        palindrome = true;
                    } else {
                        palindrome = false;
                        break;
                    }
                }
            }
        }
        if (palindrome == true) {
            System.out.println("palindrome");
        } else {
            System.out.println("not a palindrome");
        }

        System.out.println("--------------------------------");

    }
}
