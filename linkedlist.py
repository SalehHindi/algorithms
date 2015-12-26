class Node(object):
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

class UnorderedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def print_list(self):
        list_to_print = 'Head='
        current=self.head
        while current != None:
            list_to_print = list_to_print + str(current.get_data()) + '-->'
            current=current.get_next()
        list_to_print = list_to_print + 'None'
        print list_to_print

    def search(self, item):
        current = self.head
        pos = 0
        while current != None:
            pos += 1
            if current.get_data() == item:
                return pos
            current = current.get_next()
        return False

    def remove(self, item):
        current=self.head
        previous=None
        if current.get_data() == item:
            current=current.get_next()
            self.head=current
            return
        else:
            current=current.get_next()
            previous=self.head
            while previous.get_next() != None:
                if current.get_data()==item:
                    current=current.get_next()
                    previous.set_next(current)
                else:
                    previous=current
                    current=current.get_next()


newlist = UnorderedList()
newlist.add(1)
newlist.add(2)
newlist.add(1111)
newlist.add(3)
newlist.add(4)
newlist.add(10)
newlist.print_list()
print newlist.size()

newlist.remove(1111)
newlist.print_list()
print newlist.size()

newlist.remove(1)
newlist.print_list()
print newlist.size()




'''
Mistakes I've made
writing functions as foo instead of foo()


'''






