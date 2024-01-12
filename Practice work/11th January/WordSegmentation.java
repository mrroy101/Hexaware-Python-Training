public class WordSegmentation {
    public static void main(String[] args) {
        String input1 = "idontlikesung";
        String input2 = "ilikesamsung";

        String[] dictionary = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"};

        if (canSegment(input1, dictionary)) {
            System.out.println("Output for " + input1 + ": Yes");
        } else {
            System.out.println("Output for " + input1 + ": No");
        }

        if (canSegment(input2, dictionary)) {
            System.out.println("Output for " + input2 + ": Yes");
        } else {
            System.out.println("Output for " + input2 + ": No");
        }
    }

    static boolean canSegment(String input, String[] dictionary) {
        if (input.isEmpty()) {
            return true;
        }

        for (String word : dictionary) {
            if (input.startsWith(word)) {

                if (canSegment(input.substring(word.length()), dictionary)) {
                    return true;
                }
            }
        }

        return false;
    }
}
