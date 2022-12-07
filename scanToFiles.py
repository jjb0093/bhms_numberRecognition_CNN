import cv2

for i in range(10):
 img = cv2.imread('scan/img_'+str(i+1)+'.jpg')
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 img_resize = cv2.resize(gray, (int(img.shape[1] * 0.5), int(img.shape[0] * 0.5)))
 
 for k in range(4):
   for j in range(3):
     if(3*k + j == 10):
       break
   img_crop = img_resize[116+(168*k):284+(168*k), 21+(168*j):189+(168*j)]
   img_crop_2 = img_crop[10:158, 10:158]
   cv2.imwrite('images/'+str(3*k+j)+'/img_'+str(i*2+1)+'.jpg', img_crop_2)
    
 for k in range(4):
   for j in range(3):
     if(3*k + j == 10):
       break
   img_crop = img_resize[116+(168*k):284+(168*k), 618+(168*j):786+(168*j)]
   img_crop_2 = img_crop[10:158, 10:158]
   cv2.imwrite('images/'+str(3*k+j)+'/img_'+str(i*2+2)+'.jpg', img_crop_2)
