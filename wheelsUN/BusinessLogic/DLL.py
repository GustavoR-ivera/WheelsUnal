from BusinessLogic.Node import Node


class DLL():
    def __init__(self):
        self.head = None

    #  This code is contributed by jatinreaper
    # Add a node at the end of the DLL
    def append(self, new_data):

        # 1. allocate node
        # 2. put in the data
        new_node = Node(data=new_data)
        # 3. This new node is going to be the
        # last node, so make next of it as NULL
        new_node.next = None

        # 4. If the Linked List is empty, then
        #  make the new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            # last will be the tail of the list
            last = self.head
            # 5. Else traverse till the last node
            while (last.next is not None):
                last = last.next

            # 6. Change the next of last node
            last.next = new_node
            # 7. Make last node as previous of new node */
            new_node.prev = last

    # Given a node as prev_node, insert
    # a new node after the given node
    def insertAfter(self, current_node, new_data):

        # 1. allocate node  &
        # 2. put in the data
        new_node = Node(data=new_data)

        # 3. Make next of new node as next of prev_node
        #new_node.next = prev_node.next
        new_node.next = None

        # quitar la referencia del nodo sig a prev_node
        current_node.next.prev = None

        # 4. Make the next of prev_node as new_node
        current_node.next = new_node

        # 5. Make prev_node as previous of new_node
        new_node.prev = current_node

    def getTail(self):
        n = self.head
        flag = True
        while (flag):
            if n.next == None:
                flag = False
            else:
                n = n.next
        return n


if __name__ == "__main__":
    l = DLL()
    l.append("home")

    # td = l.head.next.next.next.next

    # l.insertAfter(td, "new section")

    n = l.head
    flag = True
    while (flag):
        print(n.data)
        if n.next == None:
            flag = False
        else:
            n = n.next

