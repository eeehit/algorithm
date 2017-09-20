import java.util.*;

public class GetMinMaxString {
    public String getMinMaxString(String str) {
      	String[] numberStr = str.split(" ");
      	int[] numberInt = new int[numberStr.length];
      
        int i = 0;
      	for (String number: numberStr) {
          numberInt[i] = Integer.parseInt(number);
          i = i+1;
        }
      	Arrays.sort(numberInt);
      
        return numberInt[0] + " " + numberInt[numberInt.length-1];
    }

    public static void main(String[] args) {
        String str = "1 2 3 4";
        GetMinMaxString minMax = new GetMinMaxString();
        //아래는 테스트로 출력해 보기 위한 코드입니다.
        System.out.println("최대값과 최소값은?" + minMax.getMinMaxString(str));
    }
}
