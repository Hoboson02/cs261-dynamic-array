# # DynamicArray: An array that grows to accommodate new elements.
# # Your implementation should pass the tests in test_dynamic_array.py.
# # Ryan Earl 
import numpy

class DynamicArray:
    def __init__(self):
        self.data = numpy.ndarray(10, 'O')
        self.capacity = 10 
        self.value = 0
        self.next_index = 0
        return None

    def is_empty(self): 
        if self.next_index > 0: 
            return False
        elif self.next_index ==0: 
            return True
      
    def __len__(self): 
        return self.next_index

    def append(self, numb):
        self.data[self.next_index] = numb
        self.next_index += 1

    def __getitem__(self, numb):
        return self.data[numb]

    