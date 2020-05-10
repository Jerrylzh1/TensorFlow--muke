import tensorflow as tf

with tf.GradientTape() as tape:
    # 标记为可训练函数
    x = tf.Variable(tf.constant(3.0))
    print(x)
    # 经次方操作
    y = tf.pow(x, 2)
    print(y)

grad = tape.gradient(y, x)
print(grad)
