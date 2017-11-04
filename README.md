### 一.使用
新版的工具已经不需要安装任何附属的东西了,只需两步,就可解脱~

#### 1).修改图片名
这一步十分容易,我们约定一个规则,规定图片的命名为`x_y.png`,这样x就是最终`.fnt`和`.png`的名字,而y就是对应字符的ASCII码,这样我的图片最后命名是这个样子的:

```python
fighting_header_shuzi_0.png 	#0
fighting_header_shuzi_1.png 	#1
fighting_header_shuzi_2.png 	#2
fighting_header_shuzi_3.png 	#3
fighting_header_shuzi_4.png 	#4
fighting_header_shuzi_5.png 	#5
fighting_header_shuzi_6.png 	#6
fighting_header_shuzi_7.png 	#7
fighting_header_shuzi_8.png 	#8
fighting_header_shuzi_9.png 	#9
fighting_header_shuzi_m.png 	#m
```
最后一个m是因为我的图片中包含了一个`m`字样的图片,具体ascii码表可以在[这里][3]查.


#### 2).下载可执行程序
**windows:**

将``bin/win32/images2fnt.exe``拷贝至你的碎图目录,双击运行.

**mac:**

将``bin/mac/images2fnt``拷贝至你的碎图目录,启动终端,键入``./images2fnt``.

然后...然后就神奇的东西出现了呢,在`output`目录下会找到你想要的东西~


### 二.项目
项目采用Python编写,主要依赖了这几个库:

1. Pillow
2. Pyinstaller

Pillow是Python的图片处理库,前身是Pil,项目使用Pillow拼接图片,获取图片信息.

Pyinstaller是Python的一个发布工具,会将代码打包成可执行文件,十分方便.



[1]:https://github.com/justbilt/fnt_convert/blob/master/build/images2fnt.exe
[2]:https://github.com/justbilt/fnt_convert/blob/master/build/images2fnt
[3]:http://www.weste.net/tools/ASCII.asp
[4]:https://github.com/justbilt/fnt_convert
