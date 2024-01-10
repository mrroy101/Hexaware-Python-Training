import java.util.*;

public class PairWithSum {

    public static void findPairWithSum(int[] nums, int target) {
        Arrays.sort(nums);

        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int currentSum = nums[left] + nums[right];

            if (currentSum == target) {
                System.out.println("Pair found (" + nums[left] + ", " + nums[right] + ")");
                left++;
                right--;
            } else if (currentSum < target) {
               
                left++;

            } else {
                right--;
            }
        }
    }

    public static void main(String[] args) {
        int[] nums = {8, 7, 2, 5, 3, 1};
        int target = 10;

        findPairWithSum(nums, target);
    }
}
