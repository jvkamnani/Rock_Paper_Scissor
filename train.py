import numpy as np
import tensorflow as tf
import os

base_model = tf.keras.applications.ResNet50(weights='imagenet', include_top = False)

x = base_model.output
x = tf.keras.layers.GlobalAveragePooling2D()(x)

x = tf.keras.layers.Dense(1024, activation='relu')(x)
x = tf.keras.layers.Dropout(0.5)(x)
x = tf.keras.layers.Dense(1024, activation='relu')(x)
x = tf.keras.layers.Dropout(0.5)(x)
x = tf.keras.layers.Dense(1024, activation='relu')(x)
x = tf.keras.layers.Dropout(0.5)(x)
x = tf.keras.layers.Dense(512, activation='relu')(x)
preds = tf.keras.layers.Dense(3, activation ='softmax')(x)

train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(preprocessing_function=tf.keras.applications.resnet50.preprocess_input)
valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(preprocessing_function=tf.keras.applications.resnet50.preprocess_input)

WORKING_DIRECTORY = os.getcwd()

train_generator = train_datagen.flow_from_directory(WORKING_DIRECTORY + '/train_data', 
                                                   target_size = (224, 224),
                                                   color_mode = 'rgb',
                                                   batch_size = 32,
                                                   class_mode = 'categorical',
                                                   shuffle = True)
valid_generator = valid_datagen.flow_from_directory(WORKING_DIRECTORY + '/valid_data', 
                                                   target_size = (224, 224),
                                                   color_mode = 'rgb',
                                                   batch_size = 32,
                                                   class_mode = 'categorical',
                                                   shuffle = True)

model = tf.keras.models.Model(inputs=base_model.input, outputs=preds)

for layer in model.layers[:175]:
  layer.trainable = False

for layer in model.layers[175:]:
  layer.trainable = True

model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(train_generator, validation_data=valid_generator, epochs = 8)

model.save("mymodel.h5")