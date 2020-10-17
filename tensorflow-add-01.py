import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

a = tf.constant([5,5,5], tf.float32, name='A')
b = tf.placeholder(tf.float32, shape=[3], name='B')
c = tf.add(a,b, name="Add")

with tf.Session() as sess:
    d = {b:[1,2,3]}
    print(sess.run(c,feed_dict=d))
