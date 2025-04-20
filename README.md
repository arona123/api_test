### 该项目仅作为本人练习api使用。该项目仅实现最基本的利用bv号下载视频功能

学习记录：
![image](https://github.com/user-attachments/assets/08151fed-5725-4638-85ab-e36141d518d2)
通过这样的步骤实现发送api请求

![image](https://github.com/user-attachments/assets/fa9c7b21-913b-4295-8192-2e3b880cd44d)

返回的数据为json格式，如图。

![image](https://github.com/user-attachments/assets/f980ec9c-d138-445a-adb0-b0a810c7a383)

利用respons.json()将相应内容保存
data为键值对数据类型，通过如图方式进行使用

本项目一共用到三个api
https://api.bilibili.com/x/web-interface/view （获取视频信息）
https://api.bilibili.com/x/player/playurl  (获取视频下载url)
根据上一行的url下载视频
