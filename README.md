树莓派上的 豆瓣fm
================================

现在处于开发中。。。。


pifm.c 为开源代码


install, 在树莓派上操作
----------

克隆代码

```
git clone
```


ubuntu下安装redis数据库

```
sudo  apt-get install redis-server
```

安装相关python模块

```
sudo pip install redis
```

config
--------------

需要修改config.py,添加豆瓣账号的和密码

```
email = "[your email]"
password = "[your password]"
```

run
--------

```
sudo python2 player.py
```