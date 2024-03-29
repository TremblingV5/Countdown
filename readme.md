# 下班计时器 Free Count Down!

这是一个非常简单的静态网页，主要功能就是现实你现在离下班还有多久。

当然提醒你下班还有多久也是有代价的，那就是如果你下班晚了会被阴阳怪气！当然你周末和节假日还加班也会被嘲讽。

线上地址：[你该下班了！](http://965happy.top:965)

默认的下班时间是下午6点，也可以点击“自定义下班时间”进行设置。设置的内容储存在`localStorage`中。

## 如何运行

1. 下载仓库到本地
2. 双击打开（纯纯废话）

## 如何部署

目前我的线上地址是在正常运行的（我还专门搞了个域名），所以其实没啥自行部署的。如果非要部署，那么可以：

1. 如果你有任何一个类似`nginx`这样能部署静态网页的服务，直接把本仓库代码丢进去即可。（`docker-compose.yml`中也是启动了一个`nginx`把代码丢进去）
2. 如果你懒得麻烦但是服务器资源比较丰富，可以装一个`Docker`，然后`docker-compose up -d`。（杀鸡用牛🔪）

如果是使用上面的方法2，记得把`nginx/conf.d/default.conf`中的域名修改为自己的域名。

## 如果你有好点子

很显然，这是一个整活项目。所以，如果你有任何整活或是稀奇古怪的想法，欢迎提Issue或者提PR，不胜感激。如果你愿意，你可以提需求，说想法，或是直接动手优化界面或者优化逻辑。从轻量化的角度出发，希望新的功能尽可能只依赖前端和浏览器功能进行实现。

鄙人不善前端，所以非常欢迎能对页面或是逻辑代码进行优化！

**希望各位工作中能多点乐趣，工作也能早点做完做好。**

## 功能及配置

### 自定义域名

在`./nginx/conf.d/default.conf`中，配置`server->server_name`为自定义的域名即可。

### 自部署时天气API KEY和SECRET配置

1. 在此[网站](https://tianqiapi.com/index/doc?version=day)注册账号，并获取appid和appsecret
2. 在在`./nginx/conf.d/default.conf`中，配置`add_header Set-Cookie`的内容为`appid={appid},appsecret={appsecret}; path=/`

### 随机听歌

数据来源于第三方接口，请求的数据为网易云音乐热榜。可以点击“换一首听”按钮去加载一首其他随机歌曲。

### 热榜聚合

数据来源于第三方接口，数据存储在`localStorage`中，请求到的数据会保存1个小时。
