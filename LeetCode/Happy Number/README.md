https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number ***n*** is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1. Those numbers for which this process **ends in 1** are happy numbers.

Return True if ***n*** is a happy number, and False if not.

**Example**: 

~~~
Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
~~~

----

각 자리수를 제곱해서 다시 더하기함. 영원히 돌려서, 1이 나오면 true, 아니면 false