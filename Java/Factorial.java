public class Factorial {
    public int fact(int num, int ans) {

        for (int i = 0; i < num; i++) {
            ans = (num - i) * ans;
        }
        return ans;

    }

}
