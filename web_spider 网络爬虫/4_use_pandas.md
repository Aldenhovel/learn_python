#### 本篇介绍使用Python中鼎鼎有名的pandas库进行数据清洗和输出。

# 1

### pandas是什么？

pandas是一个能够提供快速数据结构及相关操作方法的Python软件包，使用pandas来处理“关系”或者“标记”型数据既直观又简单。pandas建立于numpy之上，能够与多数科学计算环境实现良好集成，其目标时成为任何语言中可用的最强大最灵活的开源数据分析、操纵工具(becoming the most powerful and flexible open source data analysis/manipulation tool available in any language)。

### pandas可以做什么？

在我们日常工作生活中，一维或二维关系型数据结构可以满足我们大多数的使用场景，这两者简单来说就是列表和表格。
在pandas中它们也有对应的数据结构：

- 列表 Series 如：

|ix|fruit|
|:---|:---|
|0|apple|
|1|banana|
|2|orange|

- 表格 DataFrame 如：

|name|age|tel|city|
|:---|:---|:---|:---|
|joe|21|10011|Beijing|
|katy|37|13101|Shanghai|
|ben|15|10231|Xi'an|

pandas不仅提供了数据的存储方式，也提供了数据清洗处理的一些基本操作，极大简化了编程工作量，更重要的是提供了简易且可靠的数据处理平台。你可以将pandas完全作为你处理数据的工具而不是软件开发的库(当然这可能需要了解numpy)。以下是一些常用的pandas操作：

- Series常用操作

|方法|操作|
|:---|:---|
|.index|返回index列表|
|.values|返回value列表|
|.at['index']|用index查询对应的value|
|.append(s)|将s追加到原Series尾部|
|.drop(i)|删除index为i那一项|


- DataFrame常用操作

|方法|操作|
|:---|:---|

如果想要系统地学习或者查询相关教程，可以参考官方文档：
https://pandas.pydata.org/docs/reference/index.html#api

使用前首先要安装pandas，可以在IDE里面安装也可以在系统CMD里使用pip命令安装，安装完成之后我们将它导入到程序中：

```
import pandas as pd
```

# 2

我们先来看下Series数据结构，一个Series就是一个列表，分为两部分：

- key 键，即索引
- value 值，即数据

在创建Series的时候不要将key和value混淆，毕竟它是一个有序的列表而不是松散的集合，我们可以这样创建一个Series：

```
dt = {
    'A':'apple',
    'B':'banana',
    'C':'orange',
    'D':'cherry'
}
val = ['apple', 'banana', 'orange', cherry]
ix = ['A', 'B', 'C', 'D']

s1 = pd.Series(dt)
s2 = pd.Series(val, index=ix)
```

s1与s2相同，因为字典本身由key和value组成，也可以不指定key让pandas自动按顺序给你分派key(index)，index从0开始递增：

```
s3 = pd.Series(['apple', 'banana', 'orange', 'cherry'])
```

尝试输出：

```
print(s1)
```
```
>>
A     apple
B    banana
C    orange
D    cherry
dtype: object
Process finished with exit code 0
```

以s1为例，现在我们已经成功构造一个Series了，pandas提供了一些方法和属性来让我们对这个Series进行操作：

- 获取所有索引(index)
```
s1.index

>>
Index(['A', 'B', 'C', 'D'], dtype='object')
Process finished with exit code 0
```

- 获取所有值(value)
```
s1.values

>>
['apple' 'banana' 'orange' 'cherry']
Process finished with exit code 0
```

需要注意一下，以上两个属性返回列表并不是Python基本类型中的```list```，而是```<class 'pandas.core.indexes.base.Index'>```和```<class 'numpy.ndarray'>```，如果有特定需求则需要手动显式转化，pandas也提供方法转化为适用于numpy的类型，可以在官方文档中查阅。

- 根据index查找value
```
s1.at['D']
s1.D

>>
cherry
Process finished with exit code 0
```
上面两种方法都可以查询index为D对应的value值。

- 新增(append方法)
```
s = pd.Series({'E':'pear'})
s2 = s1.append(s)

>>
A     apple
B    banana
C    orange
D    cherry
E      pear
dtype: object
Process finished with exit code 0

```
append()方法可以将另一个Series追加到一个Series的后面，注意此函数返回值s2才是结果，s1未受改变。

- 删除(drop方法)
```
s2.drop('E')

>>
A     apple
B    banana
C    orange
D    cherry
dtype: object
Process finished with exit code 0
```
drop()方法则直接在原Series上操作。

- 修改
```
s1.A = 'melon'
s1['A'] = 'melon'
```
修改某一index的value可以用上面两种方法。
