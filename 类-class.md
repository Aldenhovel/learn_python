# CLASS NOTE

## 0.目录

## 1.什么是类？
类，即程序中的Class，是高级编程语言的重要内容，在比较简单的程序中我们一般只设计一个起点和一个终点，中间直接铺设具体命令即可。当我们的程序更大的时候，大量直接铺设的代码显得十分繁琐和难以修改，所以我们加入了函数的概念，通过函数执行相同的操作可以大大降低工作量。随着函数的大量使用，函数本身也可能变得繁琐起来，例如苹果和香蕉都有color,weight的属性和eat,sell的方法，为了不让它们的变量名冲突，我们只能写成
```
color_apple = 'RED'
color_banana = 'YELLOW'
weight_apple_g = 500
weight_banana_g = 350
eat_apple()
sell_apple()
eat_banana()
......
```
也许你已经发现了，随着程序中我们要描述的“对象”增加，给每一个“对象”都给予唯一的方法或变量名是一件非常繁琐且逻辑混乱的行为，例如在上面的一大堆东西中，eat_apple()与color_banana没有任何关系，按照逻辑它们应该分别属于apple和banana两个不同的“对象”，如果我们可以采用一个对象来封装各自的函数和属性，可以令程序设计得更加符合人的逻辑思维。这个“对象”就是类。

## 2.类的作用
### 2.1封装
如字面意思，封装就是把描述某个“对象”的属性和函数集中封装起来，你可以把它理解为这些变量或者函数就从原来的在主程序中散兵游勇变成在类中训练有素的士兵，平时它们只生存在类中，各个类之间互不干涉、各司其职，如：
```
class Apple:
	color
	weight
	eat()
	sell()

class Banana:
	color
	weight
	eat()
	sell()
```

### 2.2继承
继承也是类独特的功能，在我们的生活中有不少“对象”是有级别关系的，例如：水果->苹果->红富士苹果，水果是父类最低级，苹果是子类中间级，红富士是孙类最高级。父类的属性在子类中都存在，例如世间所有水果都有重量、产地属性，苹果和红富士苹果当然也有。但是子类的属性在父类中不一定存在，例如“苹果”可以有属性：核大小，但是这个属性不能放在“水果”中，因为不是所有“水果”都有核。“红富士苹果”属于“苹果”，所有它一定有核，继承了“苹果”的核大小的属性。
```
class Fruit:
	weight
	location

class Apple(Fruit):
	weight
	location
	coresize

class RedFuji(Apple):
	weight
	location
	coresize
	price
	......
```

### 2.3安全
由于在类中我们已经对一些对象的属性或函数封装起来了，所以我们可以控制它的隐私性，让某些属性或函数对外不可见。这么做可以简化一个类的对外接口，提升安全性，防止一些数据被错误更改。

## 3.使用方法
### 3.1定义类
创建类使用关键字 class ，后面加类名，括号里面加上所继承的父类。如果不需要继承父类，括号里面可以写object，因为class object是所有类的公共父类。也可以直接不写继承关系。
```
class Fruit(object):
	......

class Fruit:
	......
``` 

### 3.2构造函数
实例化类的时候我们一般需要告诉程序怎样去初始化它。构造函数为__init__(self)，可以添加参数，参数用来初始化。在下面的例子中我们定义了Student类，并且实例化了一个例子。
```
class Student(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

lihua = Student('lihua', 21)	#得到一个name为lihua,age为21的Student实体
```

### 3.3类方法
类方法即类里面存放的函数，它的编写与常规函数没有什么不一样，但是如果要访问类成员，必须在参数加上self，访问时使用self.XX。
```
class Student(object):
	def __init__(self, name):
		self.name = name

	def print_name(self):
		print(self.name)

lihua = Student('lihua')
lihua.print_name()				#调用了Student.print_name()函数，输出了self.name即“lihua”
```
假如某个函数以下划线开头，那它将在外界不可见，如下面将会报错。
```
class Student(object):
	def __init__(self, name):
		self.name = name

	def _print_name(self):
		print(self.name)

lihua = Student('lihua')
lihua._print_name()			#_print_name()为私有函数，不能被外界调用
```

### 3.4特殊的类方法
在类中有一些特殊的函数，它们多数以两个下划线开头和结尾，例如上面提及的构造函数```__init__```，这些是一些特殊的类方法，主要提供一些对类本身性质的描述，例如以下这些：

1. \_\_str__

```__str__```函数控制类的输出方法，当执行print函数时，实质上就是执行了某个类的__str__函数，例如。


```
class Student:
	def __init__(self, name):
		self.name = name 

	def __str__(self):
		return 'my name is {}'.format(self.name)

s = Student('lihua')
print(s)

>>
lihua
```


2. \_\_len__

```__len__```函数控制类在len()中的输出结果
```
class StudentList:
	def __init__(self, lst):
		self.student_lst = lst

	def __len__(self):
		return len(self.student_lst)

sl = StudentList(['a', 'b', 'c'])
print(len(sl))

>>
3
```

3. \_\_add__

```__add__```函数控制两个实体之间使用加号运算的结果，减、乘、除分别使用```__sub__```,```__mul__```,```__div__```同理。
```
class Score:
	def __init__(self, score):
		self.score = score

	def __add__(self, other):
		return Score(self.score + other.score)

	def __str__(self):
		return self.score

math = Score(100)
english = Score(69)
total = math + english
print(score)

>>
160
```

## 4.示例：创建属于自己的MySeries类
### 4.1研究需求
1. 属性
- 作为一个自己的Series类，类中至少应该包含一个pandas.Series作为中枢，然后我们再围绕这个中枢重写各种方法。

2. 方法
- 更加直白的输出方式：直接使用print方法
- 使用“+”作为拼接的方法
- 使用len()函数输出列表元素个数
- 更加方便的选择语句
- 更加方便的排序语句

### 4.2构造函数
根据我们使用Series的经验我们一般使用两种方法构造Series，要么同时指定values和index，要么只指定values使用默认序数index，所以我们自己的MySeries类也应该遵守这样的创建规范，提供这两种对应的构造函数。由于Python中类只能有一个构造函数，所以需要采用默认值判断的方式来处理不同给与参数的构造形式。下面的示例中分别提供了1.给定val和ix,2.只给定val,3.什么都没给，这三种类的构造形式。
```
   def __init__(self, val=None, ix=None):
        if val is None:
            self.ser = pd.Series()
        else:
            if ix is None:
                self.ser = pd.Series(val)
            else:
                self.ser = pd.Series(val, index=ix)

#测试：
s1 = MySeries(['apple', 'banana'], ['A', 'B'])	
s2 = MySeries(['apple', 'banana'])
```

### 4.3\_\_str__函数
如果我们想要将这个类使用print输出，那我们应该想要输出它的ser属性，格式最好和pands.Series差不多，所以我们可以这样构造```__str```函数的返回信息。
```
	def __str__(self):
		s = ''
        for i, v in self.ser.items():
            s = s + str(i) + ' : ' + str(v) + '\n'
        return s

#测试：
fruit = MySeries(['apple', 'banana'])
print(fruit)

>>
0 : apple
1 : banana
2 : orange
```

### 4.4\_\_add__函数
一般的pd.Series中我们需要使用append方式来拼接行，但是我觉得十分麻烦，如果使用“+”来实现就好了，于是我们定义MySeries类的```__add__```函数。
```
    def __add__(self, other):
	    s = MySeries()
	    s.ser = self.ser.append(other.ser)
	    return s

#测试
fruit1 = MySeries(['apple', 'banana', 'orange'])
fruit2 = MySeries(['cherry'])
print(fruit1 + fruit2)

>>
0 : apple
1 : banana
2 : orange
0 : cherry
```

### 4.5\_\_len__函数
求pandas.Series的元素个数可以使用size属性，如果改成使用len()函数来求则更符合习惯，所以我们需要改写```__len__```函数。
```
	def __len__(self):
		return self.ser.size

测试：
fruit = MySeries(['apple', 'banana', 'orange'])
print(len(fruit))

>>
3
```

### 4.6选择某行
pandas.Series中选择某行我们可以使用at[]和iat[]函数，现在我们将它改造为新的```select_one()```函数，将两者统一起来，用一个参数确认是依据索引值还是索引排位来选择。
```
    def select_one(self, i, with_index=False):
	    if with_index is True:
	        return self.ser.iat[i]
	    else:
	        return self.ser.at[i]

#测试：
fruit = MySeries(['apple', 'banana', 'orange'], ix=['A', 'B', 'C'])
print(fruit.select_one('A'))
print(fruit.select_one(1, True))

>>
apple
banana
```

### 4.7排序
pandas.Series中排序使用sort_values()函数，排完之后我们一般需要更新索引，且不需要保留原索引，所以我们可以新建一个```sort()```函数来一次性完成这些琐碎事。
```
    def sort(self):
        self.ser = self.ser.sort_values()
        self.ser = self.ser.reset_index(drop=True)
        return self

#测试：
myser = MySeries([2,6,3,2,8])
print(myser.sort())

>>
0 : 2
1 : 2
2 : 3
3 : 6
4 : 8
```

### 4.8全部代码
至此我们的一个简单的MySeries类已经完成了，它重写了一些操作pandas.Series的函数和方法，例如拼接、排序、选择、输出等，使用起来更加符合我们的特定习惯和简化了操作步骤。下面是完整代码：
```
import pandas as pd

class MySeries(object):
    '''
    This is a Class for simplifying pandas.Series, making it more straightforwardly for special working condictions
    '''

    def __init__(self, val=None, ix=None):
        if val is None:
            self.ser = pd.Series()
        else:
            if ix is None:
                self.ser = pd.Series(val)
            else:
                self.ser = pd.Series(val, index=ix)

    def __str__(self):
        s = ''
        for i, v in self.ser.items():
            s = s + str(i) + ' : ' + str(v) + '\n'
        return s

    def __add__(self, other):
        s = MySeries()
        s.ser = self.ser.append(other.ser)
        return s

    def select_one(self, i, with_index=False):
        if with_index is True:
            return self.ser.iat[i]
        else:
            return self.ser.at[i]

    def sort(self, ASC=True):
        self.ser = self.ser.sort_values(ascending=ASC)
        self.ser = self.ser.reset_index(drop=True)
        return self
```

## 感谢学习本篇章