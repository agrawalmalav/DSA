 Partition Equal Subset Sum
Send Feedback
You are given an array 'ARR' of 'N' positive integers. Your task is to find if we can partition the given array into two subsets such that the sum of elements in both subsets is equal.
For example, let’s say the given array is [2, 3, 3, 3, 4, 5], then the array can be partitioned as [2, 3, 5], and [3, 3, 4] with equal sum 10.
Follow Up:

Can you solve this using not more than O(S) extra space, where S is the sum of all elements of the given array?

Input Format:

The first line of input contains an integer 'T' representing the number of test cases or queries to be processed.
Then the test case follows.

The first line of each test case contains an integer 'N', denoting the size of the array.

The second line of each test case contains 'N' single space-separated integers representing the array elements.

Output Format:

For each test case, print “true” or “false” denoting whether we can partition into two equal subset-sum or not, in a separate line. 

Note:

You do not need to print anything; it has already been taken care of. Just implement the given function.

Constraints:

1 <= 'T' <= 10
1 <= 'N' <= 100 
1 <= 'ARR'[i] <= 100

Time Limit: 1 sec

Sample Input 1:

2
6
3 1 1 2 2 1
5
5 6 5 11 6

Sample Output 1:

true
false    

Explanation Of Sample Input 1:

For the first test case, the array can be partitioned as ([2,1,1,1] and [3, 2]) or ([2,2,1], and [1,1,3]) with sum 5.

For the second test case, the array can’t be partitioned.

Sample Input 2:

2
9
2 2 1 1 1 1 1 3 3
6
8 7 6 12 4 5

Sample Output 2:

false
true

