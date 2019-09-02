import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the commonChild function below.
    int commonChild(char[] u, char[] v, int m, int n) {
        int l[][] = new int[m+1][n+1];
        
        for(int i=0;i<m+1;i++){
            for(int j=0;j<n+1;j++){
                if(i==0 || j==0)
                    l[i][j]=0;
                else if (u[i-1]==v[j-1])
                    l[i][j]=1+l[i-1][j-1];
                else
                    l[i][j]=max(l[i-1][j],l[i][j-1]);
            }
        }

        return l[m][n];
    }
    
    int max(int a, int b){
        return (a>b)?a:b;
    }
 

    public static void main(String[] args) throws IOException {
        Solution commSolution = new Solution();
        Scanner sc = new Scanner(System.in);
        String s1 = sc.next();
        String s2 = sc.next();
        
        char[] u = s1.toCharArray();
        char[] v = s2.toCharArray();
        int m=u.length;
        int n=v.length;
        System.out.println(commSolution.commonChild(u,v,m,n));
        
    }
}
