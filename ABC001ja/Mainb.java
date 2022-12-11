import java.util.Scanner;

public class Mainb {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int val = sc.nextInt();
        double km = (double)val / 1000;

        String s = "";
        if (km < 0.1) {
            s += "00";
        } else if (km <= 5.0) {
//            System.out.println(val%1000);
            s += (val / 1000);
            s += (val % 1000) / 100;
        } else if (6 <= km && km <= 30) {
//            System.out.println(val / 1000 + 50);
//            System.out.println((val % 1000) / 100);
            s += (val / 1000 + 50);// + (val % 1000)/100;
        } else if (35 <= km && km <= 70) {
            s += ((val / 1000 -30)/5 + 80);
        } else if (km > 70) {
            s += "89";
        }
        System.out.println(s);
    }
}
