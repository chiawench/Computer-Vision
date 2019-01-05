import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
# number 1 to 10 data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
learning_rate = 0.5
xs = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.matmul(xs, W) + b

ys = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y, labels=ys))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.Session()
# important step

# tf.initialize_all_variables() no long valid from

# 2017-03-02 if using tensorflow >= 0.12

sess.run(tf.initialize_all_variables())

for i in range(500):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys})
    if i % 50 == 0:
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(ys, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        print(sess.run(accuracy, feed_dict={xs: mnist.test.images,
                                      ys: mnist.test.labels}))
