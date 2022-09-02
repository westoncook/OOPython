"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100

    >>> serial.__repr__()
    '<SerialGenerator start=100 next=101>'
    """

    def __init__(self, start):
        self.start = start
        self.prev = start -1

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.start + 1}>"

    def generate(self):
        self.prev += 1
        return self.prev

    def reset(self):
        self.prev = self.start -1