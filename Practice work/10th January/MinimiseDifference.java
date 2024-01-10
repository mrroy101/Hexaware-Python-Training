import java.util.Arrays;
import java.util.Scanner;

public class MinimiseDifference {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the size");
        int n  = sc.nextInt();
        System.out.println("enter k");
        int k= sc.nextInt();
        int[] arr= new int[n];
        int avg=0;
        System.out.println("enter the elements");
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
            avg+=arr[i];
        }
        avg = avg/n;
        for(int i=0;i<n;i++){
            if(arr[i]>avg)
                arr[i]-=k;
            else
                arr[i]+=k;
        }
        Arrays.sort(arr);

        int diff = arr[n-1]-arr[0];
        System.out.println("the minimum difference is "+ diff);



    }
}