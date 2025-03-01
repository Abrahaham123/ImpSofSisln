```python
import foo
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    Cell In[63], line 1
    ----> 1 import foo
    

    ModuleNotFoundError: No module named 'foo'



```python
if True:
print("whjda")
```


      Cell In[59], line 2
        print("whjda")
        ^
    IndentationError: expected an indented block after 'if' statement on line 1
    



```python
def f():
    raise OSError('operation failed')

excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f'Happened in Iteration {i+1}')
        excs.append(e)

raise ExceptionGroup('We have some problems', excs)

```

      + Exception Group Traceback (most recent call last):
      |   File "C:\ProgramData\anaconda3\Lib\site-packages\IPython\core\interactiveshell.py", line 3577, in run_code
      |     exec(code_obj, self.user_global_ns, self.user_ns)
      |   File "C:\Users\CompuAula 03\AppData\Local\Temp\ipykernel_12312\2397146538.py", line 12, in <module>
      |     raise ExceptionGroup('We have some problems', excs)
      | ExceptionGroup: We have some problems (3 sub-exceptions)
      +-+---------------- 1 ----------------
        | Traceback (most recent call last):
        |   File "C:\Users\CompuAula 03\AppData\Local\Temp\ipykernel_12312\2397146538.py", line 7, in <module>
        |     f()
        |   File "C:\Users\CompuAula 03\AppData\Local\Temp\ipykernel_12312\2397146538.py", line 2, in f
        |     raise OSError('operation failed')
        | OSError: operation failed
        | Happened in Iteration 1
        +---------------- 2 ----------------
        | Traceback (most recent call last):
        |   File "C:\Users\CompuAula 03\AppData\Local\Temp\ipykernel_12312\2397146538.py", line 7, in <module>
        |     f()
        |   File "C:\Users\CompuAula 03\AppData\Local\Temp\ipykernel_12312\2397146538.py", line 2, in f
        |     raise OSError('operation failed')
        | OSError: operation failed
        | Happened in Iteration 2
        +---------------- 3 ----------------
        | Traceback (most recent call last):
        |   File "C:\Users\CompuAula 03\AppData\Local\Temp\ipykernel_12312\2397146538.py", line 7, in <module>
        |     f()
        |   File "C:\Users\CompuAula 03\AppData\Local\Temp\ipykernel_12312\2397146538.py", line 2, in f
        |     raise OSError('operation failed')
        | OSError: operation failed
        | Happened in Iteration 3
        +------------------------------------
    


```python
x = 10 / 0
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    Cell In[45], line 1
    ----> 1 x = 10 / 0
    

    ZeroDivisionError: division by zero



```python
for line in open("myfile.txt"):
    print(line, end="")
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[35], line 1
    ----> 1 for line in open("myfile.txt"):
          2     print(line, end="")
    

    File C:\ProgramData\anaconda3\Lib\site-packages\IPython\core\interactiveshell.py:324, in _modified_open(file, *args, **kwargs)
        317 if file in {0, 1, 2}:
        318     raise ValueError(
        319         f"IPython won't let you open fd={file} by default "
        320         "as it is likely to crash IPython. If you know what you are doing, "
        321         "you can use builtins' open."
        322     )
    --> 324 return io_open(file, *args, **kwargs)
    

    FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'



```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide("2", "1")
```

    executing finally clause
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[33], line 10
          8     finally:
          9         print("executing finally clause")
    ---> 10 divide("2", "1")
    

    Cell In[33], line 3, in divide(x, y)
          1 def divide(x, y):
          2     try:
    ----> 3         result = x / y
          4     except ZeroDivisionError:
          5         print("division by zero!")
    

    TypeError: unsupported operand type(s) for /: 'str' and 'str'



```python
raise ValueError  # shorthand for 'raise ValueError()'
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[17], line 1
    ----> 1 raise ValueError
    

    ValueError: 



```python
raise new_exc from original_exc
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[3], line 1
    ----> 1 raise new_exc from original_exc
    

    NameError: name 'new_exc' is not defined



```python
try:
    ...
 SomeException:
    tb = sys.exception().__traceback__
    raise OtherException(...).with_traceback(tb)
```


      File <string>:3
        SomeException:
                      ^
    IndentationError: unindent does not match any outer indentation level
    



```python
try:
    if´Carlos´ == carlos.nombre:
    exept NameError:
    print("Delfine la variable
```


      Cell In[1], line 2
        if´Carlos´ == carlos.nombre:
          ^
    SyntaxError: invalid character '´' (U+00B4)
    

