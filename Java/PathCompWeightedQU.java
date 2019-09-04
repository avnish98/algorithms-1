/* Implementing Path Compressed Weighted Quick Union
   After computing root of p set each node to point at root of p
   Worst Case time : N + M log* N
   N = number of elements
   M = number of union find operations
   Log* N = iterate log function i.e. How many times you have to take log to reach N
 */

public class PathCompWeightedQU {
    int[] id;
    int[] sz; // To count the number of elements rooted at a particular position

    public PathCompWeightedQU(int n) {
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
            // Sets node to point at root
            id[n] = id[id[n]];
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
        PathCompWeightedQU pqu = new PathCompWeightedQU(7);
        pqu.union(1, 3);
        pqu.union(2, 3);
        pqu.union(5, 6);
        pqu.union(6, 3);
        if (pqu.connected(1, 6)) {
            StdOut.print("Are connected");
        }
    }
}
