
# 基础语法说明

Python的语法比较简单，采用缩进方式，写出来的代码就像下面的样子：


```python
# print absolute value of an integer:
a = 100
if a >= 0:
    print(a)
else:
    print(-a)
```

    100
    

以#开头的语句是注释，注释是给人看的，可以是任意内容，解释器会忽略掉注释。其他每一行都是一个语句，当语句以冒号:结尾时，需要进行代码缩进。
最后，请务必注意，Python程序是大小写敏感的，如果写错了大小写，程序会报错。

# 数据类型

其数据类型包括整数、浮点数、字符串、布尔值、空值。下面对需要注意的点进行解释：

## 浮点数

浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，1.23x10的9次方和12.3x10的8次方是完全相等的。浮点数可以用数学写法，如1.23，3.14，-9.01，等等。但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x10的9次方就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5，等等。

注意：Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648~2147483647。
Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。

## 字符串

字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等。
如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，比如：


```python
'Let\'s go!'
```




    "Let's go!"




```python
'\"Hello, world!\" She said '
```




    '"Hello, world!" She said '



如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试：


```python
print('\\\t\\')
```

    \	\
    


```python
print(r'\\\t\\') #r''表示''内部的字符串默认不转义
```

    \\\t\\
    

还有其他形式的转义符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\。

## 布尔值

布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来：


```python
True+True+False
```




    2




```python
3>5
```




    False



布尔值经常用在条件判断中，比如：


```python
age=20
if age >= 18:
    print('adult')
else:
    print('teenager')
```

    adult
    

## 空值

空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

# 变量与常量

## 变量

变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。
变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头。声明变量时不需要指定变量类型。比如：


```python
a=1
```

变量a是整型


```python
b ='TL000'
```

变量b是字符串

在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，例如：


```python
a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)
```

    123
    ABC
    

这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言，赋值语句如下（// 表示注释）：

int a = 123; // a是整数类型变量
a = "ABC"; // 错误：不能把字符串赋给整型变量

最后，理解变量在计算机内存中的表示也非常重要。当我们写：
a = 'ABC' 时，
Python解释器干了两件事情：
在内存中创建了一个'ABC'的字符串；
在内存中创建了一个名为a的变量，并把它指向'ABC'。

也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据，例如下面的代码：


```python
a = 'ABC'
b = a
a = 'XYZ'
print(b)
```

    ABC
    

## 常量

所谓常量就是不能变的变量，比如常用的数学常数PI就是一个常量。在Python中，通常用全部大写的变量名表示常量：


```python
PI = 3.14159265359
```

但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法。

## python中的除法

在Python中，有两种除法，一种除法是/：


```python
10/3
```




    3.3333333333333335



/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：


```python
9/3
```




    3.0



还有一种除法是//，称为地板除，两个整数的除法仍然是整数：


```python
10//3
```




    3



因为//除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数：


```python
10%3
```




    1



## 小结

Python支持多种数据类型，在计算机内部，可以把任何数据都看成一个“对象”，而变量就是在程序中用来指向这些数据对象的，对变量赋值就是把数据和变量给关联起来。

对变量赋值 x = y 是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向。

# 字符

## 字符编码

字符串也是一种数据类型，但是，字符串比较特殊的是还有一个编码问题。

因为计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。由于计算机是美国人发明的，因此，最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码，比如大写字母A的编码是65，小写字母z的编码是122。

但是要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以，中国制定了GB2312编码，用来把中文编进去。
可以想得到的是，全世界有上百种语言，日本把日文编到Shift_JIS里，韩国把韩文编到Euc-kr里，各国有各国的标准，就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示出来会有乱码。

因此，Unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节。

新的问题又出现了：如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。

所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间：
字符   ASCII         Unicode                     UTF-8
 A    01000001  00000000 01000001        01000001
中      x       01001110 00101101        11100100 10111000 10101101
搞清楚了ASCII、Unicode和UTF-8的关系，我们就可以总结一下现在计算机系统通用的字符编码工作方式：在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件。

![0.png](attachment:0.png)

浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器。所以看到很多网页的源码上会有类似meta charset="UTF-8" 的信息，表示该网页正是用的UTF-8编码。

![1.png](attachment:1.png)

## Python的字符串

在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言，例如：


```python
 print('包含中文的str')
```

    包含中文的str
    

对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：


```python
 ord('A')
```




    65




```python
chr(66)
```




    'B'




```python
chr(25991)
```




    '文'



由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。Python对bytes类型的数据用带b前缀的单引号或双引号表示： x = b'ABC'

要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：


```python
'ABC'.encode('ascii')
```




    b'ABC'




```python
'中文'.encode('utf-8')
```




    b'\xe4\xb8\xad\xe6\x96\x87'


'中文'.encode('ascii')

---------------------------------------------------------------------------
UnicodeEncodeError                        Traceback (most recent call last)
<ipython-input-130-b318511b2a75> in <module>()
----> 1 '中文'.encode('ascii')

UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：


```python
 b'ABC'.decode('ascii')
```




    'ABC'




```python
 b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
```




    '中文'



要计算str包含多少个字符，可以用len()函数：


```python
len('ABC')
```




    3




```python
len('中文')
```




    2



len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：


```python
 len(b'ABC')
```




    3




```python
len('中文'.encode('utf-8'))
```




    6



可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。

当源代码中包含中文的时候，在保存源代码时，需要务必指定保存为UTF-8编码，不然会出现乱码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：


```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

## 格式化

### %格式化

如何输出格式化的字符串？我们经常会输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串，而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式。在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：


```python
'Hello, %s' % 'world'
```




    'Hello, world'




```python
'Hi, %s, you have $%d.' % ('Michael', 1000000)
```




    'Hi, Michael, you have $1000000.'



在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
占位符	  替换内容
 %d	     整数
 %f	     浮点数
 %s	     字符串
 %x	    十六进制整数
其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：


```python
'%2d-%02d' % (3, 1)
```




    ' 3-01'




```python
'%.2f' % 3.1415926
```




    '3.14'



如果不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：


```python
'Age: %s. Gender: %s' % (25, True)
```




    'Age: 25. Gender: True'



### format()格式化

另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：


```python
 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
```




    'Hello, 小明, 成绩提升了 17.1%'



练习：小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：


```python
s1 = 72
s2 = 85
r = (85-72)/72*100
print('%.1f%s' % (r,'%'))
```

    18.1%
    

# list和tuple

## 列表--list

Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。


```python
classmates = ['Michael', 'Bob', 'Tracy']
classmates
```




    ['Michael', 'Bob', 'Tracy']



用len()函数可以获得list元素的个数：


```python
len(classmates)
```




    3



用索引来访问list中每一个位置的元素，记得索引是从0开始的：


```python
classmates[0]
```




    'Michael'




```python
classmates[2]
```




    'Tracy'



当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：


```python
classmates[-1]
```




    'Tracy'



list是一个可变的有序表，所以，可以往list中追加元素到末尾：


```python
classmates.append('Adam')
classmates
```




    ['Michael', 'Bob', 'Tracy', 'Adam']



也可以把元素插入到指定的位置，比如索引号为1的位置：


```python
classmates.insert(1, 'Jack')
classmates
```




    ['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']



要删除list末尾的元素，用pop()方法：


```python
classmates.pop(1)
classmates
```




    ['Michael', 'Bob', 'Tracy', 'Adam']



要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：


```python
classmates[1] = 'Sarah'
classmates
```




    ['Michael', 'Sarah', 'Tracy', 'Adam']



list里面的元素的数据类型也可以不同，比如：


```python
L = ['Apple', 123, True]
L
```




    ['Apple', 123, True]



## 元组--tuple

另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：


```python
classmates = ('Michael', 'Bob', 'Tracy')
classmates
```




    ('Michael', 'Bob', 'Tracy')



现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。

不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

要定义一个只有1个元素的tuple，如果你这么定义：


```python
t = (1)
t
```




    1



定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。

所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：


```python
t = (1,)
t
```




    (1,)



最后来看一个“可变的”tuple：


```python
t = ('a', 'b', ['A', 'B'])
t[2][0]='X'
t[2][1]='Y'
t
```




    ('a', 'b', ['X', 'Y'])



表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

练习--请用索引取出下面list的指定元素：


```python
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    ]
```


```python
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
```

    Apple
    Python
    Lisa
    

## 小结

list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。

# 条件判断

## if、elif、else

计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。比如，输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现：


```python
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
```

    your age is 20
    adult
    

也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了：


```python
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
```

    your age is 3
    teenager
    

当然上面的判断是很粗略的，完全可以用elif做更细致的判断：


```python
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
```

    kid
    

需要注意：条件判断从上向下匹配，当满足条件时执行对应的块内语句，后续的elif和else都不再执行。

if判断条件还可以简写，比如写：
if x:
    print('True')
只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。

## 讨论下input()
birth = input('birth: ')
if birth < 2000:
    print('00前')
else:
    print('00后')
输入1982，结果报错。这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：


```python
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
```

    birth: 1990
    00前
    
练习

小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：

```python
height = 1.75
weight = 80.5
bmi = weight/(height*height)
if bmi<=18.5:
    print('过轻')
elif bmi<=25:
    print('正常')
elif bmi<=28:
    print('过重')
elif bmi<=32:
    print('肥胖')
else:
    print('严重肥胖')
```

    过重
    

# 循环

## for .. in ..循环

Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：


```python
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
```

    Michael
    Bob
    Tracy
    

所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。

如果要计算1-100的整数之和，python提供了range()函数，可以生成一个整数序列：


```python
sum = 0
for i in range(101):
    sum += i
sum
```




    5050



## while循环

第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：


```python
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
```

    2500
    

练习--请利用循环依次对list中的每个名字打印出Hello, xxx!：


```python
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello,%s!'% name)
```

    Hello,Bart!
    Hello,Lisa!
    Hello,Adam!
    

## break

在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')
上面的代码可以打印出1~100。如果要提前结束循环，可以用break语句：


```python
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    END
    

## continue

在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。


```python
n = 0
while n < 10:
    n = n + 1
    print(n)
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    

上面的程序可以打印出1～10。但是，如果我们想只打印奇数，可以用continue语句跳过某些循环：


```python
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
```

    1
    3
    5
    7
    9
    

可见continue的作用是提前结束本轮循环，并直接开始下一轮循环。

## 小结
循环是让计算机做重复任务的有效的方法。
break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。
要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。
有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。
请试写一个死循环程序：sum = 0
x =1
while x:  #循环条件无法停止，就会陷入死循环
    x+=1
    sum+=x   
# 使用dict和set

## 字典--dict

Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：


```python
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
```

给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。

如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下：


```python
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']
```




    95



为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。

第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。

dict就是第二种实现方式，给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。

把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：


```python
d['Adam'] = 67
d['Adam']
```




    67



如果key不存在，dict就会报错。要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：


```python
'Thomas' in d
```




    False



二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：


```python
print(d.get('Thomas'))
print(d.get('Thomas', -1)) #如果key不存在，返回-1
```

    None
    -1
    

要删除一个key，用pop(key)方法，对应的value也会从dict中删除：


```python
d.pop('Bob')
d
```




    {'Adam': 67, 'Michael': 95, 'Tracy': 85}



需务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
和list比较，dict有以下几个特点：

1、查找和插入的速度极快，不会随着key的增加而变慢；
2、需要占用大量的内存，内存浪费多。
而list相反：

1、查找和插入的时间随着元素的增加而增加；
2、占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。

这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
key = [1, 2, 3]
d[key] = 'a list'

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-214-2d69ccd6fa89> in <module>()
      1 key = [1, 2, 3]
----> 2 d[key] = 'a list'

TypeError: unhashable type: 'list'
## 集合--set

set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

要创建一个set，需要提供一个list作为输入集合：


```python
s = set([1, 2, 3])
s
```




    {1, 2, 3}



注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。

重复元素在set中自动被过滤：


```python
s = set([1, 1, 2, 2, 3, 3])
s
```




    {1, 2, 3}



通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：


```python
s.add(4)
s
```




    {1, 2, 3, 4}




```python
s.add(4)
s
```




    {1, 2, 3, 4}



通过remove(key)方法可以删除元素：


```python
s.remove(4)
s
```




    {1, 2, 3}



set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：


```python
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2 #交
```




    {2, 3}




```python
s1 | s2 #并
```




    {1, 2, 3, 4}



set和dict的唯一区别仅在于没有存储对应的value。

set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。

## 再议不可变对象

上面讲了，str是不变对象，而list是可变对象。

对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：


```python
a = ['c', 'a', 'b']
a.sort() 
a
```




    ['a', 'b', 'c']



而对于不可变对象，比如str，对str进行操作呢：


```python
a = 'abc'
a.replace('a', 'A')
```




    'Abc'




```python
a
```




    'abc'



虽然字符串有个replace()方法，也确实变出了'Abc'，但变量a最后仍是'abc'，应该怎么理解呢？先把代码改成下面这样：


```python
a = 'abc'
b = a.replace('a', 'A')
b
```




    'Abc'




```python
a
```




    'abc'



要始终牢记的是，a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'：
┌───┐                  ┌───────┐
│  a   │──────── >│     'abc'    │
└───┘                  └───────┘
当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：
┌───┐                  ┌───────┐
│  a   │──────── >│    'abc'     │
└───┘                  └───────┘
┌───┐                  ┌───────┐
│  b   │───────— >│    'Abc'     │
└───┘                  └───────┘
所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

## 小结

使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。

set和dict的唯一区别仅在于没有存储对应的value。
