import pytest
from linked_list import LinkedList

class TestLinkedList:
    def test_linked_list_length(self):
        ll = LinkedList()
        name = 'name'
        for n in name:
            ll.append(n)
        
        assert ll.length == 4
    
    def test_linked_list_get_method(self):
        ll = LinkedList()
        name = 'frank'
        for n in name:
            ll.append(n)
        
        assert ll.get(2).data == 'a'
    
    def test_linked_list_get_method_raise_error(self):
        ll = LinkedList()
        name = 'frank'
        for n in name:
            ll.append(n)
        
        with pytest.raises(IndexError):
            ll.get(10)

    def test_linked_list_insert_method(self):
        ll = LinkedList()
        name = 'frank'
        for n in name:
            ll.append(n)
        
        ll.insert('x', 2)
        assert ll.get(2).data == 'x'
        assert ll.get(1).data == 'r'
        assert ll.get(3).data == 'a'
    
    def test_linked_list_insert_method_raise_error(self):
        ll = LinkedList()
        name = 'frank'
        for n in name:
            ll.append(n)
        
        with pytest.raises(IndexError):
            ll.insert('o', 10)
    
    def test_linked_list_pop_method(self):
        ll = LinkedList()
        name = 'frank'
        for n in name:
            ll.append(n)
        ll.pop()
        ll.pop(3)
        assert ll.length == 3
        assert ll.get(0).data == 'r'
        assert ll.get(2).data == 'n' 

