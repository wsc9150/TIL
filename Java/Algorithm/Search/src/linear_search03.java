// 실수 검색

import java.util.Scanner;

public class linear_search03 {

	public static void main(String[] args) {
		double[] x = {12.7, 3.14, 6.4, 7.2};
		Scanner s = new Scanner(System.in);
		
		double k = s.nextDouble();
		int idx = seq_search(x, k);
		
		if (idx == -1) 
			System.out.println("검색값을 갖는 원소가 존재하지 않습니다.");
		else
			System.out.println("검색값은 x[" + idx + "]에 있습니다.");
	}
	
	public static int seq_search(double []a, double key) {
		
		for (int i = 0; i < a.length; i++) 
			if (a[i] == key)
				return i;
		
		return -1;
	}

}
