import java.util.*;

class MinimumSquares {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the number");
        int num = sc.nextInt();
        System.out.println(getMinSquares(num));
        
    }
    static int getMinSquares(int n){
        int num= n;

        if(n<=3)
        return n;
        
        for(int i = 1;i<=n;i++){
            int temp = i * i;
            if(temp > n)
                break;
            else if(temp == n){
                num = 1;
                break;
            }
            else
                num = Math.min(num, 1 + getMinSquares(n-temp));

        }


        return num;


    }
}
