package apss.chap08.trianglepath;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N = 0;
	static int[][] map = null;
	static int[][] cache = null;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int T = Integer.parseInt(st.nextToken());
		
		for(int inx=0; inx<T; inx++) {
			
			N = Integer.parseInt(new StringTokenizer(br.readLine(), " ").nextToken());
			map = new int[N][N];
			cache = new int[N][N];
			
			for(int jnx=0; jnx<N; jnx++) {
				st = new StringTokenizer(br.readLine(), " ");
				for(int knx=0; knx<=jnx; knx++) {
					map[jnx][knx] = Integer.parseInt(st.nextToken());
				}
			}
			
			System.out.println(findMax(0,0));
		}

	}
	
	public static int findMax(int y, int x) {
		if(y == N-1) return map[y][x];
		
		if(cache[y][x]!=0) return cache[y][x];
		
		int result1 = findMax(y+1,x);
		int result2 = findMax(y+1,x+1);
		int result = (result1>result2) ? result1 : result2;
		return cache[y][x] = result + map[y][x];
	}

}
