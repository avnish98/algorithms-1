/* Implementing Weighted Quick Union
   Placing small trees below tall trees to avoid longer trees
   Depth of any node is at most log N
   Worst Case time : N + M log N
   N = number of elements
   M = number of union find operations
 */

public class WeightedQU {
    int[] id;
    int[] sz; // To count the number of elements rooted at a particular position

    public WeightedQU(int n) {
        id = new int[n];
        sz = new int[n];
        for (int i = 0; i < n; i++) {
            id[i] = i;
            sz[i] = 0;
        }
    }

    public boolean connected(int p, int q) {
        return (root(p) == root(q));
    }

    public int root(int n) {
        while (id[n] != n) {
            n = id[n];
        }
        return id[n];
    }

    public void union(int p, int q) {
        int pid = id[p];
        int qid = id[q];
        if (pid == qid) {
            return;
        }

        // If elements rooted at p is less than elements rooted at q
        // then root the tree of p at q
        // and increment the size of tree of p with size of tree of q
        if (pid < qid) {
            id[p] = q;
            sz[q] += sz[p];
        } else {
            id[q] = p;
            sz[p] += sz[q];
        }
    }

    public static void main(String[] args) {
        WeightedQU wqu = new WeightedQU(7);
        wqu.union(1, 3);
        wqu.union(2, 3);
        wqu.union(5, 6);
        wqu.union(6, 3);
        if (wqu.connected(1, 6)) {
            StdOut.print("Are connected");
        }
    }
}
