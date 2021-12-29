"""This file is for testing tensorflow installation
without the need to install jupyter notebook"""

# Import `tensorflow`
import tensorflow as tf

# Initialize two constants
x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])

# Multiply
result = tf.multiply(x1, x2)

# Intialize the Session
sess = tf.compat.v1.Session()

# Print the result
print(sess.run(result))

# Close the session
sess.close()