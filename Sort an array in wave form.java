public class Solution {

 

    public static int[] waveFormArray(int[] arr, int n) {

        // Write your code here.

        for (int i = 1; i < n; i+=2) {

            if(arr[i]>arr[i-1]){

                swap(arr, i, i-1);

            }

            if(i<n-1 && arr[i]>arr[i+1]){

                swap(arr, i, i+1);

            }

 

            

        }

        return arr;

    }

 

    private static void swap(int[] arr, int i, int j){

        int temp = arr[i];

        arr[i] = arr[j];

        arr[j]=temp;

    }

 

}

 
