## Replace Node With Depth

For a given a Binary Tree of integers, replace each of its data with the depth of the tree.  
Root is at depth 0, hence the root data is updated with 0. Replicate the same further going down the in the depth of the given tree.  
The modified tree will be printed in the in-order fashion.  
Example:  

![image](https://github.com/agrawalmalav/DSA/assets/51107910/2b6ceba0-4313-4a7f-9f19-8bf3263fba70)


The above tree after updating will look like this:  

![image](https://github.com/agrawalmalav/DSA/assets/51107910/4c395dfd-9fe2-4c94-9125-9b68da2a1778)


Output: 2 1 2 0 2 1 2 (printed in the in-order fashion)  

## Input Format:

The first and the only line of input will contain the node data, all separated by a single space. Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.  

## Output Format:

The first and the only line of output prints the updated tree in the in-order fashion.  


## Constraints:  

1 <= N <= 10^5  
Where N is the total number of nodes in the binary tree.  

Time Limit: 1sec  

 ## Sample Input 1:
```
2 35 10 2 3 5 2 -1 -1 -1 -1 -1 -1 -1 -1 
```
## Sample Output 1:

2 1 2 0 2 1 2   

## Sample Input 2:
```
1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
```
## Sample Output 2:

2 1 2 0 2 1 2   

