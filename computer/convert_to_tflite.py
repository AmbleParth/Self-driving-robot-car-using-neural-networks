import tensorflow as tf

# Load the Keras model
keras_model = tf.keras.models.load_model('model_combined1.h5')


# Convert the Keras model to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(keras_model)
tflite_model = converter.convert()

# Save the TensorFlow Lite model to a file
with open('C:/Users/SARTHAK AMBLE/Desktop/Project/model_combined1.tflite', 'wb') as f:
    f.write(tflite_model)
