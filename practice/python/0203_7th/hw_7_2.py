class StringRepeater:
    
    def __init__(self):
        self.str = ''

    def repeat_string(self, num, word):
        self.str = word
        for __ in range(num):
            print(f'{self.str}')

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
