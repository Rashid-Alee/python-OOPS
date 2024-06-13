# Shape Drawing Application
# Base Class
class Shape:
    # Abstract method to be implemented by all derived classes
    def draw(self):
        raise NotImplementedError("Subclass must implement abstract method")


# Derived Class for Circle
class Circle(Shape):
    # Implementation of the draw method for Circle
    def draw(self):
        print("Drawing a Circle")


# Derived Class for Rectangle
class Rectangle(Shape):
    # Implementation of the draw method for Rectangle
    def draw(self):
        print("Drawing a Rectangle")


# Derived Class for Triangle
class Triangle(Shape):
    # Implementation of the draw method for Triangle
    def draw(self):
        print("Drawing a Triangle")


# Function to demonstrate polymorphism
def draw_shape(shape):
    # Calls the appropriate draw method based on the object type
    shape.draw()


# Creating objects of different shapes
circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

# Drawing shapes using polymorphism
print("Drawing shapes:")
draw_shape(circle)  # Output: Drawing a Circle
draw_shape(rectangle)  # Output: Drawing a Rectangle
draw_shape(triangle)  # Output: Drawing a Triangle
