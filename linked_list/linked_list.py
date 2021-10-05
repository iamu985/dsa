import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.loc = 0
    
    def __str__(self):
        if self.next == None:
            return str((self.data, self.next))
        else:
            return str((self.data, self.next.data))

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
        '''This function pushes the node to the last of list and assigns the next pointer to the node'''
        node = Node(data)
        if self.head == None:
            self.head = node
            self.updateLength() # updates length of the list 
        elif self.head.next == None:
            self.head.next = node 
            loc_number = self.head.loc + 1
            node.loc = loc_number
            self.updateLength() # updates length
        else:
            previous_node = self.head
            while previous_node.next != None:
                previous_node = previous_node.next
                if previous_node.next == None:
                    previous_node.next = node
                    loc_number = previous_node.loc + 1
                    node.loc = loc_number
                    self.updateLength() # updates length
                    break

    def push(self, data):
        '''
        This fucntion inserts the data at the first of the list and also shifts the pointer to the previous head node
         '''
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.loc = self.head.loc
            self.head.loc = self.head.loc + 1
            node.next = self.head
            self.head = node
    
    def get(self, loc):
        #traverse throug the list
        node = self.head
        while (node):
            if node.loc == loc:
                return node
            node = node.next 
        
        raise IndexError
    

    
    def insert(self, data, loc):
        '''
        Algorithm
        1. Count the number of nodes in the list
        2. If count exceeds loc i.e. loc > count then,
            Append new node at the end of the list
            Set new_node loc to loc i.e. new_node.loc = loc
        3. If count > loc, then,
            Get last count node whose loc is less than defined loc
            Set last count node next to the new node
            Set new node next to the node after last count node
            Set new node loc value to after last count node loc
            Set after last count node loc value to + 1
        '''
        if loc > self.length:
            raise IndexError

        if loc < self.length:
            node = Node(data)
            swap_node = self.get(loc)
            prev_node = self.get(loc-1)

            prev_node.next = node 
            node.next = swap_node

            node.loc = loc
            while (swap_node):
                swap_node.loc += 1
                swap_node = swap_node.next
    
             

    def updateLength(self):
        node = self.head
        count = 0 
        while (node):
            count += 1
            node = node.next
        self.length = count
            

    
    def printList(self):
        temp = self.head
        while (temp):
            if temp.next != None:
                print(f"{temp.data}({temp.loc}) <=>", end=' ')
                temp = temp.next
            else:
                print(f'{temp.data}({temp.loc})')
                temp = temp.next
    
    def pop(self, loc=0):
        try:
            prev_node = self.get(loc-1)
            next_node = self.get(loc+1)
            
            prev_node.next = next_node
            next_node.loc -= 1
            self.updateLength()
        except IndexError:
            next_node = self.get(loc+1)
            self.head = next_node
            next_node.loc -= 1
            self.updateLength()
            

if __name__ == '__main__':
    ll = LinkedList()
    print('-'*13)
    print(' Linked list')
    print('-'*13)
    pop = ['frank', 'brano', 135, 'eleven', 'emma', 'corey', 'django']
    c = [1, 2, 3]
    for n in pop:
        ll.append(n)
    
    ll.printList()
    
