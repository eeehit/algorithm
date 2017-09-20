import java.util.ArrayList;
import java.util.Arrays;

class Divisible {
	public int[] divisible(int[] array, int divisor) {
		//ret에 array에 포함된 정수중, divisor로 나누어 떨어지는 숫자를 순서대로 넣으세요.
    ArrayList<Integer> ret = new ArrayList<>();
    for(int number: array) {
    	if (number%divisor == 0) {
      	ret.add(number);
      }
    }
		return ret.stream().mapToInt(i -> i).toArray();
	}
	// 아래는 테스트로 출력해 보기 위한 코드입니다.
	public static void main(String[] args) {
		Divisible div = new Divisible();
		int[] array = {5, 9, 7, 10};
		System.out.println( Arrays.toString( div.divisible(array, 5) ));
	}
}
