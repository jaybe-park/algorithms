package starbuksGangster.day1.Q14864;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.PriorityQueue;

public class Main {
	
	static int vortexNum, linkNum;
	static int[] cardPeople, upperCnt, lowerCnt;
	static int card = 1;

	public static void main(String[] args) throws Exception{
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		vortexNum = Integer.parseInt(st.nextToken());
		linkNum = Integer.parseInt(st.nextToken());
		cardPeople = new int[vortexNum];
		upperCnt = new int[vortexNum];
		lowerCnt = new int[vortexNum];
		
		int[] cntOfLink = new int[vortexNum+1];
		
		ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
		for(int inx=0; inx<vortexNum+1; inx++) {
			graph.add(new ArrayList<Integer>());
		}
		
		for(int inx=0; inx<linkNum; inx++) {
			st = new StringTokenizer(br.readLine(), " ");
			int v2 = Integer.parseInt(st.nextToken()); //후행 정점
			int v1 = Integer.parseInt(st.nextToken()); //선행 정점
			upperCnt[v2-1]++;
			lowerCnt[v1-1]++;
			
			if(v1==v2) {
				System.out.println(-1);
				return;
			}
			
			graph.get(v1).add(v2);                     //선행 정점에 후행하는 정점의 정보 추가
			cntOfLink[v2]++;                           //후행 정점에 대한 간선의 수 증가
		}
		
		try {
			topologicalSort(graph, cntOfLink);
		} catch(Exception e) {
			System.out.println(-1);
			return;
		}
	
		for(int inx = 0; inx < vortexNum; inx++) {
			System.out.print(cardPeople[inx]+" ");
		}
		System.out.println();

	}
	
	static void topologicalSort(ArrayList<ArrayList<Integer>> graph, int[] cntOfLink) throws Exception {
		PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>(); //minHeap으로 구현

		for(int inx=1; inx<vortexNum+1; inx++) {
			if(cntOfLink[inx]==0)
				minHeap.offer(inx);
		}
		
        for (int inx = 0; inx < vortexNum; inx++) {
            int v = minHeap.remove(); 
            
            if(upperCnt[v-1]-lowerCnt[v-1]+v != card) 
            	throw new Exception();
            
            cardPeople[v-1] = card++;

            for (int nextV : graph.get(v)) {
                cntOfLink[nextV]--; 

                if (cntOfLink[nextV] == 0) {
                	minHeap.offer(nextV);
                }
            }
        }
	}
}
