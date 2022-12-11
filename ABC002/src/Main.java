import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double[][] points = new double[3][2];
        for (int i = 0; i < points.length; i++) {
            points[i][0] = sc.nextInt();
            points[i][1] = sc.nextInt();
        }
        for (int i = 0; i < points.length; i++) {
            points[points.length-i-1][0] -= points[0][0];
            points[points.length-i-1][1] -= points[0][1];
        }
        System.out.println(Math.abs(points[1][0]*points[2][1] - points[1][1] * points[2][0])/2);
    }
}