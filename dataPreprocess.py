from keras.preprocessing.image import ImageDataGenerator

train_dir = 'train/img_train/'
valid_dir = 'train/img_valid'

train_datagen = ImageDataGenerator(rescale = 1./255, rotation_range = 25,
width_shift_range=0.2, height_shift_range=0.2)
valid_datagen = ImageDataGenerator(rescale = 1./255, rotation_range = 25,
width_shift_range=0.2, height_shift_range=0.2)

train_generator = train_datagen.flow_from_directory(train_dir, target_size = (108, 108), batch_size = 20, class_mode = 'categorical')
valid_generator = valid_datagen.flow_from_directory(valid_dir, target_size = (108, 108), batch_size = 20, class_mode = 'categorical')
