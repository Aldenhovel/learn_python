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
这是一个xml的树状信息，使用DataFrame存储的结果直接是一张person表格：
|name|age|tel|
|:---|:---|:---|
|joe|18|10001|
|ben|22|10011|
|jane|26|10231|


