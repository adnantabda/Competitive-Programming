import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# DSU implementation
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True

t = int(input())
results = []
for _ in range(t):
    n = int(input())
    # read original permutation p (1-indexed values)
    p = list(map(int, input().split()))
    # read removal order d (1-indexed positions)
    d = list(map(int, input().split()))
    # convert d to 0-indexed
    d = [x-1 for x in d]
    
    # Precompute inverse of p:
    # For each number v from 1 to n, let inv[v-1] be the index i such that p[i]==v.
    inv = [-1]*n
    for i in range(n):
        inv[p[i]-1] = i

    # We will process queries in reverse.
    # At a given reverse state, "restored" indices are those not removed.
    # Initially, all indices are removed (i.e. b[i] == 0) so answer = n.
    ans = [0]*(n+1)
    ans[0] = n  # state with 0 restored -> all zeros → need to fix all n positions.
    
    added = [False]*n  # whether index i has been restored
    dsu = DSU(n)
    R = 0  # number of restored indices
    # Let comp be the number of DSU components among restored indices.
    comp = 0  
    # Let E = R - comp, the extra edges (cycle count) discovered so far.
    
    # Process queries in reverse order:
    # reverse_state[i] will be the answer after i indices have been restored,
    # which corresponds to the forward state before the (n-i)-th removal.
    for i in range(n):
        x = d[i]  # x is the index that is being restored now (in reverse)
        added[x] = True
        R += 1
        comp += 1  # new index starts as its own component
        # When we restore index x, try to union with its two “neighbors” in the permutation graph.
        # 1. If p[x] is not already x+1 (i.e. x wasn’t originally fixed)
        #    and if the index corresponding to p[x] (i.e. p[x]-1) is already restored,
        #    then union x and (p[x]-1).
        if p[x] != x+1:  # if index x was not originally fixed
            y = p[x]-1
            if added[y]:
                if dsu.union(x, y):
                    comp -= 1
        # 2. Also, if there is an index j with p[j] == x+1 (i.e. x appears in the permutation),
        #    and if that index is restored, union x and j.
        j = inv[x]  # index j such that p[j] == x+1
        if j != -1 and added[j]:
            if p[j] != j+1:  # only consider j if it was not originally fixed
                if dsu.union(x, j):
                    comp -= 1
        # Now the extra saved operations (E) among restored indices equals R - comp.
        E = R - comp
        # And the number of still–removed indices is Z = n - R.
        Z = n - R
        # The answer (minimum operations needed) is:
        #   ops = Z + E.
        ops = Z + E
        ans[i+1] = ops
    # The reverse processing produced answers for states with 0,1,...,n restored.
    # In the forward process, after j queries (j removals) the state corresponds to
    # the reverse state with R = n - j restored.
    # So we output ans in reverse order (skipping the state where 0 queries were made).
    out = []
    for j in range(1, n+1):
        out.append(str(ans[n - j]))
    results.append(" ".join(out))
    
sys.stdout.write("\n".join(results))
