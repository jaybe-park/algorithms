package apss.chap08.lis2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N = 0;
	static int[] array = null;
	static int[] cache = null;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		int T = Integer.parseInt(st.nextToken());
		
		for(int tnx=0; tnx<T; tnx++) {
			N = Integer.parseInt(new StringTokenizer(br.readLine(), " ").nextToken());
			array = new int[N];
			cache = new int[N];
			
			st = new StringTokenizer(br.readLine(), " ");
			for(int inx=0; inx<N; inx++) 
				array[inx] = Integer.parseInt(st.nextToken());
			
			System.out.println(lis(0));
			
		}
		
	}
	
	public static int lis(int start) {
		
		if(cache[start]!=0) return cache[start];
		
		cache[start] = 1;
		for(int next = start+1; next<N; next++) {
			if(array[start] < array[next]) {
				int recur = lis(next) + 1;
				cache[start] = (cache[start] > recur) ? cache[start] : recur; 
			}
		}
		return cache[start];
		
	}

}
