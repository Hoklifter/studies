from linked_list import LinkedList
import linked_list_extra_methods

def verify(self):
    list_size = self.size()
    if list_size > 1:
        for i in range(1, list_size):
            previous = self.node_at_index(i-1).data
            current = self.node_at_index(i).data

            if previous > current:
                return False

    return True

LinkedList.verify = verify
