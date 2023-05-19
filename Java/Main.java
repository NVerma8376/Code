import java.util.*;
import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        try (Scanner mScanner = new Scanner(System.in)) {
            System.out.print("Enter Number: ");
            double number = mScanner.nextDouble();

            double answer = 0;

            for (int i = 1; i < number + 1; i++) {
                answer = Math.pow((number / i), i) + answer;
            }
            System.out.println(answer);
        }

    }

}
