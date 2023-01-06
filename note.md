
json解析器技巧：

1. 运算符重载, 关系运算符，
2. value types
   1. bool, int, double, char* ,string
   2. Value 抽象
3. 类型转换运算符
4. 递归分解，迭代器技巧
5. 字符串处理
6. 关键结构：json：kv -- map， vector ： list
7. 输入输出流
8. 类型定义与校验
9.  定位index处理

序列化技巧:
1. SERIALIZE 宏依次将成员变量进行序列化
2. 变参，多参数，-》单参数
3. 模版函数递归  -》 read<T> 、write<T>
4. 各种类型的序列化函数
   1. char,bool,int32,int64,float,double,
   2. string, vector<T> , list<T>, map<k,v>
   3. serializable，
   4. __VA_ARGS__ 多参数
5. 输入输出流重载
6. 格式 TLV编码： type + len + values


反射技巧：
1. 宏定义的巧用，方便
2. 模版单例模式，注册类和函数，std::map
3. 注册-相当于序列化类和函数
4. 调用相当于反序列化
5. function 包裹一切函数，typedef std::function<R(decltype(this), Args...)>
6.  ... 多参数 __VA_ARGS__