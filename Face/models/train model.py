from deepface import DeepFace

# https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet50
# https://towardsdatascience.com/complete-image-augmentation-in-opencv-31a6b02694f5

# todo: add Res50 architecture model for comparison
deepface_model_me = DeepFace.build_model("DeepFace")

deepface_model_not_me = DeepFace.build_model("DeepFace")

deepface_model_me.summary()
deepface_model_not_me.summary()
