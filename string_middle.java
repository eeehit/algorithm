class StringExercise{
    String getMiddle(String str){
      int start = (int) (str.length()-1)/2;
      int end = Math.round((str.length())/2) + 1;
    	return str.substring(start, end);
    }
    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void  main(String[] args){
        StringExercise se = new StringExercise();
        System.out.println(se.getMiddle("test"));
    }
}
