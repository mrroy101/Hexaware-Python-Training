import java.util.Scanner;

public class DivisibilityBy7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = scanner.nextInt();

        while (number >= 7) {
            number = number - 7;
        }

        if (number == 0) {
            System.out.println("The number is divisible by 7.");
        } else {
            System.out.println("The number is not divisible by 7. Remainder: " + number);
        }

        scanner.close();
    }
}
