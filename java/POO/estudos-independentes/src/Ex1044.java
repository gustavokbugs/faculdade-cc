import java.util.Scanner;
//teste commit
public class Ex1044 {

    public static boolean valida_multiplos(int a, int b) {
        return a % b == 0 || b % a == 0;
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o primeiro numero: ");
        int a = scanner.nextInt();

        System.out.println("Digite o segundo numero: ");
        int b = scanner.nextInt();

        scanner.close();

        if (valida_multiplos(a, b)) {
            System.out.println("Sao multiplos");
        } else {
            System.out.println("Nao sao multiplos");
        }
    }
}