Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = lambda x: x * 2 + 1
>>> def b(b,x):
...     return b(x+a(x))
... 
>>> x=3
>>> b(a,x)
21
