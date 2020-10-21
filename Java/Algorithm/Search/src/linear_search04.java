import java.util.Arrays;
import java.util.Scanner;

public class linear_search04 {

	public static void main(String[] args) {
		String str1 = "string";
		String[] str2 = {"DTS", "AAC", "FLAC"};
		Scanner s = new Scanner(System.in);
		
		int idx1 = seq_search_str(str1, 'n');
		int idx2 = seq_search_strArr(str2, "DTS");

		System.out.println(str1 + "에서 \"n\"의 인덱스는 " + idx1 + "입니다.");
		System.out.println(Arrays.toString(str2) + "에서 \"DTS\"의 인덱스는 " + idx2 + "입니다.");
	}

	public static int seq_search_str(String a, char key) {

		for (int i = 0; i < a.length(); i++)
			if (a.charAt(i) == key)
				return i;

		return -1;
	}

	public static int seq_search_strArr(String[] a, String key) {

		for (int i = 0; i < a.length; i++)
			if (a[i] == key)
				return i;

		return -1;
	}

}
