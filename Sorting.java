public class Main{

	public static void main(String [] args){
    int[] list = {8,7,6,5,4};
    Main.printArray("input: ",list);
    int[] res = Main.bubblesort(list, 4);
    Main.printArray("bubblesort: ", res);
  }

  public static void printArray(String s, int[] A){
    int l = A.length;
    System.out.print(s+"[");
    for (int i=0; i<l-1; i++){
      System.out.print(A[i]+" ");
    }
    System.out.print(A[l-1]+"]\n");
  }

  public static int[] bubblesort(int[] A, int n){
    if ( n == 0 )
      return A;
    int m = 0;
    for (int i=0; i<n; i++){
      if(A[i] > A[i+1]){
        int temp = A[i];
        A[i] = A[i+1];
        A[i+1] = temp;
        m = i;
      }
    }
    //System.out.println("m: "+m);
    return bubblesort(A, m);
  }

}
