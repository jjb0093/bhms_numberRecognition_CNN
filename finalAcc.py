import cv2
import matplotlib.pyplot as plt
import numpy as np
from keras.models import load_model

def img_transform(img):
 image = cv2.imread(img)
 return (image/255)

test = []
name = []
for i in range(10):
 for j in range(91, 99):
  dir = 'train/img_test/img_'+str(j)+'_'+str(i)+'.jpg'
test.append(img_transform(dir))
name.append('img_'+str(j)+'_'+str(i)+'.jpg')

test = np.array(test)
model = load_model('model_final.h5')
prediction = model.predict_proba(test)

success = 0
for i in range(len(test)):
 output = prediction[i]
 percent = round(output[np.argmax(output)], 2)
 number = np.argmax(output)
 if(int(i/10) == number):
  result = 'true'
  success += 1
 else:
  result = 'wrong'
  
 plt.imshow(test[i])
 plt.title('OUTPUT : {0}, PERCENT : {1}'.format(number, round(percent, 2)))
 plt.show()
 
 print('{0} : {1} -> {2}'.format(name[i], number, result))
 print("정확도: {0}".format((success/len(test)*100)))
