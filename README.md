# Object Oriented Programming

- Object oriented programming is a programming paradigm
- Objects oriented programming is like the blueprint to the objects
- The blueprints is called as Class
- Every Object has its state and behaviour

### Types of Programming

- Declarative
- Functional
- Logical
- Imperative 
- Object oriented programming

### Advantages of OOPS

- Modularity - Every object acts as individual modules, thus the changes doesn't affect other object
- Scalabilty - We can add more attributes such as action or state for every object since it's scalable
- Reusability - We can use the same object in multiple programs without writing them again


### Class

- Class is a blueprint which create objects
- Every class has object's state and behaviour defined
- We are responsible for creating the class
- Using those classes we could create 'n' of objects

***Example for objects***

```
Book
Car
Dog
Player
```

We just create single class for 'Book' defining its state and behaviour and we could create multiple object (instances of book)

### Writing a class

- Class name has Pascal case (upper camel case) naming convention
- Which means every word starts with upper case

***Example***
```
House
LinkedList
SchoolBackpack
```

### Problem Statement

- Classes can be designed by reviewing the problem statements
- problem statements are actual client discussion about the project

***Example***

```
Starfood is a fast food shop. We have fast foods like Burger, Pizza, Sanwiches. We also provide waterbottles, Cooldrink, French fries. Customer who buy more that 3 items will get 10% discount. There are 5 employees working in the shop
```

In the above example filter the nouns to use them as classes.
```
food, shop, burger, pizza, sanwich, watterbottle, cooldrink, Frenchfries, Customer, employee
```
These are the potential candidates for the objects

### Questions to keep in mind
We need to ask questions to ourselves while designing the class or selecting the candidates for the class.

- Is this item needed for the scope of the project?
- Does the term represent an example of a class? what class?
- Is this class important that we are creating?


### Structure of the class

-  A class defined by two parts
    - Header - class keyword, name of class with inherited class name if any (first line)

        ***Example***
        ```
        class FastFood:
        ```
    - Body - Contains the elements of the "blueprint", including the attributes and behavior of the objects. They can be classified into the below elements
        -   class attributes
        - ```__init__()```
        - Methods

***Example***

```
class ClassName:
    # Class Attributes
    # __init__()
    # Methods
```

### Instance

- An object created from the class
- Class is an abstract
- Instance is concrete
- A class is just a blueprint however an instance is actual object with attributes.

### Instance Attributes

The attributes of an object. They are variables that belong to a particular object

***Example***

A Backpack may have below attributes
```
size
color
weight
material
Number of pockets
Number of zippers
```

Instance attributes are same to all the instances but they are not necessarily to be same. For example `size` attribute for two `Backpack` instances might be different. One could be `small` and another one could be `large`.

### `__init__()`

- `__init__` is the magic class method which automatically called whenever an instance is created.
- The instance attributes are created through `__init__()` method.
- This is called as constructor.

***Example 1***

We are going to create a class `House`. Every house has different price. We need to have `price` attribute in class. Which can be specified in `__init__()` method.

```
class House:

    def __init__(self, price):
        self.price = price

```

Let's break down the above code.
- `def __init__(self, price):` 
    - `def` keyword to create method in class. 
    - `__init__(self, price):` - Init always has `self` as first parameter. This `self` represents the instance created. The `price` or any other attributes can be added after `self`
- `self.price = price`
    - Takes the `price` attribute given in the instance 
    - And assign the `price` value to the instance `self.price`. since `self` refers to the instance

***Example 2***

We need to create a Backpack class with `items` attribute. 

```
class Backpack:

    def __init__(self):
        self.items = []
```

Let's break down the above code.
- `def __init__(self):`
    - create init method with no attribute. We don't need to customize the attributes when initializing.
- `self.items = []`
    - We are creating instance attribute `items` using `self.items`
    - we assign `[]` empty list to instance attribute `items`.
    - This is because in the real world when we get a Backpack. it would be empty without any items. We have to fill them up.

### Few common mistakes while creating `__init__()`

- Omitting the `def` keyword
- Using only one `_` before and after to the `init`
- Omitting `self` as the first parameter
- Not using `self.<attribute>` to define the instance attribute inside `__init__(self)` method

### Why `self`

- `self` - A generic way for referring the current instance.

```
class House:

    def __init__(self, price):
        self.price = price
```

We create multiple instances in actual programs, Every instance attribute has different value. `self` keyword refers the attribute of current instance. `self.price = price` - both `price` are not same. `self.price` is the price of instance. the second `price` is the parameter passed.

### Creating an instance

Instance is the actual object which is created from Class

***Example 1 - Instance without argument***

```
class Backpack:

    def __init__(self):
        self.items = []

# Creating Backpack object instance
my_backpack = Backpack()
print(my_backpack)
```

***Output***

The output is just printing the memory address of `Backpack` object created

```
<__main__.Backpack object at 0x000002B835A9AD10>
```

***Example 2 - Instance with 1 argument***

```
class Circle:

    def __init__(self, radius):
        self.radius = radius

# Creating circle object with radius as 5
my_circle = Circle(5)
print(my_circle)
```

***Output***

The output is just printing the memory address of `Circle` object created

```
<__main__.Circle object at 0x00000220271EAD10>
```


***Example 3 - Instance with more arguments***

```
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

# Rectangle object is created with length and width (more than one argument)
my_rectangle = Rectangle(5, 10)
print(my_rectangle)
```

**Note: The order of argument passing should be same as it specified in the `__init__()` method**


***Output***

The output is just printing the memory address of `Rectangle` object created

```
<__main__.Rectangle object at 0x000002733DD27D60>
```

**Note: `self` is not required to specify in the argument. since its automatically taken from the instance.**


### Accessing Attributes

- We can access the attribute of an object instance using Dot notation
- Syntax used to access the members of an object (its variable and methods) is called Dot Notation
- `<object>.<attribute>` - This is the syntax to access instance's/object's attribute outside the class
- `self.<attribute>` - This syntax is to access the instance attribute within the class


***Example 1 - Accessing attribute outside the class***

```
class Circle:

    def __init__(self, radius):
        self.radius = radius
        

my_circle = Circle(3.14)
print(my_circle.radius)
```

***Output***
```
3.14
```


***Example 2 - Accessing attribute inside the class***

```
class Circle:

    def __init__(self, radius):
        self.radius = radius
        print(self.radius)
        

my_circle = Circle(3.14)
```

***Output***
```
3.14
```

***Example 3 - Accessing multiple instances attributes***

```
class Movie:

    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating

# Creating instances
my_favorite_movie = Movie("Vikram", 2022, "Tamil", 4.8)
your_favorite_movie = Movie("RRR", 2022, "Telugu", 4.5)

# Accessing the instance attributes 

print("My Favorite Movie: ")
print(my_favorite_movie.title)
print(my_favorite_movie.year)
print(my_favorite_movie.language)
print(my_favorite_movie.rating)


print("Your Favorite Movie: ")
print(your_favorite_movie.title)
print(your_favorite_movie.year)
print(your_favorite_movie.language)
print(your_favorite_movie.rating)
```

***Output***

```
My Favorite Movie: 
Vikram                                                                                                   
2022
Tamil
4.8                                                                                                      
Your Favorite Movie: 
RRR
2022
Telugu
4.5
```

This is the best example for accessing the instance/object attributes. Since every instance has same attributes but values would be different based on the object.


### Default Arguments

- Default values assigned to parameters when their corresponding arguments are omitted.
- `<paramater>=<value>` - This is the syntax for assigning default values for arguments
- Parameters with default value should be the last parameters in the list of parameters


***Example***

```
class Circle:

    def __init__(self, radius=3.5):
        self.radius = radius

circle1 = Circle()
circle2 = Circle(4)

print(circle1.radius)
print(circle2.radius)

```

***Output***

```
3.5
4
```

In the above example we have created `circle1` without passing any argument and `circle2` with argument.
Since the `Circle` class has specified with default `radius` value in the `__init__()` method, which is `3.5`. Thus on printing `circle1` it gives default value though it is not passed as an argument. whereas in the `circle2` we are passing an argument while creating the object instance. So on printing the value for the `circle2` is `4`.


### Modify the value to object attribute

We can modify the instance attribute value like below example. It's simple like assigning value to a variable.

```
class Backpack:
    
    def __init__(self, color):
        self.items = []
        self.color = color

my_backpack = Backpack("Red")
your_backpack = Backpack("Black")

# Printing the color of both backpacks
print("Before modification")
print(my_backpack.color)
print(your_backpack.color)

# changing the color of my_backpack

my_backpack.color = "Green"

# Printing the color of both backpacks again
print("After modification")
print(my_backpack.color)
print(your_backpack.color) 
```

***Output***

```
Before modification
Red
Black
After modification
Green
Black
```

### Class Attributes

- A class attribute is an attribute of class
- It belong to the whole class
- All object instances share the same attribute
- If we change the value of class attribute, It would affect all instances
- Class attribute are genearally defined before `__init__()` method
- `<class_attribute> = <value>` - This is the syntax to create class attribute. 

***Example 1***

```
class Dog:

    # Class attribute
    species = "Canis Lupus"
    
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

```
In the above example we have `Dog` class. The `__init__()` method has defined instance attributes like `name, age, breed`. However our motive is to have same species of dog for all the instances. we add our `species` class attribute after the class. So whenever any instance call `species` attribute, the value would be same. 

***Example 2***

```
class Backpack:

    #class attribute
    max_num_items = 10

    def __init__(self):
        self.items = []

```

Above is the perfect example of using class attribute. We define `max_num_items` and assign value `10` to it. Whenever any backpack instance is created all of them has the same value for `max_num_items` attribute. So the change would affect all the instance.

### Accessing class attribute

- We could access the class attribute using Dot notation
- <ClassName>.<attribute_name> - We can use this syntax to access class attribute both inside and outside the class

***Example***
```
class Backpack:

    #class attribute
    max_num_items = 10

    def __init__(self):
        self.items = []

print(Backpack.max_num_items)
```

***Practical Example***
```
class Movie:

    id_counter = 1

    def __init__(self, name, rating):
        self.id = Movie.id_counter
        self.name = name
        self.rating = rating

        Movie.id_counter += 1

my_favorite_movie = Movie("Vikram", 4.8)
your_favorite_movie = Movie("Bahubali", 4.7)

print(my_favorite_movie.id, my_favorite_movie.name, my_favorite_movie.rating)
print(your_favorite_movie.id, your_favorite_movie.name, your_favorite_movie.rating)
```

In the above example, every `Movie` instance has `name` and `rating` instance attributes. however we need to create unique id for every movie that is created. This id should start with `1` and increment everytime when we create a movie. We have created a class attribute `id_counter` and assign it to `1`. We create an instance attribute `id` with `self.id` and assign it to `Movie.id_counter`. This would create `id` with the value of `Movie.id_counter` whenever we create an instance. However this would always remain `1`. So we are creating an increment to this class attribute within `__init__()` method. `Movie.id_counter += 1`. The solution is complete now. Whenever we create an instance it creates an unique id to the instance. 

***Output***
```
1 Vikram 4.8
2 Bahubali 4.7
```

Output worked as expected. Note that we are using `my_favorite_movie.id` to print the id of instance not the `Movie.id_counter`, because it would always be `1` for all the instances. we have an instance attribute which is eligible candidate `id` for unique id creation.

### Modifying Class attributes

**Warning:** : Modifying the class attribute would affect all the instances. However in some cases we require to modify the class attribute.

***Example***

We have a Juice shop which is newly opened. Shop owner wants to give an offer to the customers to catch up new customers. He is pricing all the juices to `50` Rupees fixed. How could we design the class.

```
class Juice:

    price = 50

    def __init__(self, name, with_ice):
        self.name = name
        self.with_ice = with_ice

my_juice = Juice('Apple', True)
your_juice = Juice('Watermelon', False)

print(my_juice.price)
print(your_juice.price)
```

***Output***
```
50
50
```

As per the above code I'm ordering Apple Juice, with ice, you are ordering Watermelon juice without ice. Once we done with our juices we are checking out. If we see the price for both the juices would be 50. Since it's taken from class attribute.

The Juice shop owner decided to raise the juices price to 65 after some days. We could update the class attribute like the below.

```
class Juice:

    price = 50

    def __init__(self, name, with_ice):
        self.name = name
        self.with_ice = with_ice

my_juice = Juice('Apple', True)
your_juice = Juice('Watermelon', False)

print(my_juice.price)
print(your_juice.price)

Juice.price = 65

print(my_juice.price)
print(your_juice.price)
```

***Output***
```
50
50
65
65
```

So, the price is raised to all juices to 65 after the update.

### Encapsulation

- Encapsulation is one of the main pillers of object oriented programming
- It is bundling of data and methods into a single unit class
- Class acts as a capsule which has both attributes and methods
- Class separates them from the rest of the program
- The purpose is to restric the access of attributes and methods (Information Hiding)
- It prevents the direct access to the attributes for security reasons
- Getters and setters are the methods helpful to achieve the information hiding
- Developer needs to choose which attribute is puplic and which one is non public attribute.

### Abstraction

- Abstraction is a principle to show only essential attributes of a class and hides unnecessary details
- Hide the complexity from the user
- Example: We just need to know how to drive a car. we don't need to understand how engine works.
- Example2: User just need to click the buttons in UI. He don't need to understand the background processes.
- Class has two main parts
    - Interface - Visible part of the class
    - Implementation - Internal part of the class with the code performs that performs functionality
- Abstraction allows to abstract out common part of the code to avoid repetation
- Single class with Inheritance instead of multiple classes


### Public vs Non Public attributes

- Classes attributes can be public or non public to avoid unexpected changes to the attribute
- **Public** - An attribute can be accessed and modified directly without any access restriction

    ***Example***

    ```
    class Car:

    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

    my_car = Car("Jaguar", 2020, "White")

    print(my_car.year)
    ```

    ***Output***
    ```
    2020
    ```
    The problem lies in creating public attribute is suppose we tried to add the below line in our program. 

    ```
    my_car.year = 5000
    ```
    This would modify the year which we created while instantiating the `my_car` instance.

    ```
    class Car:

    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

    my_car = Car("Jaguar", 2020, "White")

    print(my_car.year)
    my_car.year = 5000
    print(my_car.year)
    ```

    ***Output***

    ```
    2020
    5000
    ```

    This creates a serious bug

- **Non Public** - An attribute that shouldn't be accessed or modified outside of the class

    - In Python we have two types of non-public attribute 
    - By Convention - adding `_<attribute>` - non-public (Protected)
    - Changing Name - adding `__<attribute>` - Name mangling (Private)

    ***Example***

    ```
    class Car:

        def __init__(self, brand, year, color):
            self.brand = brand
            self._year = year
            self.color = color

    my_car = Car("Jaguar", 2020, "White")
    print(my_car.year)

    ```

    In the above example we just added an `_` in front of `year` attribute in our `__init__()` method. If we access the `year` attribute now we would see an error

    ***Error Output***
    ```
    Traceback (most recent call last):
        File "c:\Users\sundar\code\encapsulation.py", line 10, in <module>
            print(my_car.year)
    AttributeError: 'Car' object has no attribute 'year'. Did you mean: '_year'?
    ```
    
    **Note: There is no absolute private/protect in Python. We just provide the convention in python that the attribute is private.**

    We can still access the `year` attribute like `_year` but we shouldn't do it.

    ```
    print(my_car._year)
    ```
    The above line prints the year without any problem. but this shouldn't be done in the code

### Name Mangling

- This is the process of changing the name of an attribute.
- This could be achieved by adding double underscore infront of the attribute `__<attribute>`
- `__<attribute__` which typically converts our attribute name like `_<class>__<attribute>`

***Example***

Let's take the same `Car` class as an example. Instead of `_year` we are now adding `__year` like below code

```
class Car:

    def __init__(self, brand, year, color):
        self.brand = brand
        self.__year = year
        self.color = color

my_car = Car("Jaguar", 2020, "White")
```

Now if we try to access the `year` by any of the below method it would fail. 

```
print(my_car.year)
print(my_car._year)
print(my_car.__year)
```

***Error Output***
```

  File "c:\Users\suthanga\Desktop\Code\encapsulation.py", line 10, in <module>
    print(my_car.year)
AttributeError: 'Car' object has no attribute 'year'

Traceback (most recent call last):
  File "c:\Users\sundar\Desktop\Code\encapsulation.py", line 12, in <module>
    print(my_car._year)
AttributeError: 'Car' object has no attribute '_year'

Traceback (most recent call last):
  File "c:\Users\sundar\Desktop\Code\encapsulation.py", line 14, in <module>
    print(my_car.__year)
AttributeError: 'Car' object has no attribute '__year'
PS C:\Users\suthanga\Desktop\Code\Object Oriented Programming>
```

This makes restriction little more tight. However it's possible to access the attribute with below syntax.

```
print(my_car._Car__year)
```

This is the original name mangling which the `__` converts. Though we could access the attribute we shouldn't do that. 

Bottomline is, if we see any attribute with single or double underscores it is a red warning to developer that we shouldn't use the attribute outside of the class.

***Correct way to create Non-public attributes***

`__<attribute>`
`__<attribute>_`

The above are the only correct way to create non-public attribute

**Note: `__<attribute>__` is called as Magic method which we will see in later sections**

### Getters and Setters

- Getters and Setters are the methods inside the class
- These getters and setters are helpful in accessing the non-public attributes or other attributes with indirect access
- They act as an intermediate between the attributes and user
- getters - get the value of the attribute
- setters - set the value of the attribute
- `get_<attribute>` - is the syntax of getter
- `set_<attribute>` - is the syntax of setter

***Getter Example***
```
class Movie:

    def __init__(self, title, rating):
        self._title = title
        self.rating = rating

    def get_title(self):
        return self._title

my_movie = Movie("Vikram", 4.8)
print("My favorite movie is ", my_movie.get_title())
```

Let's breakdown the code,
- We have `Movie` class with two attributes `_title` and `rating`
- We create a getter method with `get_<attribute>` convention to access the non public attribute `_title`
- The method returns instance's title with this line 
`return self._title`
- To use the getter method we need to follow the  syntax `<object>.get_<attribute>()`
- example: `my_movie.get_title()`

***Setter example***
Setters are used to set the value for an attribute with validation in the setter method. In the below example we are going to create a `Token` class which creates a token and get it with getters and modify the token with setter. We are going to validate in setter that token should only be integer

```
class Token:

    def __init__(self, token):
        self._token = token

    def get_token(self):
        return self._token

    def set_token(self, new_token):
        if isinstance(new_token, int):
            self._token = new_token
        else:
            print("Enter valid Token format!!!")

my_token = Token(1234)

print("My Token is", my_token.get_token())
```

For the above program the output would be 

```
My Token is 1234
```

Now let's use the setter method to set the new token

```
my_token.set_token(12345)
print("My New Token is", my_token.get_token())
```
This modifies the token to `12345`
```
My Token is 1234
My New Token is 12345
```

Suppose if pass a string attribute to the `set_token()` method it would fail because we are using validation inside the setter method `isinstance(new_token, int)`

```
my_token.set_token("Testing")
print("My New Token is", my_token.get_token())
```

```
My Token is 1234
Enter valid Token format!!!
My New Token is 1234
```

As we could see the old token value is protected without any changes. setters acts as an intermediater and do the validation

### Properties

- Properties are the pythonic way to work with non-public attributes, getters and setters
- we normally create getter and setter methods for an attribute and create a property within the class
- `name = property(get_name, set_name)` - This is the way to specify the property with both getter and setter
- Now whenever it is required to call the non-public `_name` attribute we could call without direct access/getter/setter. we could access directly with property `<object>.name`
- When you try to access the value of the property, the getter method is called
- When you try to modify the value of the property, the setter method is called

***Example***

```
class Circle:

    VALID_COLORS = ("Red", "Blue", "Green")

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, int) and new_radius > 0:
            self._radius = new_radius
        else:
            print("Invalid radius passed!!!")
    
    radius = property(get_radius, set_radius)

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            print("Invalid color passed!!!")
            
    color = property(get_color, set_color)

my_circle = Circle(10, "Red")

#Radius
print("circle radius: ", my_circle.radius)
my_circle.radius = 5
print("New radius: ", my_circle.radius)

#Color
my_circle.color = "Green"
print("New color: ", my_circle.color)
```

### `@property` decorator

- Decorator is a function which takes the function and extend its functionality without modifying it
- We could create both getter and setter property with `@property` decorator

**Getter property with `@property`**

```
class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        return self._rating

my_fav_movie = Movie("RRR", 4.7)

print("Rating: ", my_fav_movie.rating)
```

Let's break down the above code,

- We created a `Movie` class with `title` and non-public attribute `_rating`
- We need to create a getter with `@property` decorator
- To use the decorator we need to add the `@property` above the method we use for getter
- The name for the getter method could be simple as the attribute name
- Rest of the method would be same as we getting in normal getter method


**Setter property with `@<property_name>.setter`**

```
@rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, float) and 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print("Invalid Rating Given!!!")
```

- For setter the syntax is little different. we need to use the getter property name as decorator and add keyword setter with dot notation - `@rating.setter`
- The method name should be same as the getter method.
- Rest are the same as the general setter

***Whole Example program***

```
class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, float) and 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print("Invalid Rating Given!!!")

my_fav_movie = Movie("RRR", 4.7)

print("Rating: ", my_fav_movie.rating)

my_fav_movie.rating = 4.9
print("Rating: ", my_fav_movie.rating)
```

***Output***
```
Rating:  4.7
Rating:  4.9
```

### `@property.deleter`

- There is another property called `@property.deleter` which deletes the property value

```
@rating.deleter
    def rating(self):
        del self._rating
```

To access the deleter property
```
del my_fav_movie.rating
```

### Methods

- Method is the behavior or action of the object
- Method is a function associated to an object of the class or to the class itself
- Calling a method is similar to calling a function
- There are three methods
    1. Instance method
    2. Class method
    3. Static method

### Instance method

- Method that belongs to a specific object
- They have access to the state(attributes) of the object that calls them
- This can be achieved through `self`
- `self` in methods refers to the instance that are calling the method
- Method names usually include verbs since they are representing action
    - Example: `Calculator` class may have `add`, `subtract`, `multiply`, `divide` methods
- Naming conventions for methods (snake case)
    - Should be a lowercase and words can be seperated with underscore - `method_name`
    - for Non-public methods we could add leading underscore - `_show_balance`


***Example syntax for methods***
```
class ClassName:

    # class attribute
    
    # __init__()

    def method_name(self, param1, param2):
        #code
```
***Example***
```
class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
```

### Accessing methods

- Accessing methods are similar to accessing the function
- But there is a small syntax change, since they are shared by instances they methods would be called along with the object name - <object>.<method_name>(<arguments>)
- For the above `Calculator` class we could access the `add` method like below
```
calculation = Calculator(8, 2)
print(calculation.add())
```
This would return the output as `10`

***Practical Example***
```
class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Input is not valid item")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            print(f"{item} is removed")
            return 1
        else:
            print(f"{item} not in the backpack")
            return 0

    def has_item(self, item):
        return item in self._items

# Creating Backpack
# saving the items to a variable
# printing the items
my_backpack = Backpack()
items = my_backpack.items
print(items)

#Adding an item to backpack and print items
my_backpack.add_item("Books")
print(items)

#Adding another item and print items
my_backpack.add_item("Waterbottle")
print(items)

#Checking if Backpack has Waterbottle
has_water = my_backpack.has_item("Waterbottle")
print(has_water)

#Removing the items from Backpack
my_backpack.remove_item("Waterbottle")
print(items)
my_backpack.remove_item("Books")
print(items)
my_backpack.remove_item("Pencilbox")
print(items)
```

***Output***
```
[]
['Books']
['Books', 'Waterbottle']
True
Waterbottle is removed
['Books']
Books is removed
[]
Pencilbox not in the backpack
[]
```

***Note: `<ClassName>.<method_name>(<instance>, <args>)` is also a valid syntax to call the method***

### Non-public methods

- Methods can follow the same procedure as attributes for non-public methods
- Non-public method can use single or double underscores accordingly

***Example***

```
def _display_data(self):
    # code

def __display_account_balance(self):
    # code
```

### Default value for argument in method

- we can add the default value to a method's parameter
- The parameter with default value should be at the end of the list

***Example Syntax***
```
def <method_name>(self, <param1>=<value>):
    #code
```

***Example with `Backpack` class***

For default argument example we could use the same `Backpack` class example. We are going to create a method `show_items` with default argument `sorted_list=False`. This method would display the list in the backpack instance unsorted if the user don't pass any argument to the method. If the user use `True` as the value in the method argument then the program would return sorted list

```
    def show_items(self, sorted_list=False):
        if sorted_list:
            print(sorted(self._items))
        else:
            print(self._items)
```

To access these methods we could do something like below,
```
# Un sorted list Using show_items
my_backpack.show_items()

# sorted list Using show_items
my_backpack.show_items(True)
```

***Output***
```
['Waterbottle', 'Books']
['Books', 'Waterbottle']
```

The first line of the output is unsorted list and the second line of output is sorted list.

### Calling a method from another method

- We could call a method from another method in the class
- This helps in reusing the functionality which was already created
- `self.<method_name>(<arguments>)` - This is the syntax for calling a method from another method

***Example***
Let's take the same `Backpack` class for this example. we are going to create a method and call another method inside that 

```
    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Input is not valid item")

    def add_multiple_items(self, items):
        for item in items:
            self.add_item(item)
```

In the above example snippet, we could see we have two methods `add_item` and `add_multiple_items`. `add_item` typically takes a parameter `item` and append to the list of items in backpack object. In `add_multiple_items` we are planning to pass a list of items and we call `add_item` method as `self.add_item(item)` in for loop of the list we passed. which would call the actual funtion for every iteration and add the item to backpack object


### Aggregation

- Concept in object oriented programming that describes the relationship between two classes
- Building complex object that are composed of other objects
- We store instances of the simpler objects in the more complex objects
- It's a "has a" relationship between the class. An object of class B has an object of class A

***Example***

*Employee and Vehicle* 
An employee has a vehicle. 
Here employee is an object of a class (`Employee`) and vehicle is an object of another class (`Vehicle`). But the employee needs the information of vehicle

***Example***
```
class Vehicle:

    def __init__(self, color, license_plate, is_electric):
        self.color = color
        self.license_plate = license_plate
        self.is_electric = is_electric

    def show_license(self):
        print(self.license_plate)

    def show_info(self):
        print("Vehicle Info:")
        print(f"Color - {self.color}")
        print(f"License Plate - {self.license_plate}")
        print(f"Is Electric - {self.is_electric}")

class Employee:

    def __init__(self, name, employee_no, vehicle):
        self.name = name
        self.employee_no = employee_no
        self.vehicle = vehicle

    def show_employee(self):
        print("Employee Info:")
        print(f"Name - {self.name}")
        print(f"Employee No - {self.employee_no}")

    def show_vehicle_info(self):
        self.vehicle.show_info()
```

- The above code has couple of classes. 
- `Vehicle` class (simple class) with `Employee` class (complex class) has been created. 
- In `Vehicle` class `__init__()` method we have three instance attributes `color, license_plate, is_electric`
- `Vehicle` class has two methods. `show_license()` which shows the `license_plate` attribute and `show_info()` method which displays all the attributes of `Vehicle` class
- `Employee` class `__init__()` method has three attributes `name, employee_no, vehicle`
- Here `name` and `employee_no` is a standalone instance attributes. however, `vehicle` is the object instance of `Vehicle` class. This is aggregation
- We have two methods in `Employee` class. `show_employee` method would show the employee detail. `show_vehicle_info` is the method which uses aggregation. 
- `show_vehicle_info` method just has one line `self.vehicle.show_info()`. here we are just referring the `self.vehicle` which is just the vehicle object. `show_info()` is the method from the `Vehicle` class
- Now let's see how we call the methods of `Vehicle` class from `Employee` class object instance


```
employee_vehicle = Vehicle("Blue", "TN 19 V 0531", is_electric=False)
employee = Employee("Sundar", 113453, employee_vehicle)

print(employee.name)
print(employee.employee_no)

print("___________________")

employee.show_employee()
employee.show_vehicle_info()

print("___________________")

print(employee.vehicle.color)
print(employee.vehicle.license_plate)
print(employee.vehicle.is_electric)
```

- We first instantiate `employee_vehicle` instance by passing the attributes as parameter
- Then we create `employee` instance with name and employee_no. For the third parameter/attribute we just simply pass the vehicle object instance name. In our case it's `employee_vehicle`. which we created in previous step
- Now the Aggregation is set between both `Employee` and `Vehicle` class. we could access any methods, attributes of `Vehicle` class from employee instances
- We could access the `show_vehicle_info` which would take the values from `Vehicle` class
- Similarly we could access the vehicle instance attributes by using this format `employee.vehicle.color`. (i.e, <employee_instance>.<employee_vehicle_instance_attribute>.<vehicle_instance_attribute>)

