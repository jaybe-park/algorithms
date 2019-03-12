package starbuksGangster.day1.Q14863;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static final int MAXN = 100;
	static final int MAXK = 100000;	
	static int N, K;
	
	static int[][] nodeInfo =  new int[MAXN+1][4];
	static int[][] memo     =  new int[MAXN+1][MAXK+1];

	public static void main(String[] args) throws Exception{
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		for(int inx=0; inx<N; inx++) {
			st = new StringTokenizer(br.readLine(), " ");
			nodeInfo[inx][0] = Integer.parseInt(st.nextToken()); //walking time cost
			nodeInfo[inx][1] = Integer.parseInt(st.nextToken()); //walking donation
			nodeInfo[inx][2] = Integer.parseInt(st.nextToken()); //riding time cost
			nodeInfo[inx][3] = Integer.parseInt(st.nextToken()); //riding donation
		}

		int maxWalkingDonation = dfs(0, nodeInfo[0][1], nodeInfo[0][0]);
		int maxRidingDonation = dfs(0, nodeInfo[0][3], nodeInfo[0][2]);
		int answer = (maxWalkingDonation > maxRidingDonation) ? maxWalkingDonation : maxRidingDonation;
		
		System.out.println(answer);

	}
	
	public static int dfs(int cnt, int donation, int timeCost) {
		
		if(timeCost > K)
			return -1;
		
		if(memo[cnt][timeCost] == -1)
			return -1;
		
		if(cnt == N && timeCost <= K)
			return donation;
		
		if(memo[cnt][timeCost] != 0)
			return memo[cnt][timeCost] + donation;
		
		int val = -1;
		int nextWalkingVal = dfs(cnt+1, donation + nodeInfo[cnt+1][1], timeCost + nodeInfo[cnt+1][0]);
		int nextRidingVal = dfs(cnt+1, donation + nodeInfo[cnt+1][3], timeCost + nodeInfo[cnt+1][2]);
		
		val = (val>nextWalkingVal) ? val : nextWalkingVal;
		val = (val>nextRidingVal) ? val : nextRidingVal;
		
		if(val == -1) {
			memo[cnt][timeCost] = -1;
		}else {
			memo[cnt][timeCost] = val - donation;
		}
		
		return val;
	}

}
