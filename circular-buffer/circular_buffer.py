class BufferFullException(BufferError):

    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):

    def __init__(self, message):
        self.message = message


class CircularBuffer:

    def __init__(self, capacity):
        self.buffer = list()
        self.capacity = capacity

    def read(self):
        if len(self.buffer) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        out = self.buffer.pop(0)
        return out

    def write(self, write_data):
        if len(self.buffer) == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.buffer.append(write_data)

    def overwrite(self, overwrite_data):
        try: 
            self.write(overwrite_data)
        except BufferError:
            self.read()
            self.write(overwrite_data)

    def clear(self):
        self.__init__(self.capacity)

    def show(self):
        return self.buffer