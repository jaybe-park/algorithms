package ps.algospot.chap6.picnic;
import java.lang.*;
import java.io.*;
import java.util.*;

/*

 * 
 */
class Jaegoon {
	 
	static int N;
	static int TC, M;
	static int answer;
	static boolean map[][];
	static Scanner sc;
	static boolean visit[];
	
	static void init() {
		
		N = sc.nextInt();
		M = sc.nextInt();
		map = new boolean[N][N];
		visit = new boolean[N];
		answer = 0;
		
		for(int i=1; i<=M; i++) {
			int n1 = sc.nextInt();
			int n2 = sc.nextInt();
			
			if(n1<n2) map[n1][n2] = true;
			else map[n2][n1] = true;
		}
		
	}
	
	static int dfs(int students, int st, boolean visit[]) {
		
		
		
		int temp = 0;
		for(int i=st+1;i<N;i++) {
			if(map[st][i] && !visit[i]) {
				
				if(students-2 == 0) return 1;
				
				visit[i] = true;
				
				
				for(int j=st+1;j<N;j++) {
					if(!visit[j]) {
						visit[j] = true;
						temp += dfs(students-2, j, visit);
						visit[j] = false;
					}
				}				
				visit[i] = false;
			}
		}
		
		return temp;
	}
	
	public static void main(String [] args) throws Exception {
		
		sc = new Scanner(System.in);
		TC = sc.nextInt();
		
		for(int t=1; t<=TC; t++) {
			
			init();
			visit[0]= true;
			answer = dfs(N, 0, visit);
			
			System.out.println(answer);
		}
		
		sc.close();
	}

}