 Longest Palindromic Subsequence
Send Feedback
You have been given a string ‘A’ consisting of lower case English letters. Your task is to find the length of the longest palindromic subsequence in ‘A’.
A subsequence is a sequence generated from a string after deleting some or no characters of the string without changing the order of the remaining string characters. (i.e. “ace” is a subsequence of “abcde” while “aec” is not).
A string is said to be palindrome if the reverse of the string is the same as the actual string. For example, “abba” is a palindrome, but “abbc” is not a palindrome.
Input Format:

The first line of input contains an integer ‘T’ representing the number of test cases. Then the test cases follow.

The only line of each test case contains a single string ‘A’ consisting of only lowercase English letters.

Output Format:

For each test case, print a single integer denoting the length of the longest palindromic subsequence in string ‘A’.

The output for each test case is in a separate line.

Note:

You do not need to print anything, it has already been taken care of. Just implement the given function.

Constraints:

1 <= T <= 10
1 <= N <= 10 ^ 2

Where ‘T’ is the number of test cases, and ‘N’ is the length of the string.

Time limit: 1 sec.

Sample Input 1:

2
bbabcbcab
bbbab

Sample Output 1:

7
4

Explanation of Sample Input 1:

For the first test case, the longest palindromic subsequence is “babcbab”, which has a length of 7. “bbbbb” and “bbcbb” are also palindromic subsequences of the given string, but not the longest one.

For the second test case, the longest palindromic subsequence is “bbbb”, which has a length of 4.

Sample Input 2:

3
cbbd
bebeeed
abcd

Sample Output 2:

2
4
1

