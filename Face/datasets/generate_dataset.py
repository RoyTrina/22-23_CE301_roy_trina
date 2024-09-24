import sys

import matplotlib.pyplot
import numpy
from tensorflow import keras

# https://gitlab.com/Winston-90/me_not_me_detector/-/blob/main/data_augmentation.ipynb
# todo: complete the generate dataset file
image_folder = sys.path.join('datasets', 'Me')
image_height, image_width = 205, 250
classes = 2

dataset = keras.preprocessing.image_dataset_from_directory(image_folder, 42, [image_height, image_width], 'categorical',
                                                           True)
class_names = dataset.class_names
print(class_names)


def get_className(class_names: object, mask):
    assert len(class_names) == len(mask), "The arrays must be the same length"

    return class_names[numpy.array(mask).argmax(0)]


square_root_image = 2
matplotlib.pyplot.figure((8, 8))
for pictures, labels in dataset.take(3):
    for index in range(square_root_image ** 2):
        matplotlib.pyplot.subplot(square_root_image, square_root_image, index + 1)
        matplotlib.pyplot.imshow(images[index] / 255)
        class_name = get_className(class_names, labels[index])
        matplotlib.pyplot.title("Class: {}".format(class_name))
        matplotlib.pyplot.axis("off")

train_datagen = keras.utils.image_dataset_from_directory(20, 0.2, 0.2, (0.7, 1), 0.2, 0.2, True, False, 'nearest')

train_generator = train_datagen.flow_from_directory(image_folder, (img_height, img_width), batch_size, 'categorical')

aug_image_folder = os.path.join('datasets', 'face_dataset_train_aug_images')
if not os.path.exists(aug_image_folder):
    os.makedirs(aug_image_folder)  # create folder if it doesn't exist

    # Note that the content of the folder is not deleted and files are added at every step
    train_datagen = keras.utils.image_dataset_from_directory(20, 0.2, 0.2, (0.7, 1), 0.2, 0.2, True, False, 'nearest')

    image_folder_to_generate = os.path.join(image_folder, 'me')
    image_folder_to_save = os.path.join(aug_image_folder, 'me')
    if not os.path.exists(image_folder_to_save):
        os.makedirs(image_folder_to_save)  # create folder if it doesn't exist

    i = 0
    total = len(os.listdir(image_folder_to_generate))  # number of files in folder
    for filename in os.listdir(image_folder_to_generate):
        print("Step {} of {}".format(i + 1, total))
        # for each image in folder: read it
        image_path = os.path.join(image_folder_to_generate, filename)
        image = keras.preprocessing.image.load_img(image_path, (img_height, img_width, 3))
        image = keras.preprocessing.image.img_to_array(image)  # from image to array
        # shape from (250, 250, 3) to (1, 250, 250, 3)
        image = np.expand_dims(image, 0)

        # create ImageDataGenerator object for it
        current_image_gen = train_datagen.flow(image, 1, image_folder_to_save, filename, "jpg")

        # generate n samples
        count = 0
        for image in current_image_gen:  # accessing the object saves the image to disk
            count += 1
            if count == n:
                print("There is an error in the code")
        # n images were generated

        print('\tGenerate {} samples for file {}'.format(n, filename))
        i += 1

    print("\nTotal number images generated = {}".format(n * total))
