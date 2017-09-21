//가장 큰 정사각형 찾기
//Level 4
//O와 X로 채워진 표가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 표에서 O로 이루어진 가장 큰 정사각형을 찾아 넓이를 반환하는 findLargestSquare 함수를 완성하세요. 예를 들어

//1	2	3	4	5
//X	O	O	O	X
//X	O	O	O	O
//X	X	O	O	O
//X	X	O	O	O
//X	X	X	X	X
//가 있다면 정답은

//1	2	3	4	5
//X	O	O	O	X
//X	O	O	O	O
//X	X	O	O	O
//X	X	O	O	O
//X	X	X	X	X
//가 되며 넓이는 9가 되므로 9를 반환해 주면 됩니다.


import java.util.*;

class TryHelloWorld {
  public int findLargestSquare(char[][] board) {
    int answer = 1;
    archive(board, board.length);
    for(int n=board.length-1 ; n>=0 ; n--) {
      int count = checkEnd(board, n);
      System.out.println(count);
      if (count>=1) {
        answer = answer+1;
      }
      if (count<=1) {
        break;
      }
      archive(board, n);
    }
    
    return answer*answer;
  }
  public boolean findSquare(char s1, char s2, char s3, char s4) {
    return ((s1 == 'O') && (s2 == 'O') && (s3 == 'O') && (s4 == 'O'));
  }
  public void archive(char [][]board, int n) {
  	for(int i=0 ; i<n-1 ; i++) {
    	for(int j=0 ; j<n-1 ; j++) {
      	if (findSquare(board[i][j], board[i][j+1], board[i+1][j], board[i+1][j+1]) == true) {
          board[i][j] = 'O';
        } else {
          board[i][j] = 'X';
        }
      }
    }
  	for(int i=0 ; i<n ; i++) {
      board[i][n-1] = ' ';
      board[n-1][i] = ' ';
    }
    return ;
  }
  public int checkEnd(char[][] board, int n) {
  	int count = 0;
    for(int i=0 ; i<n ; i++) {
    	for(int j=0 ; j<n ; j++) {
      	if (board[i][j] == 'O') {
        	count = count+1;
        }
      }
    }
    return count;
  }
  public static void main(String[] args) {
    TryHelloWorld test = new TryHelloWorld();
    char [][]board ={
      {'X','O','O','O','X'},
      {'X','O','O','O','O'},
      {'X','X','O','O','O'},
      {'X','X','O','O','O'},
      {'X','X','X','X','X'}};
    System.out.println(test.findLargestSquare(board));
  }
}
