# Trapping Rain Water
"""
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
def trap(height):
    # Ven
    s1, s2 = 0, 0
    max1, max2 = 0, 0
    for i in range(len(height)):
        if height[i] > max1:
            max1 = height[i]
        s1 += max1

        if height[len(height)-i-1] > max2:
            max2 = height[len(height)-i-1]
        s2 += max2
    # s = s1+s2-rect-vol
    s = s1+s2-max1*len(height)-sum(height)
    return s

def trap2(height):
    # pointer
    # find the peak index
    peak_index = 0
    for i in range(len(height)):
        if height[i] > height[peak_index]:
            peak_index = i
    
    # set the leftmost bar
    left_most_bar = 0
    water = 0
    for i in range(peak_index):
        if height[i] > left_most_bar:
            left_most_bar = height[i]
        else:
            # water = min(leftmost, peak) - height[i]
            water += left_most_bar - height[i]

    right_most_bar = 0
    for i in range(len(height)-1, peak_index, -1):
        if height[i] > right_most_bar:
            right_most_bar = height[i]
        else:
            water += right_most_bar - height[i]
    return water

print(trap2([0,1,0,2,1,0,1,3,2,1,2,1]))