/*
    Implementation of Union Find Structure
    Find : Connects two elements
    Connected : Return true if connected
*/

public class UF {

    private int[] arr;
    private int size;

    UF(int n) {
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = i;
        }
        size = n;
    }

    void union(int p, int q) {
        arr[p] = arr[q];
    }

    boolean connected(int p, int q) {
        if (arr[p] == arr[q]) {
            return true;
        }
        return false;
    }

    int find(int n) {
        for (int i = 0; i < size; i++) {
            if (arr[i] == n) {
                return i;
            }
        }
        return -1;
    }

    int count() {
        int counter = 0;
        for (int i = 0; i < size; i++) {
            counter++;
        }
        return counter;
    }

    public static void main(String[] args) {
        int N = StdIn.readInt();
        UF uf = new UF(N);
        while (!StdIn.isEmpty()) {
            int p = StdIn.readInt();
            int q = StdIn.readInt();

            // If not connected then connect and print out values
            if (!uf.connected(p, q)) {
                uf.union(p, q);
                StdOut.print(p + " " + q);
            }
        }
    }

}
