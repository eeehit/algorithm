class Fibonacci {
	public long fibonacci(int num) {
		long c = 0;
    long a = 0;
    long b = 1;
    for(int i=2 ; i<num+1 ; i++) {
        c = a+b;
        a = b;
        b = c;
    }
    return c;
	}

  // 아래는 테스트로 출력해 보기 위한 코드입니다.
	public static void main(String[] args) {
		Fibonacci c = new Fibonacci();
		int testCase = 3;
		System.out.println(c.fibonacci(testCase));
	}
}
