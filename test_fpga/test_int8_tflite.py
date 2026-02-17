import numpy as np
import tensorflow as tf
from tensorflow import keras

# Load MNIST test data
(_, _), (x_test, y_test) = keras.datasets.mnist.load_data()
x_test = (x_test / 255.0).astype("float32")

# Load INT8 TFLite model
interpreter = tf.lite.Interpreter(model_path="cnn_model_int8_quantized.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Test first image
sample_index = 0
img = x_test[sample_index].reshape(1,28,28,1)
in_scale, in_zero = input_details[0]['quantization']
img_q = (img / in_scale + in_zero).astype(np.int8)

interpreter.set_tensor(input_details[0]['index'], img_q)
interpreter.invoke()

out = interpreter.get_tensor(output_details[0]['index'])
out_scale, out_zero = output_details[0]['quantization']
probs = (out.astype(np.float32) - out_zero) * out_scale

predicted_class = np.argmax(probs)
true_class = y_test[sample_index]

print(f"Predicted Class: {predicted_class}")
print(f"True Class: {true_class}")
