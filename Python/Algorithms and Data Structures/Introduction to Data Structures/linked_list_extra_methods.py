from linked_list import *

def delete_at_index(self, index):
    """
    Deletes the Node at index position
    Deletion takes 0(1) time but finding the node to delete takes O(n) time.

    Takes overall O(n) time
    """
    if index == 0:
        self.head = self.head.next_node

    if index > 0:
        position = index
        current = self.head

        while position > 1:
            current = current.next_node
            position -= 1

        prev_node = current
        deleted_node = current.next_node

        prev_node.next_node = deleted_node.next_node


def node_at_index(self, index):
    """
    Returns the Node at index position
    Takes O(n) time
    """

    if index == 0:
        return self.head

    if index > 0:
        position = index
        current = self.head

        while position > 0:
            current = current.next_node
            position -= 1

        return current

    return


LinkedList.node_at_index = node_at_index
LinkedList.delete_at_index = delete_at_index
