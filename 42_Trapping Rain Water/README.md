# Note
 _s1_ 
```diff
! `韦恩图`
https://leetcode-cn.com/problems/trapping-rain-water/solution/wei-en-tu-jie-fa-zui-jian-dan-yi-dong-10xing-jie-j/
S1 + S2会覆盖整个矩形，并且：重复面积 = 柱子面积 + 积水面积
积水面积 = S1 + S2 - 矩形面积 - 柱子面积
```
 _s2_ 
```diff
! `指针`
step1: 找到最高bar的index
step2：设置左边最高的bar高度为0
       遍历，如果height[i] > leftmostbar: 更新leftmostbar
       water += leftmostbar-height[i]
step3: 重复设置右边bar
```