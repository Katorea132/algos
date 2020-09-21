class Node:
    """Nodes for a linked list, only contain a
    value, a next and a prev
    """
    def __init__(self, value=0):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    """Class for both singly and doubly linked lists
    """

    def __init__(self, is_doubly=False):
        self.head = None
        self.tail = None
        self.is_doubly = is_doubly

    def add_to_start(self, new):
        """Adds a node at the start of a linked list,
        making it the head

        Args:
            new (Node): Node to be added
        """
        prev_head = self.head
        self.head = new
        new.prev = None
        new.next = prev_head
        prev_head.prev = self.head

    def add_to_end(self, new):
        """Adds a node at the end of a linked list,
        making it the tail

        Args:
            new (Node): Node to be added
        """
        if self.is_doubly:
            tailer = self.tail
            new.next = None
            if tailer:
                prev_tail = tailer
                self.tail = new
                prev_tail.next = new
                new.prev = prev_tail
            else:
                self.tail = new
                self.head = new
        else:
            header = self.head
            if header:
                while(header.next):
                    header = header.next
                header.next = new
            else:
                self.head = new

    def print_list(self, rev):
        """Prints the linked list's values in forward order
        or reverse if possible
        """
        if self.head:
            if rev:
                tailer = self.tail
                while(tailer):
                    print(tailer.value)
                    tailer = tailer.prev
            else:
                header = self.head
                while(header):
                    print(header.value)
                    header = header.next


a = LinkedList(False)
newnode = Node(10)
a.add_to_end(newnode)
a.add_to_end(Node(20))
a.add_to_end(Node(30))
a.print_list(True)
a.add_to_start(Node(40))
a.add_to_start(Node(50))
a.print_list(False)
print()
a.print_list(True)

a = LinkedList(True)
newnode = Node(10)
a.add_to_end(newnode)
a.add_to_end(Node(20))
a.add_to_end(Node(30))
a.print_list(True)
print()
a.add_to_start(Node(40))
a.add_to_start(Node(50))
a.print_list(False)
print()
a.print_list(True)
