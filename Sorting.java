public class Main{

	public static void main(String [] args){
    int[] list = {6,5,4,3,2,1};
    Main.printArray("input: ",list);
    int[] res = new int[list.length];
    System.arraycopy(list,0,res,0,list.length);
    bubblesort(res, res.length);
    printArray("bubblesort: ", res);
    printArray("input: ",list);
    printArray("mergesort: ", mergesort(list));

  }



  public static void bubblesort(int[] A, int n){
    if ( n == 0 ) return;
    int m = 0;
    for (int i=0; i<n-1; i++){
      if(A[i] > A[i+1]){
        int temp = A[i];
        A[i] = A[i+1];
        A[i+1] = temp;
        m = i+1;
      }
    }
    bubblesort(A, m);
  }

  public static int[] mergesort(int[] A){
    if (A.length == 1)
      return A;
    int n = A.length;
    //create the 2 arrays
    int[] left = new int[n/2];
    int lenR = n%2 == 0 ? n/2 : n/2+1;
    int[] right = new int[lenR];
    //set the middle
    int m = n/2;
    //split the array into left and right :) easy
    for (int i=0; i<n; i++){
      if (i<m)
        left[i] = A[i];
      else
        right[i-m] = A[i];
    }
    mergesort(left);
    mergesort(right);
    return merge(left,right);
  }

  //compare the first element of both lists and put the lowest in the result
  //i can use 2 queue
  public static int[] merge(int[] left, int[] right){
    int lenRes = left.length+right.length;
    int[] res = new int[lenRes];
    int leftP = 0;
    int rightP = 0;
    printArray("left: ",left);
    printArray("right: ", right);
    //fill in the result with the lowest element you see
    int i = 0;
    while(rightP < right.length && leftP < left.length){
        if(left[leftP] < right[rightP]){
          System.out.println("aggiungoL "+left[leftP] +" in pos "+i);
          res[i] = left[leftP];
          leftP++;
        }
        else {
          System.out.println("aggiungoR "+right[rightP]+ " in pos "+i );
          res[i] = right[rightP];
          rightP++;
        }
        i++;
    }
    //add the remain element if the 2 halves are not the same lenght
    while(leftP < left.length){
      System.out.println("aggiungoL elemento in pos "+leftP+" che sarebbe "+left[leftP]);
      res[i] = left[leftP];
      i++;
      leftP++;
    }

    while(rightP < right.length){
      System.out.println("aggiungoR elemento in pos "+rightP+" che sarebbe "+right[rightP]);
      res[i] = right[rightP];
      rightP++;
      i++;
    }
    printArray("res: ", res);
    return res;
  }

  public static void printArray(String s, int[] A){
    int l = A.length;
    System.out.print(s+"[");
    for (int i=0; i<l-1; i++){
      System.out.print(A[i]+" ");
    }
    System.out.print(A[l-1]+"]\n");
  }
}
