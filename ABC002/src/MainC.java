import java.util.Scanner;
import java.util.Arrays;

public class MainC {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = -1 * sc.nextInt();
        }
        Arrays.sort(arr);

        int[] com = new int[n];
        double c = 0;
        for (int i=k-1; i >= 0; i--) {
            c = (c - arr[i]) / 2;
        }
        System.out.println(c);
    }
}
