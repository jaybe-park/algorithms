package ps.algospot.chap6.boggle;
import java.lang.*;
import java.io.*;
import java.util.*;

/*
 * DFS�� �̿��� ����Ž�� + �޸������̼��� �̿��� Ǯ����.
 * ó���� �޸������̼� ���� Ǯ������ �ð��ʰ��� ����.
 * �׷��� boolean visit[][][] = new boolean[6][6][�ܾ����]�� ���� �޸������̼��ߴ�.
 * visit�� ����Ʈ�� false�� �ΰ�, �ش� �ܾ��� ö�ڿ��� ���� �ܾ�� 8���� ��� �ܾ �ϼ����� ������ visit = true�� ������
 * �� ������ ö�ڿ� �ٽ� �湮���� �ʵ��� �ߴ�.
 * 
 */
class Jaegoon {
	 
	static int N;
	static int TC;
	static boolean answer;
	static String map[];
	static Scanner sc;
	static String word[];
	static int dx[] = {1, 1, 1, 0, -1, -1, -1, 0};
	static int dy[] = {1, 0, -1, -1, -1, 0, 1, 1};
	
	static void init() {
		
		map = new String[6];
		
		for(int y=1;y<=5;y++) {
			map[y] = sc.next();
		}
		
		N = sc.nextInt();
		word = new String[N+1];
		for(int i=1;i<=N;i++) {
			word[i] = sc.next();
		}
	}
	
	static boolean dfs(int x, int y, String s, int idx, boolean visit[][][]) {
		
		if(idx == s.length()) {
			return true;
		}
		
		boolean temp = false;
		
		
		for(int i=0;i<8;i++) {
			int nx = x+dx[i];
			int ny = y+dy[i];
			
			if(nx<1 || 5<nx || ny<1 || 5<ny) continue;
			else if(visit[ny][nx][idx+1]) continue;
			else if(map[ny].charAt(nx-1) == s.charAt(idx)) {
				//System.out.println(nx+" "+ny);
				temp= dfs(nx, ny, s, idx+1, visit);
				if(temp) return temp;
			}
			
		}
		visit[y][x][idx] = true;
		return false;
	}
	
	public static void main(String [] args) throws Exception {
		
		sc = new Scanner(System.in);
		TC = sc.nextInt();
		
		for(int t=1; t<=TC; t++) {
			
			init();
			
			for(int i=1;i<=N;i++) {
				String s = word[i];
				answer = false;
				for(int y=1;y<=5;y++) {
					for(int x=1;x<=5;x++) {
						if(map[y].charAt(x-1) == s.charAt(0)) {
							boolean visit[][][] = new boolean[6][6][s.length()+1];
							visit[y][x][0] = true;
							answer = dfs(x, y, s, 1, visit);
							if(answer) break;
						}
					}
					if(answer) break;
				}
				if(answer) System.out.println(s+" YES");
				else  System.out.println(s+" NO");
			}
		}
		
		sc.close();
	}

}