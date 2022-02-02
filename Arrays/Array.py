Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> listanomes=['João','Patricia','Debora']
>>> type (listanome)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type (listanome)
NameError: name 'listanome' is not defined
>>> type(listanomes)
<class 'list'>
>>> listanomes(1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    listanomes(1)
TypeError: 'list' object is not callable
>>> listanomes[1]
'Patricia'
>>> 
>>> 
>>> listanomes.append('Mariana')
>>> listanomes
['João', 'Patricia', 'Debora', 'Mariana']
>>> lista
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    lista
NameError: name 'lista' is not defined
>>> 
>>> sorted(lista)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    sorted(lista)
NameError: name 'lista' is not defined
>>> sorted(listanomes)
['Debora', 'João', 'Mariana', 'Patricia']
>>> lista.reverse(listanomes)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    lista.reverse(listanomes)
NameError: name 'lista' is not defined
>>> 