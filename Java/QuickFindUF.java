/* Implementation of QuickFind on UF Data Structure
    Eager or basic approach
    Worst Case time : M N
    N = number of elements
    M = number of union find operations
 */

public class QuickFindUF {
    private int[] id;

    private QuickFindUF(int N) {
        id = new int[N];
        for (int i = 0; i < N; i++) {
            id[i] = i;
        }
    }

    public boolean connected(int p, int q) {
        return id[p] == id[q];
    }

    public void union(int p, int q) {
        // Takes n^2 array accesses to execute n union commands on n array elements. (Very Expensive)
        int pid = id[p];
        int qid = id[q];
        for (int i = 0; i < id.length; i++) {
            if (id[i] == pid) {
                id[i] = qid;
            }
        }
    }

    public static void main(String[] args) {
        QuickFindUF qf = new QuickFindUF(3);
    }


}
