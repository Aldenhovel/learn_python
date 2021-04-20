# 1.
各种各样的网页有众多组成元素，例如图片、链接、文本、图形和动画，这种复杂的网页结构体也意味着抓取网页源代码的爬虫不一定能立刻获得你想要的信息。
所以在开始编写爬虫程序之前，你需要先计划清楚：
- 去哪里爬？
- 爬什么？

更专业一点的问法是：
- 目标网页的URL地址是哪里？
- 所需要的数据在于此URL地址传回网页源码结构的路径是什么？

第一个问题显然容易解决，没有人会不知道自己想要爬哪些数据。

第二个问题则可能有点难度，如果你有了解过html或者xml这种标记语言的知识，那你大概可以明白网页源码是一个树状结构。
一个比较合适的比喻是：html是网页的骨骼，javascript是网页的肌肉，css是网页的皮肤。
在我们现在面对这种比较简单的网页结构上，信息元素多半会存储于html上，即网页源代码，在使用requests获得网页源码后我们就可以对它进行解析，找到目标的位置。

举个例子：
这是一个html文件（内容即对应网页源码）
```
<html>
  <body>
    <div id="joe">hello joe</div>
    <div id="ben">hello ben</div>
    <li>
      <p class="a">a</p>
      <p class="b">b</p>
      <p class="c">c</p>
    </li>
  </body>
</html>
```
如果你想要抓取：
```hello joe```

你需要告诉计算机目标的位置是：
```html/body/div[id="joe"]/```

计算机根据你的位置就能一路搜索：
```<html>---<body>---<div id="joe">```
就能找到你所定位的标签，接下来便可以保存标签的内容或者其他所需的信息。这就是最基本的爬虫思路：获取源码——搜索元素——保存信息。

# 2.
你已经了解了html的结构和爬虫的重点——搜索元素，由于整个网页源代码是一个完整的字符串，我们可以使用这些方法找到你的内容。
- 瞪大眼睛一行行找，一直找，直到找到为止
- 根据html的标签结构，使用正则表达式逐层筛选，一直筛，直到筛选出想要的结构
- 利用Chrome浏览器定位到目标标签，使用BeautifulSoup解析到目标内容

显然第三种方法更加快捷，但是需要做两件事：
- 定位元素位置
- 使用BeautifulSoup来解析到目标内容

第一点可以参考这里（并不需要使用到XPath路径，但是你要知道怎么去找元素位置）：
https://blog.csdn.net/weixin_43277055/article/details/85319676

第二点关于BeautifulSoup包，可以先看看官方文档，有助于更加全面地了解它的功能：
https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/

# 3.
下面将介绍BeautifulSoup包的简易使用
首先我们导入包（事前要先安装）

```from bs4 import BeautifulSoup```

然后利用之前得到的response.text初始化一个BeautifulSoup实例，为了简化，我们直接拿取这个html树的body内容（相当于进入了<body>节点）

```
soup = BeautifulSoup(response.text)
body = soup.body
```

你可以想象此时网页源代码已经变成了一棵树，只要按照对应路径进入到分支，就能找到结果。关键的“进入”有以下两个方法：
- find() 返回进入某一分支后的节点
- find_all() 返回所有符合要求的分支的节点列表
除此之外，这两个方法需要带有参数，一个是目标的标签类型，一个是目标的属性值。举个例子：

```
<html>
  <body>
    <div id="joe">hello joe</div>
    <div id="ben">hello ben</div>
    <li>
      <p class="a">a</p>
      <p class="b">b</p>
      <p class="c">c</p>
    </li>
  </body>
</html>
```
在上面的html例子中，想要找到```hello ben```这个元素，可以这么写：
```info = body.find('div', id='ben').string```

找到```a```这个元素，这样写：
```info = body.find('li').find('p', class_="a").string```

想要找到所有的```<p>```中包含的信息，这么写：
```info_list = body.find('li').find_all('p')```
- 注意find()的返回结果是一个标签对象，find_all()的返回结果是由标签对象组成的列表
- 想要获得标签的字符串形式内容，需要使用标签的string属性

最后所得的```info```是目标内容的字符串，```info_list```是标签的列表
```
print(info)

for info in info_list:
  print(info.string)
```


