import java.util.Scanner;

public class LookAndSay{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); 
        String result = lookAndSay(n);
        System.out.println("The " + n + "'th term in the Look-and-say sequence is: " + result);
    }

    static String lookAndSay(int n) {
        if (n <= 0) {
            return "Invalid input";
        }

        if (n == 1) {
            return "1";
        }

        String previousTerm = "1";
        for (int i = 2; i <= n; i++) {
            previousTerm = getNextTerm(previousTerm);
        }

        return previousTerm;
    }

    static String getNextTerm(String s) {
        StringBuilder result = new StringBuilder();
        int count = 1;

        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                count++;
            } else {
                result.append(count).append(s.charAt(i - 1));
                count = 1;
            }
        }

       
        result.append(count).append(s.charAt(s.length() - 1));

        return result.toString();
    }
}
