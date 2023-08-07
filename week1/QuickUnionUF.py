## Quick Union
## Time complexity: O(N^2)

class QuickUnionUF:

    #set all numbers to be their own root
    def __init__(self: any, n: int) -> None:
        self.id = [i for i in range(n)]

    #find the root of the number
    def root(self, i: int):
        while i != self.id[i]:
            i = self.id[i]
        return i

    #check if two numbers are connected
    def connected(self, p: int, q: int):
        return self.root(p) == self.root(q)

    #connect two numbers
    def union(self, p: int, q: int):
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j

    def __str__(self):
        return str(self.id)


if __name__ == '__main__':
    uf = QuickUnionUF(10)
    print(uf)
    uf.union(4, 3)
    print(uf)
    uf.union(3, 8)
    print(uf)
    uf.union(6, 5)
    print(uf)
    uf.union(9, 4)
    print(uf)
    uf.union(2, 1)
    print(uf)
    print(uf.connected(8, 9))
    print(uf.connected(5, 0))
    uf.union(5, 0)
    print(uf)
    uf.union(7, 2)
    print(uf)
    uf.union(6, 1)
    print(uf)
    uf.union(7, 3)
    print(uf)