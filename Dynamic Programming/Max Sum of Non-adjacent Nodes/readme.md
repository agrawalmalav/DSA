 Maximum sum of non-adjacent elements
Send Feedback
You are given an array/list of ‘N’ integers. You are supposed to return the maximum sum of the subsequence with the constraint that no two elements are adjacent in the given array/list.
Note:

A subsequence of an array/list is obtained by deleting some number of elements (can be zero) from the array/list, leaving the remaining elements in their original order.

Input format:

The first line contains a single integer ‘T’ denoting the number of test cases.

The first line of each test case contains a single integer ‘N’ denoting the number of elements in the array.

The second line contains ‘N’ single space-separated integers denoting the elements of the array/list.

Output format:

For each test case, print a single integer that denotes the maximum sum of the non-adjacent elements.

Print the output of each test case in a separate line.

Note:

You do not need to print anything; it has already been taken care of. Just implement the given function.

Constraints:

1 <= T <= 500
1 <= N <= 1000
0 <= ARR[i] <= 10^5

Where 'ARR[i]' denotes the 'i-th' element in the array/list.

Time Limit: 1 sec.

Sample Input 1:

2
3
1 2 4
4
2 1 4 9

Sample Output 1:

5
11

Explanation to Sample Output 1:

In test case 1, the sum of 'ARR[0]' & 'ARR[2]' is 5 which is greater than 'ARR[1]' which is 2 so the answer is 5.

In test case 2, the sum of 'ARR[0]' and 'ARR[2]' is 6, the sum of 'ARR[1]' and 'ARR[3]' is 10, and the sum of 'ARR[0]' and 'ARR[3]' is 11. So if we take the sum of 'ARR[0]' and 'ARR[3]', it will give the maximum sum of sequence in which no elements are adjacent in the given array/list.

Sample Input 2:

2
5
1 2 3 5 4
9
1 2 3 1 3 5 8 1 9

Sample Output 2:

8
24

Explanation to Sample Output 2:

In test case 1, out of all the possibilities, if we take the sum of 'ARR[0]', 'ARR[2]' and 'ARR[4]', i.e. 8, it will give the maximum sum of sequence in which no elements are adjacent in the given array/list.

In test case 2, out of all the possibilities, if we take the sum of 'ARR[0]', 'ARR[2]', 'ARR[4]', 'ARR[6]' and 'ARR[8]', i.e. 24 so, it will give the maximum sum of sequence in which no elements are adjacent in the given array/list.

