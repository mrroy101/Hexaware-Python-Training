import java.util.Scanner;

public class NonRepeatingElement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the size");
        int n  = sc.nextInt();
        int num =0 ;
        boolean flag = false;
        int[] arr= new int[n];
        System.out.println("enter the elements");
        for(int i=0;i<n;i++)
            arr[i] = sc.nextInt();
        for(int i=0;i<n;i++){
            flag=false;
            for(int j=0;j<n;j++){
                if(i!=j && arr[i]==arr[j]){
                flag=true;
                break;
            }
            }
            if(flag==false)
            {
                num= arr[i];
                break;
            }
    }
    System.out.println("the num is "+ num);
}
}