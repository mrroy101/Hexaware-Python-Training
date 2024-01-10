import java.util.Scanner;

public class MaximumSumCircularSubarray {

    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
        System.out.println("enter the size");
        int n  = sc.nextInt();
        int[] arr= new int[n];
        System.out.println("enter the elements");
        for(int i=0;i<n;i++)
            arr[i] = sc.nextInt();
       
        int maxNormal = 0;
        int maxCircular = 0;

        for (int i = 0; i < n; i++) {
            maxNormal = Math.max(arr[i], maxNormal + arr[i]);
            maxCircular += arr[i];
            arr[i] = -arr[i];
        }

       
        maxCircular = maxCircular + maxSubarraySum(arr);

        int result = Math.max(maxNormal, maxCircular);

        System.out.println("Subarray with the largest sum is: " + result);
    }

    private static int maxSubarraySum(int[] nums) {
        int maxSum = nums[0];
        int currentSum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            currentSum = Math.max(nums[i], currentSum + nums[i]);
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }
}
