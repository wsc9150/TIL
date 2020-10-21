// sentinel method
// ���ʹ�
// �˻��ϰ��� �ϴ� Ű���� �迭�� �� ���� ����
// �̶� �����ϴ� ���� ����(sentinel)��� �Ѵ�.

import java.util.*;

public class linear_search05 {

	public static void main(String[] args) {
		ArrayList<Integer> arr = new ArrayList<>(Arrays.asList(6, 4, 3, 2, 1, 2, 8));
		Scanner s = new Scanner(System.in);
		
		int k = s.nextInt();
		int idx = seq_search(arr, k);
		
		if (idx == -1)
			System.out.println("�˻����� ���� ���Ұ� �������� �ʽ��ϴ�.");
		else
			System.out.println("�˻����� x[" + idx + "]�� �ֽ��ϴ�.");
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
