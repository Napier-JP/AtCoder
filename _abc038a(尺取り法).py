N = int(input())
a = [int(num) for num in input().split()]
count = 0
left = 0
right = 0

while left <= N-1:
    while right < N-1 and a[right] < a[right+1]: #狭義単調増加
        right += 1 #次の要素、次の要素へと進む

    #a[right+1]が単調増加でなかったのでa[left]からa[right]までが単調増加と確定
    
    count += (right-left+1) #単調増加である部分列をleftからrightの範囲でカウント
    left += 1 #leftをrightに近づけていく。そのうちrightを追い越す
    
    if left > right: #追い越されたらrightをleftの位置まで持ってきて(つまり先のa[right+1])inner whileループを再開
        right = left

print(count)
