public class Piramid {
    public static void main(String[] args) {
        int row = 10;
        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println("");

        }
    }
}
