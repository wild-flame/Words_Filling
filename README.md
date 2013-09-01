<!doctype html>
<html lang="zh_CN">
<head>
	<meta charset="utf-8" />
	<titleWord_Fiiling_DOC</title>
    <meta name="author" content="Wildflame" />
    <meta name="description" content=Word_Fiiling_DOC" />
    <link rel="stylesheet" href="http://railstutorial-china.org/assets/styles/style.css" />
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
</head>

<div class="wrapper">

#DOCUMENTATION

<div class="content">

Word\_Filling简介：
=====================

<div class="main">


功能
----

将特定的单词图片填入图片的指定区域。

根据图像提取特征，判断可以填入单词的位置，同时画布上每个点的值都可以取到，我们可以通过比较此颜色值与背景色来得知此处是否为空白区域，以便在填入单词的时候判断是否有空位可以填入新单词。

使用方法
--------

而'../image/data/\*'里放入需要填入的图片

而'../image/xxxxx.jpg'为放入的特征图（二值图），注意二值图其实有两种情况，0表示黑色和1表示黑色，在判断的时候，这两种情况得到的结果刚好相反，即图像分别填在内部和外部。

在终端里键入

**$ python main.py**
	
会生成*input_data.csv*，同时也会生成预览图test.png。之后再输入

**$ python Generate_new_pic.py**
	
就会根据这个*input_data.csv*里的数据生成需要的结果了。

本次改进
--------

-   改进第二次填图的算法使用螺旋线来进行遍历(螺旋线)
-   输出均改为Data-和二值图像（参考图）
-   根据生成的Data来生成新的图片的数据

Dependency
----------

Python，同时需要PIL（Python Image Library）的库。

Algorithm的思路
---------------

遍历使用的是从左上角到右下角的遍历，第二次改用螺旋线来遍历。

## 还可以完善的地方

-   main.py和mylib里面的一些方法可以重构，两种遍历的方法可以继承自同一个对象。

-   在图片旋转的角度的设置的丰富性和可调节性上还可以优化。

-   第二次遍历过程中的性能提升（一个思路）：

    “位图”加了引号，用于区别图形技术中的位图。这里的位图也可以叫位示图，是一种索引，常见于文件系统等领域。它的基本思想就是用一个位代表一个对应区块的使用状态。举例来说，可以用一个字节来代表8个区块的使用状态，其中第0-7位分别代表第0-7个区块，每个位为1时表示对应区块已使用，为0则表示未使用。

    根据这个思想，我们可以把整幅图划分为类似3×3这样的小块块，然后建一个位示图表示这些小块的使用状态。在每次输出一个词时，可以直接根据位图寻找空白区域，输出该词后即时更新所用区块的使用状态。我们再算笔账，前面所说的遍历改成每步3个像素，可以提高3倍速度，这次3×3一个区块，速度有多少提升呢？答案是9倍！
    
## 最后结果的范例图片

<img src='image/test_csv.png' width=100% />

对比手工排版的原图：

<img src='image/01-0001~0142.jpg' width=100% />

----------------------

## 参考资料：

-   官方文档
    [http://effbot.org/imagingbook/](http://effbot.org/imagingbook/)
-   数字图像处理PIL的一个实例
    [http://blog.sina.com.cn/s/blog\_4b5039210100f6ki.html](http://blog.sina.com.cn/s/blog_4b5039210100f6ki.html)
-   一篇关于如何成为Python高手的文章，是从 How to become a proficient
    Python programmer 这篇文章翻译而来的
    [http://www.zhizhihu.com/html/y2011/3093.html](http://www.zhizhihu.com/html/y2011/3093.html)
-   把图片的数据变换成数组
    [http://blog.csdn.net/zhengkarl/article/details/5731317](http://blog.csdn.net/zhengkarl/article/details/5731317)
-   Python图形图像处理库的介绍之Image模块
    [http://tojaoomy.iteye.com/blog/1413810](http://tojaoomy.iteye.com/blog/1413810)
-   微博关键字图片生成算法
    [http://ued.ctrip.com/blog/?p=2471](http://ued.ctrip.com/blog/?p=2471)
-   Python Import模块
    [http://www.cnitblog.com/seeyeah/archive/2009/03/15/55440.html](http://www.cnitblog.com/seeyeah/archive/2009/03/15/55440.html)
-   Python 标准库——文件管理
    [http://www.cnblogs.com/vamei/archive/2012/09/14/2684775.html](http://www.cnblogs.com/vamei/archive/2012/09/14/2684775.html)
-   Button Generater
    [http://hi.baidu.com/dongyuejiang/item/cbe759cee62cea080ad93ad3](http://hi.baidu.com/dongyuejiang/item/cbe759cee62cea080ad93ad3)


-	Image Resizing <http://www.jqueryscript.net/layout/jQuery-Plugin-for-Client-Side-Image-Resizing-canvasResize.html>
</div>
</div>
</div>


