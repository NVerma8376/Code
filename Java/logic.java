import java.util.*;

public class logic {

    public void oddEven() {
        try (Scanner mScan = new Scanner(System.in)) {
            System.out.print("Enter a number: ");
            int num = mScan.nextInt();

            if (num % 2 == 0) {
                System.out.println("Even");
            } else {
                System.out.println("Odd");
            }
        }
    }

    public void prime() {
        try (Scanner mScan = new Scanner(System.in)) {
            System.out.print("Enter number: ");
            int num = mScan.nextInt();

            for (int i = 2; i <= num; i++) {
                if (num % i == 0) {
                    System.out.println("prime");
                } else {
                    System.out.println("not prime");
                }
            }
        }
    }

    public static void main(String[] args) {
        palindrome palindrome = new palindrome();
        special_num special = new special_num();
        AmstrongChecker amstrong = new AmstrongChecker();
        logic logic = new logic();
        logic.oddEven();
        logic.prime();
        palindrome.main();
        special.main();
        amstrong.main();

    }
}
