# YMF
simple poc framework
YMF POC框架编写
Day1 – POC框架的思考
POC框架功能主要有2个方面：

1）	提供POC给用户调用测试

2）	便于用户编写自己的POC

针对第一点，这是后期框架成熟后需要大家长时间的分享和集成；
编写重点放在第二点，如何编写一个能易于用户编写自己POC的环境。
参考Tangscan先设计出一个通用POC结构（YmfPoc）并自己根据这个结构编写一个POC（libssh）
暂时没有什么思路，先写一下基础函数（get_poc_name_description）获取所有poc的名字和description。

Day2 – 功能细化并实现

1）先添加2个分类system和Information并根据YmfPoc框架简单编写几个poc（poc命名也按照规范，美观）

2）功能方面：
1.	针对一个URL进行批量poc验证
2.	针对多个URL进行单个poc验证
3.	针对多个URL进行批量poc验证
实现上述功能，首先先决定好用线程还是进程，在angelSword中用了进程池并发，但是针对密集IO操作，应该用线程比较合适，故决定用线程池并发执行poc；

首先完成pocdb获取所有poc对象，修改get_poc_name_description函数，改为获取所有poc类名和描述，然后使用eval动态调用类；
这样做的好处在于后续只需要编写poc放在目录分好类的目录下即可，不必在pocdb修改其他代码。

修改pocdb为pocManager，将所有poc类存放在poc_dict字典中，定义poc_set做管理，区分已经验证的poc和没有验证的poc。

完成启动文件Ymf.py多线程类的基本实现

完成具体业务功能Ymf.py（输出比较粗糙）

base提供基础属性、函数等
