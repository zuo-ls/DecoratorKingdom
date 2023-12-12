"""
This file contains some useful decorators.
    - classproperty: a decorator for classmethod + property
    - superclassmethod: a decorator for class methods with super behavior.
"""

class classproperty(object):
    """
    a decorator for classmethod + property
    """
    def __init__(self, f):
        self.f = f
    def __get__(self, obj, owner):
        """
        obj: instance of the class
        owner: class itself
        """
        return self.f(owner)

class superclassmethod(object):
    """
    A decorator for class methods with super behavior.

    This decorator checks if the class containing the method is a subclass of base_class.
    If it is, then it checks if the method is defined in the base class
    and it calls the super method first and then the decorated method.

    Args:
        return_super (bool): If True, the decorated method will return a tuple of (super_result, result).
            If False, the decorated method will return result only. Default: False.
    
    Example:
    
    class Base_A:
    def foo(self):
        print("Base_A foo")

    @superclassmethod(return_super=False)
    def foo(cls):
        print("A foo")

    class A(Base_A):
        foo = foo

    class B:
        foo = foo

    a = A()
    print(a.foo())
    print('-----')
    b = B()
    print(b.foo())
    """
    def __init__(self, f=None, return_super=False):
        self.f = f
        self.return_super = return_super

    def __call__(self, f):
        self.f = f
        return self

    def __get__(self, obj, owner):
        """
        obj: instance of the class
        owner: class itself
        """
        def wrapped(*args, **kwargs):
            # Check if owner has a superclass and if the same function is defined in the superclass
            if hasattr(owner, '__bases__') and any(hasattr(base, self.f.__name__) for base in owner.__bases__):
                # If yes, call the superclass's function using super()
                super_func = getattr(super(owner, obj), self.f.__name__, None)
                if callable(super_func):
                    super_result = super_func(*args, **kwargs)
                else:
                    super_result = None
                # Execute the decorated function
                result = self.f(owner, *args, **kwargs)
                return (super_result, result) if self.return_super else result
            else:
                # If there's no superclass with the same function, just execute the decorated function
                return self.f(owner, *args, **kwargs)
        return wrapped