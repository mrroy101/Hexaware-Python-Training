import java.util.Scanner;

public class MaximumDifference {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the size");
        int n  = sc.nextInt();
        int maxDiff = -1;
        int[] arr= new int[n];
        System.out.println("enter the elements");
        for(int i=0;i<n;i++)
            arr[i] = sc.nextInt();
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                maxDiff = max(maxDiff,arr[j]-arr[i]);
            }
        }
        System.out.println("the maximum difference is " + maxDiff);
    }

    private static int max(int diff, int x) {
    
        if(diff>x)
        return diff;
        else
        return x;
    }
}
