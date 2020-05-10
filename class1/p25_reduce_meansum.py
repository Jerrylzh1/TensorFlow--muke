import tensorflow as tf

x = tf.constant([[1, 2, 3], [2, 2, 3]])
print("x:", x)
print("mean of x:", tf.reduce_mean(x))  # 求x中所有数的均值
print("sum of x:", tf.reduce_sum(x, axis=1))  # 求每一行的和

a = 8
b = 9
# fa = tf.sqrt(b)
# print("进行操作的开发数字为：", fa)
k = tf.add(a, b)
o = tf.subtract(b, a)
print(k)
print(o)

# a = tf.ones([1, 3])
# b = tf.fill([1, 3], 3.)
# print(a)
# print(b)
# print(tf.add(a, b))
# print(tf.subtract(a, b))
# print(tf.multiply(a, b))
# print(tf.divide(b, a))

# 进行操作平方、次方和平方
a = tf.fill([1, 2], 3.)
print(a)

# 次方
print(tf.pow(a, 3))
# 平方
print(tf.square(a))
# 开方
print(tf.sqrt(a))

# matmul函数
a = tf.ones([3, 2])
b = tf.fill([2, 3], 3.)
print(tf.matmul(a, b))
