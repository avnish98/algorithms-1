/* Implementation of Quick Union on UF data structure
    Lazy approach : A tree with children having same value as root
    Worst Case time : M N
    N = number of elements
    M = number of union find operations
 */

public class QuickUnion {
    int[] id;

    public QuickUnion(int n) {
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
        QuickUnion qu = new QuickUnion(6);
        qu.union(1, 3);
        qu.union(2, 6);
        qu.connected(1, 3);
    }

}
