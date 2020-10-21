// sentinel method
// 보초법
// 검색하고자 하는 키값을 배열의 맨 끝에 저장
// 이때 저장하는 값을 보초(sentinel)라고 한다.

import java.util.*;

public class linear_search05 {

	public static void main(String[] args) {
		ArrayList<Integer> arr = new ArrayList<>(Arrays.asList(6, 4, 3, 2, 1, 2, 8));
		Scanner s = new Scanner(System.in);
		
		int k = s.nextInt();
		int idx = seq_search(arr, k);
		
		if (idx == -1)
			System.out.println("검색값을 갖는 원소가 존재하지 않습니다.");
		else
			System.out.println("검색값은 x[" + idx + "]에 있습니다.");
	}

	public static int seq_search(ArrayList a, int key) {
		int i = 0;
		ArrayList<Integer> c = new ArrayList<>();
		
		c = (ArrayList<Integer>)a.clone();
		
		c.add(key);
		
		while (true) {
			if (c.get(i) == key)
				break;
			
			i++;
		}
		
		if (i == a.size())
			return -1;
		else
			return i;
	}

}
