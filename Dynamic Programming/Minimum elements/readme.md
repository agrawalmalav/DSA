 Minimum Elements
Send Feedback
You are given an array of ‘N’ distinct integers and an integer ‘X’ representing the target sum. You have to tell the minimum number of elements you have to take to reach the target sum ‘X’.
Note:

You have an infinite number of elements of each type.

For example

If N=3 and X=7 and array elements are [1,2,3]. 
Way 1 - You can take 4 elements  [2, 2, 2, 1] as 2 + 2 + 2 + 1 = 7.
Way 2 - You can take 3 elements  [3, 3, 1] as 3 + 3 + 1 = 7.
Here, you can see in Way 2 we have used 3 coins to reach the target sum of 7.
Hence the output is 3.

Input Format :

The first line of the input contains an integer, 'T’, denoting the number of test cases.

The first line of each test case will contain two space-separated integers ‘N’ and ‘X’, denoting the size of the array and the target sum.

The second line of each test case contains ‘N’ space-separated integers denoting elements of the array.

Output Format :

For each test case, print the minimum number of coins needed to reach the target sum ‘X’, if it's not possible to reach to target then print "-1".

Print a separate line for each test case.

Note :

You do not need to print anything, it has already been taken care of. Just implement the given function.

Constraints:

1 <= T <= 10
1 <= N <= 15
1 <= nums[i] <= (2^31) - 1
1 <= X <= 10000

All the elements of the “nums” array will be unique.
Time limit: 1 sec

Sample Input 1 :

2
3 7
1 2 3
1 0
1

Sample output 1 :

 3
 0

Explanation For Sample Output 1:

For the first test case,
Way 1 - You can take 4 elements  [2, 2, 2, 1] as 2 + 2 + 2 + 1 = 7.
Way 2 - You can take 3 elements  [3, 3, 1] as 3 + 3 + 1 = 7.
Here, you can see in Way 2 we have used 3 coins to reach the target sum of 7.
Hence the output is 3.

For the second test case,
Way 1 - You can take 3 elements  [1, 1, 1] as 1 + 1 + 1  = 3.
Way 2 - You can take 2 elements  [2, 1] as 2 + 1 = 3.
Here, you can see in Way 2 we have used 2 coins to reach the target sum of 7.
Hence the output is 2.

Sample Input 2 :

2
3 4
12 1 3
2 11
2 1

Sample output 2 :

2
6 

