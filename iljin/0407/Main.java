package algorithm2;
import java.lang.*;
import java.io.*;
import java.util.*;

/*
 */

public class Main {

	static int M, N, L;
	static ArrayList<Animal> animal;
	static int sniper [];
	static int answer;
	
	public static void main(String [] args) throws IOException {
		
		Scanner sc = new Scanner(System.in);
		M = sc.nextInt();
		N = sc.nextInt();
		L = sc.nextInt();
		sniper = new int[M+1];	
		animal = new ArrayList<Animal>();
		answer = 0;
		
		for(int i=1;i<=M;i++) {
			sniper[i] = sc.nextInt();
		}
		Arrays.sort(sniper);
		
		for(int i=1;i<=N;i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			if(y>L) continue;
			else animal.add(new Animal(x,y));
		}
		
		Collections.sort(animal);
		
		int animalIdx = 0;
		int sniperIdx = 0;
		
		//for(int a : sniper) System.out.println(a);
		
		while(animalIdx<animal.size()) {
			
			Animal ani = animal.get(animalIdx);
			
			if(sniperIdx<M) {
				while(sniperIdx<M && sniper[sniperIdx+1] < ani.x) {
					sniperIdx++;
				}
			}
			if(sniperIdx!=0 && L >= (ani.x-sniper[sniperIdx]+ani.y)) {
				answer++;
				//System.out.println(ani.x+" "+ani.y);
			}
			else if(sniperIdx<M) {
				if(L >= (sniper[sniperIdx+1]-ani.x+ani.y)) {
					answer++;
					//System.out.println(ani.x+" "+ani.y);
				}
			}
			
			animalIdx++;
		}
		System.out.println(answer);
	}

}

class Animal implements Comparable<Animal>{
	int x;
	int y;
	Animal(int x, int y){
		this.x = x;
		this.y = y;
	}
	
	@Override
	public int compareTo(Animal o) {
		if(this.x>o.x) return 1;
		else if(this.x<o.x) return -1;
		else return 0;
	}
}