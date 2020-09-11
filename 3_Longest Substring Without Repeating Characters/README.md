# Note
 _s1_ 
```diff
! `滑动窗口`

  int left = 0, right = 0;

  while (right < s.size()) {
      window.add(s[right]);
      right++;

      while (valid) {
          window.remove(s[left]);
          left++;
      }
  }；
```
