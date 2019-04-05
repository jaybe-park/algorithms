package apss.chap08.lis;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N = 0;
	static int[] lis = null;
	static int lisSize = -1;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int T = Integer.parseInt(st.nextToken());
		
		for(int inx=0; inx<T; inx++) {
			N = Integer.parseInt(new StringTokenizer(br.readLine(), " ").nextToken());
			lis = new int[N];
			lisSize = -1;
			st = new StringTokenizer(br.readLine(), " ");
			for(int jnx=0; jnx<N; jnx++) {
				int temp = Integer.parseInt(st.nextToken());
				if(lisSize==-1) {
					lisSize++;
					lis[lisSize] = temp;
				}else {
					if(lis[lisSize]<temp) {
						lisSize++;
						lis[lisSize] = temp;
					}else {
						int knx = lisSize-1;
						if(knx!=-1)
							while(lis[knx]>temp) {
								knx--;
								if(knx==-1) break;
							}
						lis[knx+1] = temp;
					}
				}
			}
			System.out.println(lisSize+1);
		}

	}

}
