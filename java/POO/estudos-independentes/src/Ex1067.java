import java.util.Scanner;

public class Ex1067 {
    public static boolean isOdd(int n) {
        return n % 2 != 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite um numero inteiro: ");
        int n = scanner.nextInt();
        for (int i = 1; i <= n; i++) {
            if (isOdd(i)) {
                System.out.println(i);
            }
        }
    }
}