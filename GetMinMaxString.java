public class GetMinMaxString {
    public String getMinMaxString(String str) {
      	String[] numberStr = str.split(" ");
      	int min = 0;
      	int max = 0;
      	int tmp = 0;
      
      	min = max = Integer.parseInt(numberStr[0]);
        for(int i=1 ; i<numberStr.length ; i++) {
      	  tmp = Integer.parseInt(numberStr[i]);
          if (tmp>max) {
          	max = tmp;
          } else if (tmp<min) {
          	min = tmp;
          }
        }
      
        return min + " " + max;
    }

    public static void main(String[] args) {
        String str = "1 2 3 4";
        GetMinMaxString minMax = new GetMinMaxString();
        //아래는 테스트로 출력해 보기 위한 코드입니다.
        System.out.println("최대값과 최소값은?" + minMax.getMinMaxString(str));
    }
}
