/* Implementing Quick Union with Path Compression
   Eager approach but it compresses the path by connecting nodes directly to node
   Worst Case time : N + M log N
   N = number of elements
   M = number of union find operations
 */

public class PathCompQU {
    int[] id;

    public PathCompQU(int n) {
        id = new int[n];
        for (int i = 0; i < n; i++) {
            id[i] = i;
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
        id[pid] = qid;
    }

    public static void main(String[] args) {
        PathCompQU pqu = new PathCompQU(7);
        pqu.union(1, 3);
        pqu.union(2, 3);
        pqu.union(5, 6);
        pqu.union(6, 3);
        if (pqu.connected(1, 6)) {
            StdOut.print("Are connected");
        }
    }
}
