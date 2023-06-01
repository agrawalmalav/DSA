''' 
    Following is the node structure

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

'''

def deleteAlternateNodes(head):
    # Write your code here
    curr = head

    if curr == None or curr.next == None:
        return curr

    curr.next = curr.next.next
    curr = curr.next
    head.next = deleteAlternateNodes(curr)
    return head
