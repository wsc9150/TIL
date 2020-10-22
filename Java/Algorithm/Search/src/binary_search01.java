// binary search
// 이진 검색
// 정렬되어 있는 배열에서 사용 가능
// 배열의 가운데 원소를 찾아 비교
// 검색하는 원소가 값이 더 작으면 앞쪽 범위, 더 크면 뒤쪽 범위에서 다시 가운데 원소를 찾아 비교
// 비교할 때마다 검색 범위가 반씩 줄어들게 된다. -> 선형 검색보다 빠른 검색 가능

import java.util.Scanner;

public class binary_search01 {

	public static void main(String[] args) {
		int[] x = {1, 2, 3, 5, 7, 8, 9};
		Scanner s = new Scanner(System.in);

		int k = s.nextInt();
		int idx = bin_search(x, k);

		if (idx == -1)
			System.out.println("검색값을 갖는 원소가 존재하지 않습니다.");
		else
			System.out.println("검색값은 x[" + idx + "]에 있습니다.");

	}

	public static int bin_search(int[] a, int key) {
		int pl = 0;
		int pr = a.length - 1;
		
		while (true) {
			int pc = (pl + pr) / 2;
			
			if (a[pc] == key)
				return pc;
			else if (a[pc] < key)
				pl = pc + 1;
			else
				pr = pc - 1;
			
			if (pl > pr)
				break;
		}

		return -1;
	}

}
