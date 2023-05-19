
import java.util.*;

public class Calc {
    public static void main(String[] args) {

        Instruction();

        try (Scanner scan = new Scanner(System.in)) {
            System.out.print("Enter what you want to do: ");
            int input = scan.nextInt();
            if (input == 1) {
                addition();
            }
            if (input == 2) {
                subtraction();
            }
            if (input == 3) {
                multiplication();
            }
            if (input == 4) {
                division();
            }
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }

    }

    private static void Instruction() {
        System.out.println(
                "Enter '1' for addition,\nEnter '2' for subtraction\nEnter '3' for multiplication\nEnter '4' for division");
    }

    public static void addition() {
        int num1;
        int num2;
        try (Scanner new_scanner = new Scanner(System.in)) {
            System.out.print("Enter num 1: ");
            num1 = new_scanner.nextInt();
            System.out.print("Enter num 2: ");
            num2 = new_scanner.nextInt();
        }

        System.out.print(num1 + num2);

    }

    public static void subtraction() {
        int num1;
        int num2;
        try (Scanner new_scanner = new Scanner(System.in)) {
            System.out.print("Enter num 1: ");
            num1 = new_scanner.nextInt();
            System.out.print("Enter num 2: ");
            num2 = new_scanner.nextInt();
        }

        System.out.print(num1 - num2);

    }

    public static void multiplication() {
        int num1;
        int num2;
        try (Scanner new_scanner = new Scanner(System.in)) {
            System.out.print("Enter num 1: ");
            num1 = new_scanner.nextInt();
            System.out.print("Enter num 2: ");
            num2 = new_scanner.nextInt();
        }
        System.out.print(num1 * num2);
    }

    public static void division() {
        int num1;
        int num2;
        try (Scanner new_scanner = new Scanner(System.in)) {
            System.out.print("Enter num 1: ");
            num1 = new_scanner.nextInt();
            System.out.print("Enter num 2: ");
            num2 = new_scanner.nextInt();
        }
        double ans = num1 / num2;
        System.out.print(ans);
    }
}