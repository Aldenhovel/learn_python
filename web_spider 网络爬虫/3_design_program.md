# 1.
了解了BeautifulSoup和requests后我们已经可以实现一些最简单的工作，例如在某一个特定的网页将特定位置的信息抓取并输出，但这还不算是一个完整的爬虫程序。
下面我们拓展一下：
- 如何使其自动找到你想要的网页？
- 如何设计数据结构暂存你已经爬取到的信息？
- 如何将抓取到的信息保存到硬盘里？

编写代码总是简单的事，但是如果没有在写代码之前总体计划好整个项目程序的结构，输入输出的格式以及接口，而是盲目急躁地开始写代码，后面将会付出严重代价。

# 请在开始写代码前做好项目的整体规划！！！

# 2.
我们先来解决第一个问题：如何让程序自动找到想要去的网址？

很简单，构造URL。没有爬虫可以肆无忌惮地去任何它想去地地方并正常工作，实话说，某一个爬虫都是为某一个特定的网页URL设计的，但是假如某两个URL的网页结构完全相同，那它可以正常继续工作。
这意味着我们可以观察URL结构变化，手动构造出一个网址第n页的URL，举个例子：

这个是中关村网手机频道的第一页：
```
https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_1.html
```

第二页和第三页：
```
https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_2.html
https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_3.html
```

你已经发现了，URL地址只是改变了最后一个数，即第N页我们只需要把那个数改成N就是对应的URL，它的构造方法为：
```
url = "https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_$.html".replace('$', N)
```

为了验证，我们将N假设为30，构造出第30页的URL地址：
```
https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_30.html
```
成功在浏览器上打开，构造URL完成！

- 其他比较简单的网页应该也是类似的结构，可能会有不同，也可能会在URL中带有参数或者验证信息，关键在于找规律
- 带有验证信息的URL多数具有反爬机制，需要分析Token/加密方式，此处先不展开讨论

此时我们已经让爬虫更加强大了，因为它在爬完一个页面之后有能力自动生成下一个URL地址，自动开始爬下一页，直到我们让它停为止。

# 3.
第二个问题，如何设计数据结构暂存信息？

对于有一定Python基础的朋友我比较推荐使用pandas的DataFrame，将内容存在二维表格中，pandas提供的接口对后面的数据清洗，遍历，检查都很方便。
- pandas的官方文档：https://pandas.pydata.org/docs/user_guide/

如果没有学过pandas也没关系，我们可以使用Python的基础数据类型来暂存，我的习惯是：使用list + tuple + str，举个例子：
```
<person>
    <name>joe<name>
    <age>18</age>
    <tel>10001</tel>
</person>
<person>
    <name>ben<name>
    <age>22</age>
    <tel>10011</tel>
</person>
<person>
    <name>jane<name>
    <age>26</age>
    <tel>10231</tel>
</person>
```
- 这是一个xml的树状信息，使用pandas.DataFrame存储生成一张person表格：

|name|age|tel|
|:---|:---|:---|
|joe|18|10001|
|ben|22|10011|
|jane|26|10231|

- 使用基础list + tuple + str生成信息列表：
```
dt = [('joe', '18', '10001'),
      ('ben', '22', '10011'),
      ('jane', '26', '10231')]
```

两者方法都能暂存信息，如果数据集比较大，使用pandas比较好；如果只是零星数据，列表存储显然更方便。

# 3.
最后来考虑一下怎么保存成果。

我们知道程序是在内存中运行的，如果你不将爬取到的信息保存在硬盘中，程序运行结束它就会消失，所以我们必须将信息输出到某一个文件中，这个文件可以是：
- xml文件
- SQL数据库
- 其他数据文件形式，如excel

|方法|优点|缺点|
|:---|:---|:---|
|xml|轻量跨平台，各种语言都有接口|效率较低|
|sql数据库|需要学习SQL语言|效率高，有安全性|
|excel|生活中常用，可视化|接口少，不适合在编程中使用|
|其他|...|...|

每种保存形式都有其优缺点，Python也有对应的接口或包，这里主要介绍一下更偏向轻量级的xml文件方法：
- xml是一种标记语言，教程可以参考：https://www.w3school.com.cn/xml/index.asp
- 关于Python操作xml文件，可以参考官方文档：https://docs.python.org/zh-cn/3/library/xml.etree.elementtree.html

下面我来演示一下如何将：
```
dt = [('joe', '18', '10001'),
      ('ben', '22', '10011'),
      ('jane', '26', '10231')]
```
写入到文件./my_data.xml里：

首先导入所需的包:
```
import xml.etree.ElementTree as ET
```

然后从根开始，建立这一颗树：
```
root = ET.Element("root")
tree = ET.ElementTree(root)
for info in dt:
    person = ET.Element("person")
    
    name = ET.Element("name")
    name.text = info[0]
   
    age = ET.Element("age")
    age.text = info[1]
    
    tel = ET.Element("tel")
    tel.text = info[2]
    
    person.append(name)
    person.append(age)
    person.append(tel)
    
    root.append(person)

```

此时就生成了一个xml树，里面有刚刚所保存的信息，如果想要转换成符合阅读习惯的模式，需要在写入过程中处理一下，否则文件里面可能是一行过。可以参考这里：https://blog.csdn.net/u012692537/article/details/101395192
```
def PrettyXml(element, indent='\t', newline='\n', level=0):
    if element:
        if (element.text is None) or element.text.isspace():
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
    temp = list(element)
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):
            subelement.tail = newline + indent * (level + 1)
        else:
            subelement.tail = newline + indent * level
        PrettyXml(subelement, indent, newline, level=level + 1)
```

即最后我们可以这样将这棵xml树写入到文件：
```
PrettyXml(root)
tree.write("./my_data.xml", "utf-8")
```

此时文件写入完成，已经将爬取到的信息保存到了对应路径上，检查无误则大功告成！
