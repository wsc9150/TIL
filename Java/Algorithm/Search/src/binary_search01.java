// binary search
// ���� �˻�
// ���ĵǾ� �ִ� �迭���� ��� ����
// �迭�� ��� ���Ҹ� ã�� ��
// �˻��ϴ� ���Ұ� ���� �� ������ ���� ����, �� ũ�� ���� �������� �ٽ� ��� ���Ҹ� ã�� ��
// ���� ������ �˻� ������ �ݾ� �پ��� �ȴ�. -> ���� �˻����� ���� �˻� ����

import java.util.Scanner;

public class binary_search01 {

	public static void main(String[] args) {
		int[] x = {1, 2, 3, 5, 7, 8, 9};
		Scanner s = new Scanner(System.in);

		int k = s.nextInt();
		int idx = bin_search(x, k);

		if (idx == -1)
			System.out.println("�˻����� ���� ���Ұ� �������� �ʽ��ϴ�.");
		else
			System.out.println("�˻����� x[" + idx + "]�� �ֽ��ϴ�.");

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
