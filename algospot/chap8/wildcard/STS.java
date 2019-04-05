package apss.chap08.wildcard;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	
	static int N = 0;
	static String pattern;
	static String inputString;
	static int[][] cache = null;
	static PriorityQueue<String> strings = null;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int T = Integer.parseInt(st.nextToken());
		
		for(int inx=0; inx<T; inx++) {
			pattern = new StringTokenizer(br.readLine(), " ").nextToken();
			N = Integer.parseInt(new StringTokenizer(br.readLine(), " ").nextToken());
			strings = 
				new PriorityQueue<String>(N,new Comparator<String>() {
				@Override
				public int compare(String s1, String s2) {
					for(int jnx=0; jnx<s1.length(); jnx++) {
						if(s1.charAt(jnx) < s2.charAt(jnx)) return -1;
						else if(s1.charAt(jnx) > s2.charAt(jnx)) return 1;
					}
					return 0;
				}
	        });
				
			for(int jnx=0; jnx<N; jnx++) {
				inputString = new StringTokenizer(br.readLine(), " ").nextToken();
				cache = new int[pattern.length()+1][inputString.length()+1];
				
				int result = match(0,0);
				
				if(result==1) strings.offer(inputString);
			}
			
			while(!strings.isEmpty())
				System.out.println(strings.poll());
		}

	}
	
	public static int match(int patternInx, int inputInx) {
		if(cache[patternInx][inputInx]!=0) return cache[patternInx][inputInx];
		
		while(patternInx<pattern.length() && inputInx<inputString.length() 
				&& ((pattern.charAt(patternInx) == '?') || (pattern.charAt(patternInx)==inputString.charAt(inputInx)))) {
			patternInx++;
			inputInx++;
		}
		
		if(patternInx == pattern.length()) {
			if(inputInx == inputString.length()) return cache[patternInx][inputInx] = 1;
			else return cache[patternInx][inputInx] = -1;	
		}
		
		if(pattern.charAt(patternInx) == '*') {
			for(int skip=0; skip+inputInx <=inputString.length(); skip++) 
				if(match(patternInx+1,skip+inputInx)==1) return cache[patternInx][inputInx] = 1;
		}
		
		return cache[patternInx][inputInx] = -1;
	}

}
