import tensorflow as tf

tf.zeros(2)

d = tf.random.normal([2, 2], mean=0.5, stddev=1)
print(d)
e = tf.random.truncated_normal([2, 2], mean=0.5, stddev=1)
print(e)

# 生成均匀分布随机数 [minval， maxval) z最小值 最大值
f = tf.random.uniform([2, 3], minval=0, maxval=1)
print(f)

