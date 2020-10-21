import java.util.*;

public class linear_search01 {

	public static void main(String[] args) {
		int[] x = {6, 4, 3, 2, 1, 2, 8};
		Scanner s = new Scanner(System.in);
		
		int k = s.nextInt();
		
		int idx = seq_search(x, k);
		
		if (idx == -1) 
			System.out.println("검색값을 갖는 원소가 존재하지 않습니다.");
		else
			System.out.println("검색값은 x[" + idx + "]에 있습니다.");
	}
	
	public static int seq_search(int []a, int key) {
		int idx = 0;
		
		while (true) {
			if (a[idx] == key) {
				return idx;
			}
			
			if (idx == a.length) {
				return -1;
			}
			
			idx += 1;
		}
	}

}
