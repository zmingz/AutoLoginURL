自动登录网站程序
====
程序用于自动登陆多个酒店管理平台网站，包括自动登陆多个网页，包括输入账号密码和识别验证码，最后自动点击登陆。

提示说明
----
* 本程序运行环境须要提前安装`firefox`浏览器和下载`geckodriver.exe`,并把geckodriver.exe所在路径添加到环境变量PATH中；
* python还需安装`selenium`、`tesseract-ocr`、`PIL`等库，tesseract-ocr的路径添加到环境变量PATH中；
* 需要提前对tesseract-ocr进行训练才能对验证码有较高的识别正确率。

程序运行流程
----
* 打开网页；
* 识别出账号和密码框的位置并输入账号密码；
* 识别出验证码的位置并截图保存，通过开源的OCR技术识别出验证码后输入验证码；
* 模拟点击登录

参考资料
----
* [程序原理](http://m.blog.csdn.net/article/details?id=53612197)
* [审查和操作元素](http://www.cnblogs.com/eastmount/p/4810690.html) 
* [OCR识别验证码](http://blog.csdn.net/a349458532/article/details/51490291)
* [样本训练](http://www.cnblogs.com/wzben//p/5930538.html)  
