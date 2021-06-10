import ctypes


class Array:
    """
    Implements the Array ADT using array capabilities of the ctypes module.
    """
    def __init__(self, size):
        """
        Creates an array with size elements.

        :param size: size of array.
        """
        assert size > 0, "Array size must be > 0"
        self._size = size

        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()

        # Initialize each element.
        self.clear(None)

    def __len__(self):
        """
        Returns the size of the array.

        :return: the size of the array. 
        """
        return self._size

    def __getitem__(self, index):
        """
        Gets the value of the element.

        :param index: the index of element.
        :return: value of the element.
        """
        if not 0 <= index < self._size:
            raise IndexError('Invalid index')
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        Puts the value in the array element at index position.

        :param index: the index element.
        :param value: the value of element.
        """
        if not 0 <= index < self._size:
            raise IndexError('Invalid index')
        self._elements[index] = value

    def clear(self, value):
        """
        Clears the array by setting each element to the given value.

        :param value: the value of element.
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """
        Returns the array's iterator for traversing the elements.

        :return: the array's iterator for traversing the elements. 
        """
        return _ArrayIterator(self._elements)

    def __str__(self):
        """
        Converts structure to a string.

        :return: converted structure.
        """
        to_return = "("
        for index in range(self._size - 1):
            to_print = str(self[index])
            to_return = to_return + to_print + ","
        to_print = str(self[self._size - 1])
        return to_return + to_print +")"

class _ArrayIterator:
    """
    An iterator for the Array ADT.
    """
    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration


class Array2D:
    """
    Implementation of the Array2D ADT using an array of arrays.
    """
    def __init__(self, num_rows, num_cols):
        """
        Creates a 2D array of size num_rows x num_cols.        
        :param num_rows: number of rows.
        :param num_cols: number of columns.
        """

        # Creates a 1D array to store an array reference for each row.
        self.rows = Array(num_rows)

        # Creates the 1D arrays for each row of the 2D array.
        for i in range(num_rows):
            self.rows[i] = Array(num_cols)

    def num_rows(self):
        """
        Returns the number of rows in the 2D array.

        :return: 
        """
        return len(self.rows)

    def num_cols(self):
        """
        Returns the number of columns in the 2D array.

        :return: the number of columns in the 2D array.
        """
        return len(self.rows[0])

    def clear(self, value):
        """
        Clears the array by setting every element to the given value.

        :param value: value to be set.
        """
        for row in self.rows:
            row.clear(value)

    def __getitem__(self, index_tuple):
        """
        Gets the contents of the element at position [i, j]

        :param index_tuple: the index of position. 
        :return: the value.
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        if not (0 <= row < self.num_rows() and 0 <= col < self.num_cols()):
            raise IndexError('Invalid index')
        array_1d = self.rows[row]
        return array_1d[col]

    def __setitem__(self, index_tuple, value):
        """
        Sets the contents of the element at position [i,j] to value.

        :param index_tuple: the index of position.
        :param value: the value to be set.
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        if not (0 <= row < self.num_rows() and 0 <= col < self.num_cols()):
            raise IndexError('Invalid index')
        array_1d = self.rows[row]
        array_1d[col] = value

    def __str__(self):
        st1 = ""
        for row in self.rows:
            st1 += str(row) + "\n"
        return st1

        #return str( [str(row) for row in self.rows])



class DynamicArray:
    """
    A dynamic array class a simplified Python list.
    """

    def __init__(self):
        """
        Creates an empty array.
        """
        self._size = 0  # actual number of elements
        self._capacity = 1  # default array capacity
        self._elements = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """
        Returns the number of elements in the array.

        :return: the number of elements in the array. 
        """
        return self._size

    def __getitem__(self, index):
        """
        Gets the value of the element by index.

        :param index: the index of element.
        :return: the value of the element.
        """
        if not 0 <= index < self._size:
            raise IndexError('Invalid index')
        return self._elements[index]

    def append(self, value):
        """
        Puts the value in the end of the array.

        :param value: the value of element.
        """
        if self._size == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        self._elements[self._size] = value
        self._size += 1

    def _resize(self, capacity):
        """
        Resize internal array to new capacity.
                
        :param capacity: new capacity of array.
        """
        new_elements = self._make_array(capacity)  # new (bigger) array

        # Makes a copy of elements
        for k in range(self._size):
            new_elements[k] = self._elements[k]
        self._elements = new_elements  # use the bigger array
        self._capacity = capacity

    def _make_array(self, size):
        """
        Return new array.
        
        :param size: size of array.
        :return: array.
        """
        return Array(size)

    def insert(self, index, value):
        """
        Inserts value at index, shifting subsequent values rightward.        

        :param index: the index.
        :param value: the value that need to be inserted. 
        """
        # We double a capacity if needed
        if self._size == self._capacity:
            self._resize(2 * self._capacity)

        # Shifts rightmost elements
        for i in range(self._size, index, -1):
            self._elements[i] = self._elements[i - 1]

        # Store newest element
        self._elements[index] = value
        self._size += 1

    def remove(self, value):
        """
        Removes first occurrence of value.
        
        :param value: the value that need to be removed.
        """
        for i in range(self._size):
            if self._elements[i] == value:  # found a match!
                # Shifts others elements to fill gap
                for j in range(i, self._size - 1):
                    self._elements[j] = self._elements[j + 1]

                self._elements[self._size - 1] = None  # helps garbage collection
                self._size -= 1  # we have one less item

                return  # exit immediately
        raise ValueError("Value not found")  # only reached if no match

