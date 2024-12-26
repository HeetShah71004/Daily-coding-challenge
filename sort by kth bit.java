import java.util.ArrayList;

public class Solution {

    public static int[] sortArrayByKBit(int n, int k, int arr[]) {

     ArrayList<Integer> res = new ArrayList<Integer>();

        k--;

        for (int i = 0; i < n; i++) {

            if ((arr[i] & (1 << k)) == 0) {

                res.add(arr[i]);

            }

        }

        for (int i = 0; i < n; i++) {

            if ((arr[i] & (1 << k)) != 0) {

                res.add(arr[i]);

            }

        }

        int[] result = new int[n];

        for (int i = 0; i < n; i++) {

            result[i] = res.get(i);

        }

        return result;

    }

}
