import java.util.*;

public class Fibonacci {
    public static void main(String[] args) {
        long num1 = 0;
        long num2 = 1;
        long num3;
        int count;
        try (Scanner my_scan = new Scanner(System.in)) {
            System.out.print("Enter a number: ");
            count = my_scan.nextInt();
            System.out.print(num1 + " " + num2);
            for (int i = 2; i < count; i++) {
                num3 = num1 + num2;
                System.out.print(" " + num3);
                num1 = num2;
                num2 = num3;
            }
        }

    }

}
