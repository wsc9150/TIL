// while ��� for ���

import java.util.*;

public class linear_search02 {

	public static void main(String[] args) {
		int[] x = {6, 4, 3, 2, 1, 2, 8};
		Scanner s = new Scanner(System.in);
		
		int k = s.nextInt();
		int idx = seq_search(x, k);
		
		if (idx == -1) 
			System.out.println("�˻����� ���� ���Ұ� �������� �ʽ��ϴ�.");
		else
			System.out.println("�˻����� x[" + idx + "]�� �ֽ��ϴ�.");
	}
	
	public static int seq_search(int []a, int key) {
		
		for (int i = 0; i < a.length; i++) 
			if (a[i] == key)
				return i;
		
		return -1;
	}
}
