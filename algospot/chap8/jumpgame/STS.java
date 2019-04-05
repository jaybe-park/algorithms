package apss.chap08.jumpgame;

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
			
			st = new StringTokenizer(br.readLine(), " ");
			N = Integer.parseInt(st.nextToken());
			map = new int[N][N];
			cache = new int[N][N];
			for(int jnx=0; jnx<N; jnx++) {
				st = new StringTokenizer(br.readLine(), " ");
				for(int knx=0; knx<N; knx++) {
					map[knx][jnx] = Integer.parseInt(st.nextToken());
				}
			}
			
			int result = jump(0,0);
			
			if(result==1) System.out.println("YES");
			else System.out.println("NO");
			
		}

	}
	
	public static int jump(int y, int x) {
		if(y>=N||x>=N) return -1;
		if(y==N-1&&x==N-1) return 1;
		
		if(cache[y][x]!=0) return cache[y][x];
		
		int jumpSize = map[y][x];
		int j = jump(y+jumpSize,x);
		if(j==1) {
			cache[y][x] = j;
			return j;
		}
		j = jump(y,x+jumpSize);
		if(j==1) {
			cache[y][x] = j;
			return j;
		}
		return cache[y][x] = -1;
	}

}
