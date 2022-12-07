history = model.fit_generator(train_generator, steps_per_epoch = 35, epochs = 50, validation_data = valid_generator, validation_steps = 10)
model.save('model_final.h5')

import matplotlib.pyplot as plt

accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(accuracy) + 1)

plt.plot(epochs, accuracy, 'bo', label = 'Training Accuracy')
plt.plot(epochs, val_accuracy, 'b', label = 'Validation Accuracy')
plt.legend()
plt.show()
