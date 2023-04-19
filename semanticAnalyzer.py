from copy import deepcopy
import token_1 as t

class semanticToken:
    def __init__(self, element, classification, t_type, _next):
        self.element = deepcopy(element)
        self.classification = deepcopy(classification)
        self.t_type = deepcopy(t_type)
        self._next = _next


class semanticTable:
    def __init__(self):
        self._front = None
        self._rear = None
        self._count = 0


    def __len__(self):
        return self._count
    
    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty queue"

        value = deepcopy(self._front.element)
        
        return value
    
    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"

        node = source._front
        if self._rear is None:
            self._front = node
        else:
            self._rear._next = node
        self._rear = source._rear
        self._count += source._count
        source._front = None
        source._rear = None
        source._count = 0

        return
    def insert(self, element, classification, t_type):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            a copy of value is added to the rear of queue.
        -------------------------------------------------------
        """
        node = semanticToken(element, classification, t_type, None)
        
        if self._front is None:
            self._front = node
        else:
            self._rear._next = node
        self._rear = node
        self._count += 1
        
        return
    
    def search(self, value):
        current = self._front
        while not current == None:
            if current.element == value:
                return True
            current = current._next
        return False
    
    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current.element, current.classification
            current = current._next
    

            