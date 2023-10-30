import sys
class PriorityQueueBase:
    '''abstract bse class for a priority queue'''
    class _item:
        '''Lightweight composite to store priority queue items'''
        __slots__='_key','_value'
        def __init__(self,k,v):
            self._key=k
            self._value=v
        def __It__(self,other):
            #compares items based on their keys
            return self._key<other._key
    def is_empty(self):
        '''Return True is priority Queue is empty'''
        return len(self)==0



class HeapPriorityQueue(PriorityQueueBase):
    ''''A min-oriented priority queue implementaion with a binary heap'''

    # non-public behaviours
    def _parent(self,j):
        return (j-1)//2
    def _left(self,j):
        return 2*j+1
    def _right(self,j):
        return 2*j+2
    def _has_left(self,j):
        return self._left(j)<len(self._data)
    def _has_right(self,j):
        return self._right(j)<len(self._data)
    def _swap(self,i,j):
        '''swap elements of index i and index j of array'''
        self._data[i],self.data[j]=self.data[j],self.data[i]
    def _upheap(self,j):
        parent=self._parent(j)
        if j>0 and self._data[j]<self._data[parent]:
            self._swap(j,parent)
            self._upheap(parent)
    def _downheap(self,j):
        if self._has_left(j):
            left=self._left(j)
            small_child=left
        #     although right may be smaller
        if self._has_right(j):
            right=self._right(j)
            if self._data[right]<self._data[left]:
                small_child=right
        if self._data[small_child]<self.data[j]:
            self._swap(j,small_child)
            self._downheap(small_child)#recur at position of small child

    '''public behaviours '''
    def __init__(self):
        '''create  a new Empty priority Queue'''
        self._data=[]
    def __len__(self):
        '''Return the number of items in the priotity queue'''
        return len(self._data)
    def add(self,key,value):
        '''Add a key_value pair to the priority queue'''
        self._data.append(self._item(key,value))
        # then upheap newly added position
        self._upheap(len(self._data)-1)
    def min(self):
        '''Return but do not remove the (k,v) tuple with minimum key
        Raise Exception if empty'''
        if self.is_empty():
            print('Priority queue is empty')
        item=self._data[0]
        return (item._key,item._value)
    def remove_min(self):
        '''remove and return (K,v) tuple with minimum key
        Raise Empty Exception if empty'''
        if self.is_empty():
            print("Priority queue is empty")
        self._swap(0,len(self._data)-1) # put minimum item at the end
        item=self._data.pop()             # and remove it from the list
        return (item._key,item._value)    # then fix new root

if __name__=='__main__':
    minheap=HeapPriorityQueue()
    minheap.add(0, 1)
    print(minheap.__len__())
    print(minheap.min())