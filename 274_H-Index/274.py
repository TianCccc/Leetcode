# H-index
"""
input: [3, 0, 6, 1, 5]
output: 3
"""
def hIndex_1(citations):
    # brute solution O(n^2)
    l = len(citations)
    n = 0
    for i in range(l+1):
        count = 0
        for j in range(l):
            if citations[j]>=i:
                count += 1
        if count >= i:
            n = max (n, i)
    return n

print(hIndex_1([3, 0, 6, 1, 5]))

def hIndex_2(citations):
    # sorting solution
    """
    |
    |   |
    |   |   
    |   |   |   
    |   |   |   
    |———|———|———|———|—
    """
    h = 0
    citations.sort(reverse = True)  #[6, 5, 3, 1, 0]
    l = len(citations)
    
    # Start with the largest number
    for i in range(l):
        #compare i with i's value
        if citations[i] >= i + 1 :
            h = i + 1
    return h

print(hIndex_2([3, 0, 6, 1, 5]))