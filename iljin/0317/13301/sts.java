package StarbucksGangster.day2.Q13301;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int Num;
	static long[] memo = new long[81];

	public static void main(String[] args) throws Exception{
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		Num = Integer.parseInt(st.nextToken());
		memo[0] = 1;
		memo[1] = 1;
		
		fibonacci(Num);
		
		long val = (memo[Num]+memo[Num-1])*2;
		
		System.out.println(val);

	}
	
	public static long fibonacci(int n) {
		
		if(n==0&&n==1)
			return 1;
		
		if(memo[n]!=0)
			return memo[n];
		
		long val = fibonacci(n-1) + fibonacci(n-2);
		memo[n] = val;
		return val;
	}

}
