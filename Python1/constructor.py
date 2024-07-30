#Constructor [__init__ -> initialization]
# 100% object oriented programming language.
class Circle:
    def __init__(self, radius):
        #self.radius = radius
        print("hi")

    def getRadius(self):
        return self.radius
    
    def setRadius(radius):
        radius = radius
c1 = Circle(10);
c2 = Circle(20);
print(id(c1), id(c2))
print(c1 is not c2)
class Circle1{
    int radius;
    Circle(int radius){
        this.radius = radius;
    }
    public int getRadius(){ #getRadius -> Method
        return this.radius;  #this -> Keyword
    }
}