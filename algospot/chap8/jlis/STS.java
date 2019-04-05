package apss.chap08.jlis;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N1 = 0;
	static int N2 = 0;
	static int[] array1 = null;
	static int[] array2 = null;
	static int[][] cache = null;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int T = Integer.parseInt(st.nextToken());
		
		for(int tnx=0; tnx<T; tnx++) {
			
			st = new StringTokenizer(br.readLine(), " ");
			N1 = Integer.parseInt(st.nextToken());
			N2 = Integer.parseInt(st.nextToken());
			array1 = new int[N1+1];
			array1[0] = Integer.MIN_VALUE;
			array2 = new int[N2+1];
			array2[0] = Integer.MIN_VALUE;
			cache = new int[N1+2][N2+2];

			st = new StringTokenizer(br.readLine(), " ");
			for(int inx=1; inx<=N1; inx++) 
				array1[inx] = Integer.parseInt(st.nextToken());
			
			st = new StringTokenizer(br.readLine(), " ");
			for(int inx=1; inx<=N2; inx++) 
				array2[inx] = Integer.parseInt(st.nextToken());
			
			System.out.println(jlis(0,0)-2);
			
		}
		
	}
	
	public static int jlis(int inx1, int inx2) {
		
		if(cache[inx1][inx2]!=0) return cache[inx1][inx2];
		
		cache[inx1][inx2] = 2;
		int i1 = (inx1 == 0) ? Integer.MIN_VALUE : array1[inx1];
		int i2 = (inx2 == 0) ? Integer.MIN_VALUE : array2[inx2];
		int i = (i1>i2) ? i1 : i2;
		
		for(int next1 = inx1 + 1; next1<=N1; next1++) 
			if(i<array1[next1]) {
				int recur = jlis(next1,inx2)+1;
				cache[inx1][inx2] = (cache[inx1][inx2] > recur) ? cache[inx1][inx2] : recur;
			}
		
		for(int next2 = inx2 + 1; next2<=N2; next2++) 
			if(i<array2[next2]) {
				int recur = jlis(inx1,next2)+1;
				cache[inx1][inx2] = (cache[inx1][inx2] > recur) ? cache[inx1][inx2] : recur;
			}
		
		return cache[inx1][inx2];
	}

}
