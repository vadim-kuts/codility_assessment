def solution(blocks):
    lb = len(blocks)
    if lb >= 2 and lb <= 200000:
        res = 0
        for i in range(lb):
            if blocks[i] >= 1 and blocks[i] <= 1000000000:
                j = i
                while j < lb-1 and blocks[j+1] >= blocks[j]:
                    j += 1
                h = j
                j = i
                while j > 0 and blocks[j-1] >= blocks[j]:
                    j -= 1
                l = j
                res = max(res, h - l + 1 )
        return res
