blocks = [int(input()) for i in range(int(input()))]
h, h0 = 0, 0
result = -1
for block in blocks:
    m = block // 65536
    r = (block - m * 65536)//256
    h = block - m * 65536 - r *256
    if h != (m + r + h0)*37 %256 or h >= 100:
        result = blocks.index(block)
        break
    h0 = h
print(result)
