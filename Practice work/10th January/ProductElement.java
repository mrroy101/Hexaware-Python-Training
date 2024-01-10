import java.util.*;

public class ProductElement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the size");
        int n  = sc.nextInt();
        int prod = 1;
        int[] res = new int[n];
        int[] arr= new int[n];
        System.out.println("enter the elements");
        for(int i=0;i<n;i++)
            arr[i] = sc.nextInt();
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(j==i)
                continue;
                else{
                    prod = prod*arr[j];
                }
               
            }
             res[i]=prod;
                prod = 1;
        }
        for(int i=0;i<n;i++)
        System.out.println(res[i]);


    }
}
