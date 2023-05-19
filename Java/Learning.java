import java.text.NumberFormat;
import java.util.*;

public class Learning {
    public static void main(String[] args) {
        int Principle;
        double Rate;
        double Time;
        try (Scanner my_scan = new Scanner(System.in)) {
            System.out.print("Principle: ");
            Principle = my_scan.nextInt();
            System.out.print("Rate: ");
            Rate = my_scan.nextInt();
            System.out.print("Time: ");
            Time = my_scan.nextInt();
            Double SimpleIntrest = (Principle * Rate * Time) / 100;
            NumberFormat currency = NumberFormat.getCurrencyInstance();
            String SI = currency.format(SimpleIntrest);
            System.out.println(SI);

        }
    }

}
