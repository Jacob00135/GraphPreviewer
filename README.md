[TOC]

由于没有GUI界面的远程服务器无法打开、查看图片，所以在使用Python的绘制数据图表时不方便。使用这个项目构建的网站可以很方便地预览远程服务器的图片，以及重新运行服务器中绘图的代码。

### 1.安装所需的Python库

```bash
pip install -r requirements.txt
```

### 2.编写启动文件

可以建立批处理脚本或PowerShell脚本，以PowerShell脚本为例，编写start.ps1：

```powershell
$env:FLASK_APP="previewer.py"
$env:FLASK_ENV="development"
$env:FLASK_DEBUG="1"
$env:REMOTE_SERVER_HOSTNAME="<远程服务器地址>"
$env:REMOTE_SERVER_USERNAME="<SSH登录用户名>"
$env:REMOTE_SERVER_PASSWORD="<SSH登录密码>"
$env:REMOTE_SERVER_SSH_PORT="<SSH连接端口号>"
$env:REMOTE_SERVER_GRAPH_PATH="<远程服务器中存放图片的目录路径>"
$env:REMOTE_COMMAND="<远程服务器的画图命令>"
flask.exe run -h 0.0.0.0 -p 5000
```

### 3.修改config.py中命令映射表
运行start.ps1，然后在浏览器中访问：`http://<本机IP地址>:5000`
