from deepface import DeepFace
from tensorflow.keras.applications import ResNet50

# https://towardsdatascience.com/how-to-create-real-time-face-detector-ff0e1f81925f

# todo: add deepface model
image_height, image_width = 250, 250

base_model_ResNet50 = ResNet50(weights='Deepface', include_top=False, input_shape=(image_height, image_width, 3))

base_model_deepFace = DeepFace.build_model("")
