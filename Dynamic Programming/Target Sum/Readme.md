 Target Sum
Send Feedback
You are given an array ‘ARR’ of ‘N’ integers and a target number, ‘TARGET’. Your task is to build an expression out of an array by adding one of the symbols '+' and '-' before each integer in an array, and then by concatenating all the integers, you want to achieve a target. You have to return the number of ways the target can be achieved.
For Example :

You are given the array ‘ARR’ = [1, 1, 1, 1, 1], ‘TARGET’ = 3. The number of ways this target can be achieved is:
1. -1 + 1 + 1 + 1 + 1 = 3
2. +1 - 1 + 1 + 1 + 1 = 3
3. +1 + 1 - 1 + 1 + 1 = 3
4. +1 + 1 + 1 - 1 + 1 = 3
5. +1 + 1 + 1 + 1 - 1 = 3
These are the 5 ways to make. Hence the answer is 5.

Input Format :

The first line of input contains a single integer ‘T’ representing the number of test cases.

The first line of each test case contains two space-separated integers ‘N’ and ‘TARGET’ representing the size of the given array and the target.

The second line of each test case contains ‘N’ space-separated integers representing the elements of the array.

Output Format :

For each test case, print a single integer representing the number of ways to form a target.

Print a separate line for each test case.

Constraints :

1 <= T <= 10
1 <= N <= 25
-1000 <= TARGET <= 1000
0 <= ARR[i] <= 1000

Time Limit: 1 sec

Note :

You do not need to print anything. It has already been taken care of. Just implement the given function.

Sample input 1 :

2
5 3
1 1 1 1 1
4 3
1 2 3 1

Sample Output 2 :

5
2

Explanation For Sample Input 1 :

For the first test case, ‘ARR’ = [1, 1, 1, 1, 1], ‘TARGET’ = 3. The number of ways this target can be achieved is:
1. -1 + 1 + 1 + 1 + 1 = 3
2. +1 - 1 + 1 + 1 + 1 = 3
3. +1 + 1 - 1 + 1 + 1 = 3
4. +1 + 1 + 1 - 1 + 1 = 3
5. +1 + 1 + 1 + 1 - 1 = 3
These are the 5 ways to get the target. Hence the answer is 5.

For the second test case, ‘ARR’ = [1, 2, 3, 1]. ‘TARGET’ = 3, The number of ways this target can be achieved is:
1. +1 - 2 + 1 + 3 = 3
2. -1 + 2 - 1 + 3 = 3
These are the 3 ways to get the target. Hence the answer is 2.

Sample Input 2 :

2
3 2
1 2 3
2 0
1 1

Sample Output 2 :

1
2

