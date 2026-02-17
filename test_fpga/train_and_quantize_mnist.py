import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# 1) Load and preprocess MNIST
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = (x_train / 255.0).astype("float32")
x_test  = (x_test  / 255.0).astype("float32")
x_train = x_train.reshape(-1, 28, 28, 1)
x_test  = x_test.reshape(-1, 28, 28, 1)

# 2) Define a small CNN (LeNet-style)
model = keras.Sequential([
    layers.Conv2D(32, 3, activation="relu", input_shape=(28, 28, 1)),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, activation="relu"),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(10, activation="softmax"),
])

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

print(">>> Training CNN...")
model.fit(x_train, y_train, epochs=5, batch_size=128,
          validation_data=(x_test, y_test), verbose=2)

# 3) Save Keras model
model.save("cnn_model.h5")
print("✓ Saved cnn_model.h5")

# 4) Convert to FP32 TFLite
print(">>> Converting to FP32 TFLite...")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_fp32 = converter.convert()
with open("cnn_model_fp32.tflite", "wb") as f:
    f.write(tflite_fp32)
print("✓ Saved cnn_model_fp32.tflite")

# 5) Full INT8 post-training quantization
def representative_dataset():
    for i in range(200):
        yield [x_train[i:i+1]]  # float32 in [0,1]

print(">>> Converting to INT8 TFLite...")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8
tflite_int8 = converter.convert()
with open("cnn_model_int8_quantized.tflite", "wb") as f:
    f.write(tflite_int8)
print("✓ Saved cnn_model_int8_quantized.tflite")

print("ALL DONE: Models are ready for Zynq!")
