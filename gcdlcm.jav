import java.util.Arrays;

class TryHelloWorld {
    public int[] gcdlcm(int a, int b) {
        int[] answer = new int[2];
      	answer[0] = gcd(a, b);
      	answer[1] = lcm(a, b, answer[0]);
        return answer;
  	}
  	public int gcd(int a, int b) {
    		while (b != 0) {
        	int tmp = a % b;
					a = b;
					b = tmp;
        }
    		return a;
    }
  	public int lcm(int a, int b, int gcd) {
    		return (int) a * b / gcd;
    }
    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String[] args) {
        TryHelloWorld c = new TryHelloWorld();
        System.out.println(Arrays.toString(c.gcdlcm(3, 12)));
    }
}
