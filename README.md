# AutoLoginURL
本脚本用于自动登陆多个酒店管理平台ebooking：自动登陆多个网页，包括输入账号密码和识别验证码，最后自动点击登陆。

说明：
1、本程序运行环境须要提前安装firefox浏览器和geckodriver.exe,并把geckodriver.exe添加到环境变量   PATH中；
2、python还需安装selenium、tesseract-ocr、PIL等库，tesseract-ocr的路径添加到环境变量PATH中；
3、需要提前对tesseract-ocr进行训练才能对验证码有较高的识别正确率。

程序原理：
1、打开网页；
2、识别出账号和密码框的位置并输入账号密码；
3、识别出验证码的位置并截图保存，通过开源的OCR技术识别出验证码后输入验证码；
4、模拟点击登录

参考资料：
程序原理         http://m.blog.csdn.net/article/details?id=53612197
审查和操作元素   http://www.cnblogs.com/eastmount/p/4810690.html
识别验证码       http://blog.csdn.net/a349458532/article/details/51490291
样本训练         http://www.cnblogs.com/wzben//p/5930538.html
