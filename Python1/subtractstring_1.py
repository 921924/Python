class Mystr(str):
    def __init__(self, string):
        super(str, string)

    def test_str(self):
        print(self.string)
        
str1 = Mystr('hello'); str2=Mystr('handsome')
print(str1 - str2)