import streamlit as st
from abc import ABC, abstractmethod


# ============================================================
# Assignment 1: Using `self`
# ============================================================
class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def display(self) -> str:
        return f"Student Name: {self.name}, Marks: {self.marks}"


# ============================================================
# Assignment 2: Using `cls`
# ============================================================
class Counter:
    count: int = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls) -> int:
        return cls.count

    @classmethod
    def reset(cls):
        cls.count = 0


# ============================================================
# Assignment 3: Public Variables and Methods
# ============================================================
class Car:
    def __init__(self, brand: str):
        self.brand = brand

    def start(self) -> str:
        return f"{self.brand} car has started!"


# ============================================================
# Assignment 4: Class Variables and Class Methods
# ============================================================
class Bank:
    bank_name: str = "Default Bank"

    @classmethod
    def change_bank_name(cls, name: str):
        cls.bank_name = name


# ============================================================
# Assignment 5: Static Variables and Static Methods
# ============================================================
class MathUtils:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b


# ============================================================
# Assignment 6: Constructors and Destructors
# ============================================================
class Logger:
    def __init__(self, name: str):
        self.name = name
        self._creation_msg = f"Logger '{self.name}' created!"

    def get_creation_message(self) -> str:
        return self._creation_msg

    def __del__(self):
        print(f"Logger '{self.name}' destroyed!")


# ============================================================
# Assignment 7: Access Modifiers (Public, Protected, Private)
# ============================================================
class Employee:
    def __init__(self, name: str, salary: float, ssn: str):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

    def get_ssn(self) -> str:
        return self.__ssn

    def get_info(self) -> dict:
        return {
            "name (public)": self.name,
            "_salary (protected)": self._salary,
            "__ssn (private)": self.__ssn,
        }


# ============================================================
# Assignment 8: The `super()` Function
# ============================================================
class Person:
    def __init__(self, name: str):
        self.name = name


class Teacher(Person):
    def __init__(self, name: str, subject: str):
        super().__init__(name)
        self.subject = subject

    def display(self) -> str:
        return f"Teacher: {self.name}, Subject: {self.subject}"


# ============================================================
# Assignment 9: Abstract Classes and Methods
# ============================================================
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


# ============================================================
# Assignment 10: Instance Methods
# ============================================================
class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    def bark(self) -> str:
        return f"{self.name} ({self.breed}) says: Woof! Woof!"


# ============================================================
# Assignment 11: Class Methods
# ============================================================
class Book:
    total_books: int = 0

    def __init__(self, title: str):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls) -> int:
        return cls.total_books

    @classmethod
    def reset(cls):
        cls.total_books = 0


# ============================================================
# Assignment 12: Static Methods
# ============================================================
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c: float) -> float:
        return (c * 9 / 5) + 32


# ============================================================
# Assignment 13: Composition
# ============================================================
class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

    def start(self) -> str:
        return f"Engine with {self.horsepower} HP started!"


class ComposedCar:
    def __init__(self, brand: str, engine: Engine):
        self.brand = brand
        self.engine = engine

    def start(self) -> str:
        return f"{self.brand} -> {self.engine.start()}"


# ============================================================
# Assignment 14: Aggregation
# ============================================================
class AggEmployee:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return self.name


class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: list[AggEmployee] = []

    def add_employee(self, emp: AggEmployee):
        self.employees.append(emp)

    def list_employees(self) -> list[str]:
        return [e.name for e in self.employees]


# ============================================================
# Assignment 15: Method Resolution Order (MRO)
# ============================================================
class A:
    def show(self) -> str:
        return "A.show() called"


class B(A):
    def show(self) -> str:
        return "B.show() called"


class C(A):
    def show(self) -> str:
        return "C.show() called"


class D(B, C):
    pass


# ============================================================
# Assignment 16: Function Decorators
# ============================================================
def log_function_call(func):
    def wrapper(*args, **kwargs):
        log = "Function is being called"
        result = func(*args, **kwargs)
        return log, result
    return wrapper


@log_function_call
def say_hello() -> str:
    return "Hello!"


# ============================================================
# Assignment 17: Class Decorators
# ============================================================
def add_greeting(cls):
    def greet(self) -> str:
        return "Hello from Decorator!"
    cls.greet = greet
    return cls


@add_greeting
class PersonDecorated:
    def __init__(self, name: str):
        self.name = name


# ============================================================
# Assignment 18: Property Decorators
# ============================================================
class Product:
    def __init__(self, price: float):
        self._price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

    @price.deleter
    def price(self):
        self._price = 0


# ============================================================
# Assignment 19: callable() and __call__()
# ============================================================
class Multiplier:
    def __init__(self, factor: int):
        self.factor = factor

    def __call__(self, value: float) -> float:
        return value * self.factor


# ============================================================
# Assignment 20: Custom Exceptions
# ============================================================
class InvalidAgeError(Exception):
    def __init__(self, age: int, message: str = "Age must be 18 or older"):
        self.age = age
        self.message = message
        super().__init__(self.message)


def check_age(age: int) -> str:
    if age < 18:
        raise InvalidAgeError(age)
    return f"Age {age} is valid. Access granted!"


# ============================================================
# Assignment 21: Custom Class Iteration
# ============================================================
class Countdown:
    def __init__(self, start: int):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


# ============================================================
# STREAMLIT APP
# ============================================================
st.set_page_config(page_title="OOP Practice Series", page_icon="🐍", layout="wide")

st.title("🐍 Build, Compose & Decorate — Complete OOP Practice Series")
st.markdown("**Assignment 6** — All 21 OOP concepts implemented in Python")

st.sidebar.title("📚 Assignments")
assignments = [
    "1. Using self",
    "2. Using cls",
    "3. Public Variables & Methods",
    "4. Class Variables & Class Methods",
    "5. Static Variables & Static Methods",
    "6. Constructors & Destructors",
    "7. Access Modifiers",
    "8. The super() Function",
    "9. Abstract Classes & Methods",
    "10. Instance Methods",
    "11. Class Methods",
    "12. Static Methods",
    "13. Composition",
    "14. Aggregation",
    "15. Method Resolution Order (MRO)",
    "16. Function Decorators",
    "17. Class Decorators",
    "18. Property Decorators",
    "19. callable() & __call__()",
    "20. Custom Exceptions",
    "21. Custom Iteration",
]
choice = st.sidebar.radio("Select Assignment", assignments)


# ── Helper ──
def show_code(code: str):
    st.code(code, language="python")


# ────────────────────────────────────────────────────────────
# 1. Using self
# ────────────────────────────────────────────────────────────
if choice == assignments[0]:
    st.header("1️⃣ Using `self`")
    st.markdown("A `Student` class using `self` to access instance attributes.")

    show_code("""class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def display(self) -> str:
        return f"Student Name: {self.name}, Marks: {self.marks}"
""")

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Student Name", "Ali")
    with col2:
        marks = st.number_input("Marks", min_value=0, max_value=100, value=85)

    if st.button("Create Student", key="btn1"):
        s = Student(name, int(marks))
        st.success(s.display())


# ────────────────────────────────────────────────────────────
# 2. Using cls
# ────────────────────────────────────────────────────────────
elif choice == assignments[1]:
    st.header("2️⃣ Using `cls`")
    st.markdown("A `Counter` class tracking how many objects are created using a class method with `cls`.")

    show_code("""class Counter:
    count: int = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls) -> int:
        return cls.count
""")

    Counter.reset()
    num = st.slider("How many objects to create?", 1, 20, 5)
    if st.button("Create Objects", key="btn2"):
        for _ in range(num):
            Counter()
        st.success(f"Total objects created: {Counter.get_count()}")


# ────────────────────────────────────────────────────────────
# 3. Public Variables and Methods
# ────────────────────────────────────────────────────────────
elif choice == assignments[2]:
    st.header("3️⃣ Public Variables & Methods")
    st.markdown("A `Car` class with public variable `brand` and public method `start()`.")

    show_code("""class Car:
    def __init__(self, brand: str):
        self.brand = brand  # public variable

    def start(self) -> str:  # public method
        return f"{self.brand} car has started!"
""")

    brand = st.text_input("Car Brand", "Toyota")
    if st.button("Start Car", key="btn3"):
        car = Car(brand)
        st.info(f"Accessing public variable — `car.brand` = **{car.brand}**")
        st.success(f"Calling public method — `car.start()` = {car.start()}")


# ────────────────────────────────────────────────────────────
# 4. Class Variables and Class Methods
# ────────────────────────────────────────────────────────────
elif choice == assignments[3]:
    st.header("4️⃣ Class Variables & Class Methods")
    st.markdown("A `Bank` class with class variable `bank_name` and class method `change_bank_name()`.")

    show_code("""class Bank:
    bank_name: str = "Default Bank"

    @classmethod
    def change_bank_name(cls, name: str):
        cls.bank_name = name
""")

    Bank.bank_name = "Default Bank"
    st.info(f"Current bank name: **{Bank.bank_name}**")

    new_name = st.text_input("New Bank Name", "Meezan Bank")
    if st.button("Change Bank Name", key="btn4"):
        Bank.change_bank_name(new_name)
        b1 = Bank()
        b2 = Bank()
        st.success(f"After change — Bank.bank_name = **{Bank.bank_name}**")
        st.info("All instances share the same class variable — change affects everyone!")


# ────────────────────────────────────────────────────────────
# 5. Static Variables and Static Methods
# ────────────────────────────────────────────────────────────
elif choice == assignments[4]:
    st.header("5️⃣ Static Variables & Static Methods")
    st.markdown("A `MathUtils` class with static method `add(a, b)`.")

    show_code("""class MathUtils:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b
""")

    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("Number A", value=10.0)
    with col2:
        b = st.number_input("Number B", value=20.0)

    if st.button("Add Numbers", key="btn5"):
        result = MathUtils.add(a, b)
        st.success(f"MathUtils.add({a}, {b}) = **{result}**")


# ────────────────────────────────────────────────────────────
# 6. Constructors and Destructors
# ────────────────────────────────────────────────────────────
elif choice == assignments[5]:
    st.header("6️⃣ Constructors & Destructors")
    st.markdown("A `Logger` class that prints on creation (`__init__`) and destruction (`__del__`).")

    show_code("""class Logger:
    def __init__(self, name: str):
        self.name = name
        print(f"Logger '{self.name}' created!")

    def __del__(self):
        print(f"Logger '{self.name}' destroyed!")
""")

    logger_name = st.text_input("Logger Name", "MyLogger")
    if st.button("Create & Destroy Logger", key="btn6"):
        logger = Logger(logger_name)
        st.success(f"Constructor: {logger.get_creation_message()}")
        del logger
        st.warning(f"Destructor: Logger '{logger_name}' destroyed!")


# ────────────────────────────────────────────────────────────
# 7. Access Modifiers
# ────────────────────────────────────────────────────────────
elif choice == assignments[6]:
    st.header("7️⃣ Access Modifiers")
    st.markdown("An `Employee` class demonstrating **public**, **protected**, and **private** access.")

    show_code("""class Employee:
    def __init__(self, name: str, salary: float, ssn: str):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

    def get_ssn(self) -> str:
        return self.__ssn
""")

    col1, col2, col3 = st.columns(3)
    with col1:
        emp_name = st.text_input("Name", "Ahmed")
    with col2:
        emp_salary = st.number_input("Salary", value=50000.0)
    with col3:
        emp_ssn = st.text_input("SSN", "123-45-6789")

    if st.button("Create Employee", key="btn7"):
        emp = Employee(emp_name, emp_salary, emp_ssn)

        st.success(f"**Public** `emp.name` = {emp.name}")
        st.warning(f"**Protected** `emp._salary` = {emp._salary}  _(accessible but convention says don't)_")
        st.error(f"**Private** `emp.__ssn` → AttributeError!  Use `emp.get_ssn()` = {emp.get_ssn()}")


# ────────────────────────────────────────────────────────────
# 8. The super() Function
# ────────────────────────────────────────────────────────────
elif choice == assignments[7]:
    st.header("8️⃣ The `super()` Function")
    st.markdown("`Teacher` inherits from `Person` and uses `super().__init__()` to initialize the parent.")

    show_code("""class Person:
    def __init__(self, name: str):
        self.name = name

class Teacher(Person):
    def __init__(self, name: str, subject: str):
        super().__init__(name)
        self.subject = subject

    def display(self) -> str:
        return f"Teacher: {self.name}, Subject: {self.subject}"
""")

    col1, col2 = st.columns(2)
    with col1:
        t_name = st.text_input("Teacher Name", "Sir Zia")
    with col2:
        t_subject = st.text_input("Subject", "AI Python")

    if st.button("Create Teacher", key="btn8"):
        t = Teacher(t_name, t_subject)
        st.success(t.display())


# ────────────────────────────────────────────────────────────
# 9. Abstract Classes and Methods
# ────────────────────────────────────────────────────────────
elif choice == assignments[8]:
    st.header("9️⃣ Abstract Classes & Methods")
    st.markdown("Abstract `Shape` class with concrete `Rectangle` implementation.")

    show_code("""from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height
""")

    col1, col2 = st.columns(2)
    with col1:
        width = st.number_input("Width", min_value=0.1, value=5.0)
    with col2:
        height = st.number_input("Height", min_value=0.1, value=3.0)

    if st.button("Calculate Area", key="btn9"):
        rect = Rectangle(width, height)
        st.success(f"Rectangle area = {width} x {height} = **{rect.area()}**")
        st.info("Trying to instantiate `Shape()` directly would raise `TypeError` — it's abstract!")


# ────────────────────────────────────────────────────────────
# 10. Instance Methods
# ────────────────────────────────────────────────────────────
elif choice == assignments[9]:
    st.header("🔟 Instance Methods")
    st.markdown("A `Dog` class with instance method `bark()`.")

    show_code("""class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    def bark(self) -> str:
        return f"{self.name} ({self.breed}) says: Woof! Woof!"
""")

    col1, col2 = st.columns(2)
    with col1:
        dog_name = st.text_input("Dog Name", "Bruno")
    with col2:
        dog_breed = st.text_input("Breed", "German Shepherd")

    if st.button("Make Dog Bark", key="btn10"):
        dog = Dog(dog_name, dog_breed)
        st.success(dog.bark())


# ────────────────────────────────────────────────────────────
# 11. Class Methods
# ────────────────────────────────────────────────────────────
elif choice == assignments[10]:
    st.header("1️⃣1️⃣ Class Methods")
    st.markdown("A `Book` class with class method to track total books.")

    show_code("""class Book:
    total_books: int = 0

    def __init__(self, title: str):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls) -> int:
        return cls.total_books
""")

    Book.reset()
    books_input = st.text_area("Enter book titles (one per line)", "Python Crash Course\nClean Code\nDesign Patterns")

    if st.button("Add Books", key="btn11"):
        titles = [t.strip() for t in books_input.strip().split("\n") if t.strip()]
        for title in titles:
            Book(title)
        st.success(f"Total books added: **{Book.get_total_books()}**")


# ────────────────────────────────────────────────────────────
# 12. Static Methods
# ────────────────────────────────────────────────────────────
elif choice == assignments[11]:
    st.header("1️⃣2️⃣ Static Methods")
    st.markdown("`TemperatureConverter` with static method `celsius_to_fahrenheit()`.")

    show_code("""class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c: float) -> float:
        return (c * 9 / 5) + 32
""")

    celsius = st.number_input("Temperature in Celsius", value=37.0)
    if st.button("Convert", key="btn12"):
        f = TemperatureConverter.celsius_to_fahrenheit(celsius)
        st.success(f"{celsius}°C = **{f}°F**")


# ────────────────────────────────────────────────────────────
# 13. Composition
# ────────────────────────────────────────────────────────────
elif choice == assignments[12]:
    st.header("1️⃣3️⃣ Composition")
    st.markdown("`Car` **has-a** `Engine` — Engine is part of Car (composition).")

    show_code("""class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

    def start(self) -> str:
        return f"Engine with {self.horsepower} HP started!"

class Car:
    def __init__(self, brand: str, engine: Engine):
        self.brand = brand
        self.engine = engine  # Composition

    def start(self) -> str:
        return f"{self.brand} -> {self.engine.start()}"
""")

    col1, col2 = st.columns(2)
    with col1:
        car_brand = st.text_input("Car Brand", "Honda")
    with col2:
        hp = st.number_input("Engine Horsepower", min_value=50, max_value=1000, value=180)

    if st.button("Start Car", key="btn13"):
        engine = Engine(int(hp))
        car = ComposedCar(car_brand, engine)
        st.success(car.start())


# ────────────────────────────────────────────────────────────
# 14. Aggregation
# ────────────────────────────────────────────────────────────
elif choice == assignments[13]:
    st.header("1️⃣4️⃣ Aggregation")
    st.markdown("`Department` **uses** `Employee` objects — employees exist independently (aggregation).")

    show_code("""class Employee:
    def __init__(self, name: str):
        self.name = name

class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: list[Employee] = []

    def add_employee(self, emp: Employee):
        self.employees.append(emp)

    def list_employees(self) -> list[str]:
        return [e.name for e in self.employees]
""")

    dept_name = st.text_input("Department Name", "Engineering")
    emp_names = st.text_area("Employee Names (one per line)", "Ali\nSara\nAhmed")

    if st.button("Create Department", key="btn14"):
        dept = Department(dept_name)
        for name in emp_names.strip().split("\n"):
            if name.strip():
                dept.add_employee(AggEmployee(name.strip()))
        st.success(f"**{dept.name}** Department Employees: {dept.list_employees()}")


# ────────────────────────────────────────────────────────────
# 15. Method Resolution Order (MRO)
# ────────────────────────────────────────────────────────────
elif choice == assignments[14]:
    st.header("1️⃣5️⃣ Method Resolution Order (MRO)")
    st.markdown("Diamond inheritance: `D -> B -> C -> A`. Which `show()` gets called?")

    show_code("""class A:
    def show(self) -> str:
        return "A.show() called"

class B(A):
    def show(self) -> str:
        return "B.show() called"

class C(A):
    def show(self) -> str:
        return "C.show() called"

class D(B, C):
    pass  # inherits from B and C
""")

    if st.button("Call D().show()", key="btn15"):
        d = D()
        st.success(f"Result: **{d.show()}**")
        st.info(f"MRO: {[cls.__name__ for cls in D.__mro__]}")
        st.markdown("Python uses **C3 Linearization** — `D` checks `B` first, then `C`, then `A`.")


# ────────────────────────────────────────────────────────────
# 16. Function Decorators
# ────────────────────────────────────────────────────────────
elif choice == assignments[15]:
    st.header("1️⃣6️⃣ Function Decorators")
    st.markdown("A `log_function_call` decorator that logs before function execution.")

    show_code("""def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_function_call
def say_hello() -> str:
    return "Hello!"
""")

    if st.button("Call say_hello()", key="btn16"):
        log_msg, result = say_hello()
        st.warning(f"Decorator log: *{log_msg}*")
        st.success(f"Function returned: **{result}**")


# ────────────────────────────────────────────────────────────
# 17. Class Decorators
# ────────────────────────────────────────────────────────────
elif choice == assignments[16]:
    st.header("1️⃣7️⃣ Class Decorators")
    st.markdown("An `add_greeting` decorator that adds a `greet()` method to any class.")

    show_code("""def add_greeting(cls):
    def greet(self) -> str:
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name: str):
        self.name = name
""")

    name = st.text_input("Person Name", "Asfar", key="name17")
    if st.button("Create & Greet", key="btn17"):
        p = PersonDecorated(name)
        st.success(f"**{p.name}** says: {p.greet()}")
        st.info("The `greet()` method was added by the `@add_greeting` decorator!")


# ────────────────────────────────────────────────────────────
# 18. Property Decorators
# ────────────────────────────────────────────────────────────
elif choice == assignments[17]:
    st.header("1️⃣8️⃣ Property Decorators")
    st.markdown("`Product` class with `@property` getter, `@price.setter`, and `@price.deleter`.")

    show_code("""class Product:
    def __init__(self, price: float):
        self._price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

    @price.deleter
    def price(self):
        self._price = 0
""")

    initial_price = st.number_input("Initial Price", value=100.0)
    new_price = st.number_input("Set New Price", value=200.0)

    if st.button("Demo Property", key="btn18"):
        product = Product(initial_price)
        st.info(f"**Getter** — `product.price` = {product.price}")

        try:
            product.price = new_price
            st.success(f"**Setter** — Updated to {product.price}")
        except ValueError as e:
            st.error(f"**Setter** — {e}")

        del product.price
        st.warning(f"**Deleter** — After deletion, price = {product.price}")


# ────────────────────────────────────────────────────────────
# 19. callable() and __call__()
# ────────────────────────────────────────────────────────────
elif choice == assignments[18]:
    st.header("1️⃣9️⃣ `callable()` & `__call__()`")
    st.markdown("`Multiplier` class — instances are callable like functions!")

    show_code("""class Multiplier:
    def __init__(self, factor: int):
        self.factor = factor

    def __call__(self, value: float) -> float:
        return value * self.factor
""")

    col1, col2 = st.columns(2)
    with col1:
        factor = st.number_input("Multiplier Factor", value=3, min_value=1)
    with col2:
        value = st.number_input("Value to Multiply", value=10.0)

    if st.button("Multiply!", key="btn19"):
        m = Multiplier(int(factor))
        st.info(f"`callable(m)` = **{callable(m)}**")
        st.success(f"`m({value})` = {value} x {factor} = **{m(value)}**")


# ────────────────────────────────────────────────────────────
# 20. Custom Exceptions
# ────────────────────────────────────────────────────────────
elif choice == assignments[19]:
    st.header("2️⃣0️⃣ Custom Exceptions")
    st.markdown("`InvalidAgeError` — raises if age < 18.")

    show_code("""class InvalidAgeError(Exception):
    def __init__(self, age: int, message: str = "Age must be 18 or older"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def check_age(age: int) -> str:
    if age < 18:
        raise InvalidAgeError(age)
    return f"Age {age} is valid. Access granted!"
""")

    age = st.number_input("Enter Age", min_value=0, max_value=120, value=16)
    if st.button("Check Age", key="btn20"):
        try:
            result = check_age(int(age))
            st.success(result)
        except InvalidAgeError as e:
            st.error(f"InvalidAgeError: {e.message} (you entered {e.age})")


# ────────────────────────────────────────────────────────────
# 21. Custom Class Iteration
# ────────────────────────────────────────────────────────────
elif choice == assignments[20]:
    st.header("2️⃣1️⃣ Custom Class Iteration")
    st.markdown("`Countdown` class with `__iter__()` and `__next__()` for iteration.")

    show_code("""class Countdown:
    def __init__(self, start: int):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
""")

    start = st.number_input("Countdown from", min_value=1, max_value=50, value=5)
    if st.button("Start Countdown", key="btn21"):
        countdown = Countdown(int(start))
        values = list(countdown)
        st.success(f"Countdown: {' -> '.join(map(str, values))}")


# ── Footer ──
st.sidebar.markdown("---")
st.sidebar.markdown("Made with Python + Streamlit")
st.sidebar.markdown("**UV + Streamlit Project**")
