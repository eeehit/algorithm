//소수 찾기
//Level 2
//numberOfPrime 메소드는 정수 n을 매개변수로 입력받습니다.
//1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하도록 numberOfPrime 메소드를 만들어 보세요.
//소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
//(1은 소수가 아닙니다.)
//10을 입력받았다면, 1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환
//5를 입력받았다면, 1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환

import java.util.*;

class NumOfPrime {
  int numberOfPrime(int n) {
    //init 
    //에라토스테네스의 체
    int p=2;
    ArrayList<Integer> arr = new ArrayList();
    for(int i=2 ; i<n+1 ; i++) {
      arr.add(i);
    }
    
    //proc
    while (Math.pow(p,2) <= n) {
      for(int i=0 ; i<arr.size() ; i++) {
        int num = arr.get(i);
        if (num%p == 0 && num!=p) {
          arr.remove(i);
        }
      }
      p = p+1;
    }
    
    //output
    return arr.size();
  }

	public static void main(String[] args) {
		NumOfPrime prime = new NumOfPrime();
		System.out.println( prime.numberOfPrime(10) );
	}

}
