import java.util.Scanner;

public class Ex1071 {
    public static boolean isOdd(int num) {
        return num % 2 != 0;
    }

    public static int sumOddNumbers(int start, int end) {
        int total = 0;
        for (int num = start; num <= end; num++) {
            if (isOdd(num)) {
                total += num;
            }
        }
        return total;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o valor de x: ");
        int x = scanner.nextInt();
        System.out.println("Digite o valor de y: ");
        int y = scanner.nextInt();

        if (x > y) {
            int aux = x;
            x = y;
            y = aux;
        }
        int resultado = sumOddNumbers(x, y);
        System.out.println("Soma dos impares: " + resultado);
    }
}