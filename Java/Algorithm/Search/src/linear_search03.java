// �Ǽ� �˻�

import java.util.Scanner;

public class linear_search03 {

	public static void main(String[] args) {
		double[] x = {12.7, 3.14, 6.4, 7.2};
		Scanner s = new Scanner(System.in);
		
		double k = s.nextDouble();
		int idx = seq_search(x, k);
		
		if (idx == -1) 
			System.out.println("�˻����� ���� ���Ұ� �������� �ʽ��ϴ�.");
		else
			System.out.println("�˻����� x[" + idx + "]�� �ֽ��ϴ�.");
	}
	
	public static int seq_search(double []a, double key) {
		
		for (int i = 0; i < a.length; i++) 
			if (a[i] == key)
				return i;
		
		return -1;
	}

}
