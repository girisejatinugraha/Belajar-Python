#Tipe Data Primitif
x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))


"""
Output:
<class 'int'>
<class 'float'>
<class 'complex'>
"""


var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

"""
Output:
10
<memory address>
11
<memory address>
"""

#boolean
x = True
print(type(x))

x = False
print(type(x))

"""
Output:
<class 'bool'>
<class 'bool'>
"""

#Formatted String
name = "Giri"
print(f"Hello, nama saya {name}")
 
"""
Output: 
Hello, nama saya Giri
"""

#%-formatting
name = "Giri"
print("Nama saya %s" % (name))
 
"""
Output: 
Nama saya Giri
"""

#str.format()
name = "Giri"
print("Nama saya {}".format(name))
 
"""
Output: 
Nama saya Giri
"""