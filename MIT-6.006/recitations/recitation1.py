class StaticArray:
    def __init__(self, n):
        self.data = [None] * n
    def get_at(self, i):
        if not (0 <= i < len(self.data)): raise IndexError
        return self.data[i]
    def set_at(self, i, x):
        if not (0 <= i < len(self.data)): raise IndexError
        self.data[i] = x
    
def birthday_match(students):
    '''
    Find a pair of students with  the same birthday
    Input: tuple of student (name, bday) tuples
    Output: tuple of student names or None

    Very poor algorithm as we lose O(n) to initialising the array and
    then loop through the array making the time complexity O(n2)
    '''
    n = len(students)                           # O(1)
    record = StaticArray(n)                     # O(n)
    for k in range(n):                          # n
        (name1, bday1) = students[k]            # O(1)
        for i in range(k):                      # k
            (name2, bday 2) = record.get_at(i)  # O(1)
            if bday1 == bday2:                  # O(1)
                return (name1, name2)           # O(1)  
        record.set_at(k, (name1, bday1))        # O(1)
    return None                                 # O(1)