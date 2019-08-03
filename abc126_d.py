# cf. https://atcoder.jp/contests/abc126/submissions/5451729
import sys

N = int(input())
nodes = [set() for _ in range(N)]
for line in sys.stdin:
    u, v, w = map(int, line.split())
    u, v = (u - 1, v - 1)
    nodes[u].add((v, w))
    nodes[v].add((u, w))
    # 各要素には繋がっている先のノード番号と距離のタプルの集合が入る

ans = [-1 for _ in range(N)]
q = [(0, 0, -1)]  # 相手の頂点(v), 0番ノードからの距離(dist), 探索元ノード(parent)の初期化

while q:
    v, dist, parent = q.pop()  # 最後にappendされたものを取り出すので、深さ優先でたどっていることになる

    # m番ノードからn番ノードまでの距離をdist(m, n)とするとき、
    # 任意のノードx, y、および 0番からx, yへそれぞれ辿った時の分岐点(branch)となるあるノードbについて
    #
    # dist(x, y) = dist(b, x) + dist(b, y) = (dist(0, x) - dist(0, b)) + (dist(0, y) - dist(0, b))
    #            = dist(0, x) + dist(0, y) - 2 * dist(0, b)
    #
    # すなわちdist(x, y)の偶奇は0番ノードからの距離の和によって定まる。
    # 0番とx番、0番とy番について条件を満たすため x, yそれぞれの色を0番からの距離の偶奇によって定めると、
    # 奇奇 or 偶偶のときx, yは同色で、かつdist(x, y)は偶数となり「x, yの色が同一 ⇔ dist(x, y)は偶数」という条件を満たしている。
    if dist % 2 == 0:
        ans[v] = 0
    else:
        ans[v] = 1

    for u, w in nodes[v]:  # 相手のノードから伸びている辺(接続先u, 距離w)それぞれについて...
        if u == parent:
            continue  # この辺の接続先は今しがた辿ってきたノードなので不要、appendせず次のループへ

        q.append((u, dist + w, v))  # 相手の頂点, 距離, 探索元ノード

print("\n".join(map(str, ans)))
