package StarbucksGangster.day2.Q13300;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int studentNum;
	static int capacity;
	static int[][] studentInfo = new int[2][6];
	static int minRoomNum = 0;

	public static void main(String[] args) throws Exception{
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		studentNum = Integer.parseInt(st.nextToken());
		capacity = Integer.parseInt(st.nextToken());
		
		for(int inx=0; inx<studentNum; inx++) {
			st = new StringTokenizer(br.readLine(), " ");
			studentInfo[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())-1]++;
		}
		
		for(int inx=0; inx<2; inx++) {
			for(int jnx=0; jnx<6; jnx++) {
				minRoomNum += studentInfo[inx][jnx]/capacity;
				
				if(studentInfo[inx][jnx]%capacity!=0) 
					minRoomNum++;
			}
		}
		
		System.out.println(minRoomNum);

	}

}
