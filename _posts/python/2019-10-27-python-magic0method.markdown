---
layout: post
title: "Python中的魔术方法"
date: 2019-10-27 
tags: Python solution basis
---


### 起步
<table class="t_table" cellspacing="0">
<tbody>
<tr>
<td width="30%">
<div align="center"><span style="font-family: 'Microsoft YaHei'; font-size: 15px;"><strong>魔法方法</strong></span></div>
</td>
<td>
<div align="center"><span style="font-family: 'Microsoft YaHei'; font-size: 15px;"><strong>含义</strong></span></div>
</td>
</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">&nbsp;</span></td>
<td>
<div align="left">
<div align="center"><span style="color: #ff0000; font-family: 'Microsoft YaHei'; font-size: 15px;"><strong>基本的魔法方法</strong></span></div>
</div>
</td>
</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__new__(cls[, ...])</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">1. __new__ 是在一个对象实例化的时候所调用的第一个方法</span><br><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">2. 它的第一个参数是这个类，其他的参数是用来直接传递给 __init__ 方法</span><br><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">3. __new__ 决定是否要使用该 __init__ 方法，因为 __new__ 可以调用其他类的构造方法或者直接返回别的实例对象来作为本类的实例，如果 __new__ 没有返回实例对象，则 __init__ 不会被调用</span><br><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">4. __new__ 主要是用于继承一个不可变的类型比如一个 tuple 或者 string</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__init__(self[, ...])</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">构造器，当一个实例被创建的时候调用的初始化方法</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__del__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">析构器，当一个实例被销毁的时候调用的方法</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__call__(self[, args...])</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">允许一个类的实例像函数一样被调用：x(a, b) 调用 x.__call__(a, b)</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__len__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当被 len() 调用时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__repr__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当被 repr() 调用或者直接执行对象时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__str__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当被 str() 调用或者打印对象时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__bytes__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当被 bytes() 调用时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__hash__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当被 hash() 调用时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__bool__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当被 bool() 调用时的行为，应该返回 True 或 False</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__format__(self, format_spec)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当被 format() 调用时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">&nbsp;</span></td>
<td>
<div align="center"><span style="color: #ff0000; font-family: 'Microsoft YaHei'; font-size: 15px;"><strong>有关属性</strong></span></div>















</td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__getattr__(self, name)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当用户试图获取一个不存在的属性时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__getattribute__(self, name)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当该类的属性被访问时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__setattr__(self, name, value)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当一个属性被设置时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__delattr__(self, name)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当一个属性被删除时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__dir__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当 dir() 被调用时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__get__(self, instance, owner)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当描述符的值被取得时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__set__(self, instance, value)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当描述符的值被改变时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__delete__(self, instance)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当描述符的值被删除时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">&nbsp;</span></td>
<td>
<div align="center"><span style="color: #ff0000; font-family: 'Microsoft YaHei'; font-size: 15px;"><strong>比较操作符</strong></span></div>















</td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__lt__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义小于号的行为：x &lt; y 调用 x.__lt__(y)</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__le__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义小于等于号的行为：x &lt;= y 调用 x.__le__(y)</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__eq__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义等于号的行为：x == y 调用 x.__eq__(y)</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__ne__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义不等号的行为：x != y 调用 x.__ne__(y)</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__gt__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义大于号的行为：x &gt; y 调用 x.__gt__(y)</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__ge__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义大于等于号的行为：x &gt;= y 调用 x.__ge__(y)</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">&nbsp;</span></td>
<td>
<div align="center"><span style="color: #ff0000; font-family: 'Microsoft YaHei'; font-size: 15px;"><strong>算数运算符</strong></span></div>















</td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__add__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义加法的行为：+</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__sub__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义减法的行为：-</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__mul__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义乘法的行为：*</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__truediv__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义真除法的行为：/</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__floordiv__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义整数除法的行为：//</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__mod__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义取模算法的行为：%</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__divmod__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当被 divmod() 调用时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__pow__(self, other[, modulo])</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当被 power() 调用或 ** 运算时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__lshift__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义按位左移位的行为：&lt;&lt;</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__rshift__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义按位右移位的行为：&gt;&gt;</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__and__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义按位与操作的行为：&amp;</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__xor__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义按位异或操作的行为：^</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__or__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义按位或操作的行为：|</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">&nbsp;</span></td>
<td>
<div align="center"><span style="color: #ff0000; font-family: 'Microsoft YaHei'; font-size: 15px;"><strong>反运算</strong></span></div>















</td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__radd__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">（与上方相同，当左操作数不支持相应的操作时被调用）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__rsub__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">（与上方相同，当左操作数不支持相应的操作时被调用）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__rmul__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">（与上方相同，当左操作数不支持相应的操作时被调用）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__rtruediv__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">（与上方相同，当左操作数不支持相应的操作时被调用）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__rfloordiv__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">（与上方相同，当左操作数不支持相应的操作时被调用）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__rmod__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">（与上方相同，当左操作数不支持相应的操作时被调用）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__rdivmod__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">（与上方相同，当左操作数不支持相应的操作时被调用）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__rpow__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">（与上方相同，当左操作数不支持相应的操作时被调用）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__rlshift__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">（与上方相同，当左操作数不支持相应的操作时被调用）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__rrshift__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">（与上方相同，当左操作数不支持相应的操作时被调用）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__rand__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">（与上方相同，当左操作数不支持相应的操作时被调用）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__rxor__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">（与上方相同，当左操作数不支持相应的操作时被调用）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__ror__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">（与上方相同，当左操作数不支持相应的操作时被调用）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">&nbsp;</span></td>
<td>
<div align="center"><span style="color: #ff0000; font-family: 'Microsoft YaHei'; font-size: 15px;"><strong>增量赋值运算</strong></span></div>















</td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__iadd__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义赋值加法的行为：+=</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__isub__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义赋值减法的行为：-=</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__imul__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义赋值乘法的行为：*=</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__itruediv__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义赋值真除法的行为：/=</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__ifloordiv__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义赋值整数除法的行为：//=</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__imod__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义赋值取模算法的行为：%=</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__ipow__(self, other[, modulo])</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义赋值幂运算的行为：**=</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__ilshift__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义赋值按位左移位的行为：&lt;&lt;=</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__irshift__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义赋值按位右移位的行为：&gt;&gt;=</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__iand__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义赋值按位与操作的行为：&amp;=</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__ixor__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义赋值按位异或操作的行为：^=</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__ior__(self, other)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义赋值按位或操作的行为：|=</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">&nbsp;</span></td>
<td>
<div align="center"><span style="color: #ff0000; font-family: 'Microsoft YaHei'; font-size: 15px;"><strong>一元操作符</strong></span></div>















</td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__pos__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义正号的行为：+x</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__neg__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义负号的行为：-x</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__abs__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当被 abs() 调用时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__invert__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义按位求反的行为：~x</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">&nbsp;</span></td>
<td>
<div align="center"><span style="color: #ff0000; font-family: 'Microsoft YaHei'; font-size: 15px;"><strong>类型转换</strong></span></div>















</td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__complex__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当被 complex() 调用时的行为（需要返回恰当的值）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__int__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当被 int() 调用时的行为（需要返回恰当的值）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__float__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当被 float() 调用时的行为（需要返回恰当的值）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__round__(self[, n])</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当被 round() 调用时的行为（需要返回恰当的值）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__index__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">1. 当对象是被应用在切片表达式中时，实现整形强制转换</span><br><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">2. 如果你定义了一个可能在切片时用到的定制的数值型,你应该定义 __index__</span><br><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">3. 如果 __index__ 被定义，则 __int__ 也需要被定义，且返回相同的值</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">&nbsp;</span></td>
<td>
<div align="center"><span style="color: #ff0000; font-family: 'Microsoft YaHei'; font-size: 15px;"><strong>上下文管理（with 语句）</strong></span></div>















</td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__enter__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">1. 定义当使用 with 语句时的初始化行为</span><br><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">2. __enter__ 的返回值被 with 语句的目标或者 as 后的名字绑定</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__exit__(self, exc_type, exc_value, traceback)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">1. 定义当一个代码块被执行或者终止后上下文管理器应该做什么</span><br><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">2. 一般被用来处理异常，清除工作或者做一些代码块执行完毕之后的日常工作</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">&nbsp;</span></td>
<td>
<div align="center"><span style="font-family: 'Microsoft YaHei'; font-size: 15px;"><strong><span style="color: #ff0000;">容器类型</span></strong></span></div>















</td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__len__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当被 len() 调用时的行为（返回容器中元素的个数）</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__getitem__(self, key)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义获取容器中指定元素的行为，相当于 self[key]</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__setitem__(self, key, value)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义设置容器中指定元素的行为，相当于 self[key] = value</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__delitem__(self, key)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义删除容器中指定元素的行为，相当于 del self[key]</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__iter__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当迭代容器中的元素的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__reversed__(self)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当被 reversed() 调用时的行为</span></td>















</tr>
<tr>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">__contains__(self, item)</span></td>
<td><span style="font-family: 'Microsoft YaHei'; font-size: 15px;">定义当使用成员测试运算符（in 或 not in）时的行为</span></td>















</tr>















</tbody>














</table>