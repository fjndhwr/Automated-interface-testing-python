# 自动化接口测试使用
##### 作者：黄文榕
##### 时间：2020-04-23
##### 版本：V0.0.1
#####  修改：
|更新时间|更新人|作用|
|--|--|--|

### 配置
```
url: http://192.168.8.90:30097 #url地址
out_path: d:/md/ #输出目录
tester: hwr #测试人员
version: V4.1.0 #测试版本
head: # 头文件 可增加或者减少，但不可减为0
  Accept: application/json, text/plain, */*
  Cookie: jenkins-timestamper-offset=-28800000; JSESSIONID=3d97136c-df5f-498f-acb8-daccf7fc73f3
```

### Excel 文件
| 属性名称 | 作用 | 顺序 | 备注 |
| --- | --- | --- | --- |
path | 路径地址 | 1 
params | 传参 | 2 | json格式
medthod | 请求方式 | 3 | get/post
return | 对于返回参数的验证 | 4 | json格式
error_msg | 可预料报错  | 5 | json格式 list
name | 接口名称 | 6 |
author | 接口作者 | 7 | 接口更新最好是更新作者或者写多个作者

#### 属性详解
##### params
- 如果某个属性需要传入多个值可以用 # 进行分割
- 导入一组之后该软件会自动生成每个属性置为空各生成1组，和随机生成字符串10组
- 没有参数也必须填值否则该条会无法导入，无参数时输入{}

##### return
- return输入的参数 key为参数名 value为该属性的类型
- 没有参数也必须填值否则该条会无法导入，无参数时输入{}
- return的属性类型与java不同比对表入下
- 如果data返回的是list型时，格式类型为[{}]或[]即可，里面的参数只需填入一个
- 如果data返回的是json直接，格式类型为{}
###### 输入参数类型
仅为部分如果有其他需求请联系管理人员
| java类型 | 所需要输入的类型 |
| --- | ---|
String | str
Integer | int

##### error_msg
- 没有参数也必须填值否则该条会无法导入，无参数时输入[]
- json的 list 类型，如：["xxx不能为空"]

#### 其他
- 只有 name 和 author 能为空其他都不能填入空值

### 其他注意事项
- 写好测试用例之后打开app.exe即可使用
- 为了简单查看到日志，建议在cmd中(打开相应的目录在上面的路径框输入cmd，然后输入app.exe打开)
- 如果代码出现异常请联系管理员
- 代码每隔三秒调用一次接口所以测试需要一定时长，控制台出现 test end 字样为测试结束
- 有其他修改意见请联系管理员