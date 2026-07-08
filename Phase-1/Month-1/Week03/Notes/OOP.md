# Python OOP — From "What Is It?" to the Last Concept

One short explanation per idea, in teaching order, each with exactly
one easy example.

---

## 0. What is OOP?

**Object-Oriented Programming** is a way of organizing code around
**objects** — bundles of data and the behavior that belongs with that
data — instead of writing one long list of separate variables and
functions.

**Procedural style** (before OOP): data and functions are separate.
```python
name = "Rex"
age = 3

def describe(name, age):
    return f"{name} is {age} years old"
```

**OOP style**: the data and the function that uses it live together in
one unit.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} years old"
```

Why bother? Once you have many "things" in your program (dogs,
employees, network devices...), OOP keeps each thing's data and
behavior organized together, instead of scattered across loose
variables and functions that all need to be passed around manually.

---

## 1. Classes and Objects

A **class** is the blueprint. An **object** (instance) is one real
thing built from that blueprint.
```python
class Dog:
    pass

rex = Dog()      # rex is an object (instance) of class Dog
buddy = Dog()     # a completely separate object
```

## 2. Attributes, Methods, and `self`

**Attributes** = the data an object stores. **Methods** = functions
that belong to the class. **`self`** = "this particular object,"
automatically passed into every method.
```python
class Dog:
    def __init__(self, name):
        self.name = name        # attribute

    def bark(self):              # method
        return f"{self.name} says Woof!"

rex = Dog("Rex")
print(rex.bark())                # Rex says Woof!
```

## 3. Combining Objects

An object can hold another object as one of its attributes.
```python
class Engine:
    def start(self):
        return "Vroom!"

class Car:
    def __init__(self):
        self.engine = Engine()   # Car "has an" Engine

my_car = Car()
print(my_car.engine.start())     # Vroom!
```

## 4. Accessing and Modifying Object Data

By default, you can read and change an object's attributes directly
with a dot, from anywhere.
```python
rex.name = "Max"       # changed directly, no restrictions yet
print(rex.name)        # Max
```
This is convenient but risky — nothing stops you from setting a
nonsense value. That's the problem the next few concepts solve.

## 5. Protected Attributes (`_name`)

A single leading underscore is a **convention**: "please don't touch
this from outside the class." Python doesn't actually block it — it's
a signal, not a lock.
```python
class Dog:
    def __init__(self, name):
        self._name = name   # "protected" by convention only
```
**When to use it:** whenever the attribute is meant for internal use
or for subclasses, but you don't need to strictly forbid outside
access.

## 6. Private Attributes (`__name`) and "Consenting Adults"

A double leading underscore triggers **name mangling** — Python
renames it internally to `_ClassName__name`, making outside access
much harder (though never fully impossible).

Python's **"Consenting Adults"** philosophy: the language trusts
programmers to respect conventions rather than locking everything down
with strict enforcement like some other languages do.
```python
class Dog:
    def __init__(self, name):
        self.__name = name   # harder to reach from outside

d = Dog("Rex")
# d.__name        -> would raise an AttributeError
print(d._Dog__name)  # still technically reachable, but ugly on purpose
```
**Protected vs private, in short:** use protected (`_x`) for "internal,
but subclasses may still need it." Use private (`__x`) for "truly just
this class's business, nobody else should touch it."

## 7. Getters and Setters (Classic Style)

Plain methods used to read/write a value indirectly, so you can add
validation logic.
```python
class Dog:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0:
            raise ValueError("Age can't be negative")
        self.__age = value
```
**Why bother**, instead of just making the attribute public? Because
this way, nobody can sneak in a bad value (like a negative age) without
going through your check first.

## 8. Properties (`@property`)

The modern version of getters/setters — it looks like a normal
attribute from the outside, but still runs your validation code.
```python
class Dog:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age can't be negative")
        self._age = value

d = Dog(3)
d.age = 5        # looks like a plain attribute, but the setter runs
```
**Properties vs classic getters/setters:** same purpose (controlled
access), but properties use normal-looking dot syntax (`d.age = 5`)
instead of explicit method calls (`d.set_age(5)`) — cleaner to read
and write.

## 9. Static Attributes (Class Attributes)

A value shared by **every** object of the class, not copied per
instance — e.g. a running total.
```python
class Dog:
    total_dogs = 0            # shared by ALL dogs

    def __init__(self, name):
        self.name = name        # unique per dog (instance attribute)
        Dog.total_dogs += 1

Dog("Rex")
Dog("Max")
print(Dog.total_dogs)         # 2
```

## 10. Static Methods (`@staticmethod`)

A method that doesn't need `self` (or the class) at all — it's just a
regular function grouped inside the class because it's related.
```python
class Dog:
    @staticmethod
    def is_valid_name(name):
        return len(name) > 0

print(Dog.is_valid_name("Rex"))   # True, no Dog object needed
```
**When to use it:** anytime the logic doesn't need any of the object's
or class's own data to do its job.

## 11. Class Methods (`@classmethod`)

A method that receives the **class itself** (`cls`) instead of an
object. The most common use: an alternate way to build an object.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, text):
        name, age = text.split(",")
        return cls(name, int(age))

rex = Dog.from_string("Rex,3")
```

## 12. Protected and Private Methods

The same underscore rules from attributes also apply to methods.
`_helper()` signals "internal use"; `__helper()` gets name-mangled.
Often used for logic meant to be overridden by subclasses, or internal
steps the outside world shouldn't call directly.
```python
class Dog:
    def make_sound(self):
        return self._sound_effect()   # public method uses a helper

    def _sound_effect(self):           # protected helper
        return "Woof!"
```

## 13. Encapsulation

The umbrella principle behind everything from sections 5–12: keep data
and the methods that manage it bundled together, and hide internal
details so outside code can only interact through a safe, controlled
interface.

**Why it matters:** it prevents invalid states (like a negative age)
and lets you change how something works internally later without
breaking code that uses it — as long as the public interface stays the
same.

## 14. Abstraction

A class marked as **abstract** can never be turned into an object
directly — it only exists to define a contract: "every subclass of me
must implement these specific methods."
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Shape()   -> TypeError: can't instantiate an abstract class
```

## 15. Inheritance

A class can inherit attributes and methods from another class,
avoiding repeated code and modeling "is-a" relationships.
```python
class Animal:
    def eat(self):
        return "Eating..."

class Dog(Animal):     # Dog "is an" Animal
    pass

rex = Dog()
print(rex.eat())        # inherited from Animal
```

## 16. `super()`

Lets a subclass call its parent's version of a method — useful for
*extending* the parent's behavior instead of fully replacing it.
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # let Animal handle "name"
        self.breed = breed
```

## 17. Multiple Inheritance

A class can inherit from **more than one** parent class at once.
```python
class Swimmer:
    def swim(self):
        return "Swimming"

class Walker:
    def walk(self):
        return "Walking"

class Duck(Swimmer, Walker):    # gets both abilities
    pass
```

## 18. Polymorphism

Different classes can implement the *same* method name in their own
way, and you can call it on any of them without checking which type it
is first.
```python
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

for animal in [Cat(), Dog()]:
    print(animal.speak())   # each one speaks differently
```
**Small bonus tip:** you can use type hints to document that a list
should only contain one base type, e.g. `def inspect(vehicles: list[Vehicle])`
— Python won't enforce it at runtime, but it helps readers (and your
editor) understand the intent.

## 19. Duck Typing

"If it walks like a duck and quacks like a duck, treat it as a duck."
Python doesn't check an object's exact type before calling a method —
it just tries. If the method exists, it works; if not, you get a
natural `AttributeError`.
```python
def make_it_speak(thing):
    return thing.speak()   # works on ANY object with a .speak() method
```

## 20. Composition

One object **creates and owns** another object internally — the inner
object's life is tied to the outer one.
```python
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()   # Car creates its own Engine
```

## 21. Aggregation

One object **holds a reference** to other objects that already existed
on their own — the container doesn't own their lifecycle.
```python
class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)   # song already existed before this

song1 = "Bohemian Rhapsody"        # created independently
my_playlist = Playlist()
my_playlist.add_song(song1)         # just referenced, not owned
```
**Composition vs aggregation, in short:** composition = "I made you,
you're mine." Aggregation = "I just know about you; you existed
before me and you'll exist after me."

## 22. Nested Classes

A class defined **inside** another class — usually a small helper
structure that only makes sense in that context.
```python
class Device:
    class LogEntry:
        def __init__(self, timestamp, status):
            self.timestamp = timestamp
            self.status = status

    def __init__(self):
        self.last_log = None

    def log(self, timestamp, status):
        self.last_log = Device.LogEntry(timestamp, status)
```

## 23. Magic (Dunder) Methods

Special methods surrounded by double underscores that let your objects
work with Python's built-in syntax (`print()`, `==`, etc.) instead of
needing custom-named methods for everything.
```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):                 # controls print(obj)
        return f"({self.x}, {self.y})"

    def __eq__(self, other):           # controls obj1 == obj2
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
print(p1)              # (1, 2)  <- uses __str__ automatically
```

---

## Conclusion: The Big Picture

Everything above builds toward four pillars:

| Pillar | Built from |
|---|---|
| **Encapsulation** | protected/private attributes & methods, getters/setters, properties |
| **Abstraction** | abstract classes (`ABC`, `@abstractmethod`) |
| **Inheritance** | inheritance, `super()`, multiple inheritance |
| **Polymorphism** | polymorphism, duck typing |

And two extra practical skills that sit alongside the four pillars:
**object relationships** (composition, aggregation, nested classes,
combining objects) and **class-level tools** (static attributes/
methods, class methods, magic methods) that make classes more powerful
and convenient to use.