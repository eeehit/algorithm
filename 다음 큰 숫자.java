//다음 큰 숫자
//Level 3
//어떤 수 N(1≤N≤1,000,000) 이 주어졌을 때, N의 다음 큰 숫자는 다음과 같습니다.
//N의 다음 큰 숫자는 N을 2진수로 바꾸었을 때의 1의 개수와 같은 개수로 이루어진 수입니다.
//1번째 조건을 만족하는 숫자들 중 N보다 큰 수 중에서 가장 작은 숫자를 찾아야 합니다.
//예를 들어, 78을 2진수로 바꾸면 1001110 이며, 78의 다음 큰 숫자는 83으로 2진수는 1010011 입니다.
//N이 주어질 때, N의 다음 큰 숫자를 찾는 nextBigNumber 함수를 완성하세요.

import java.nio.ByteBuffer;
import java.nio.ByteOrder;

class TryHelloWorld {
  public int nextBigNumber(int n) {
    int answer = n+1;
    int nCount = bitCount(Integer.toBinaryString(n));
    
    while (true) {
      if (bitCount(Integer.toBinaryString(answer)) == nCount)	break;
      answer = answer+1;
    }
    return answer;
  }
  public int bitCount(String s) {
    int count = 0;
    char[] cArr = s.toCharArray();
    for(char c : cArr) {
      if (c == '1') {
        count = count+1;
      }
    }
    return count;
  }
  public static void main(String[] args) {
    TryHelloWorld test = new TryHelloWorld();
    int n = 78;
    System.out.println(test.nextBigNumber(n));
  }
}
