import java.util.Scanner;

public class Ex1006 {

    public static boolean validarValor(double valor, double minimo, double maximo) {
        return minimo <= valor && valor <= maximo;
    }

    public static double lerValorValidado(String mensagem, double minimo, double maximo, Scanner scanner) {
        while (true) {
            try {
                System.out.print(mensagem);
                double valor = Double.parseDouble(scanner.nextLine());

                if (validarValor(valor, minimo, maximo)) {
                    return valor;
                } else {
                    System.out.println("Valor inválido! Digite um valor entre " + minimo + " e " + maximo + ".");
                }

            } catch (NumberFormatException e) {
                System.out.println("Entrada inválida! Digite um número.");
            }
        }
    }

    public static double calcularMediaPonderada(double a, double b, double c, int pesoA, int pesoB, int pesoC) {
        return (a * pesoA + b * pesoB + c * pesoC) / (pesoA + pesoB + pesoC);
    }

    public static void exibirMedia(double media) {
        System.out.printf("MEDIA = %.1f\n", media);
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        double a = lerValorValidado("Digite o primeiro valor: ", 0, 10, scanner);
        double b = lerValorValidado("Digite o segundo valor: ", 0, 10, scanner);
        double c = lerValorValidado("Digite o terceiro valor: ", 0, 10, scanner);

        double media = calcularMediaPonderada(a, b, c, 2, 3, 5);

        exibirMedia(media);

        scanner.close();
    }
}