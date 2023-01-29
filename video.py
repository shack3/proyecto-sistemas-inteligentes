import cv2

#Arreglo vacío
img_array = []

#For para leer imagenes desde un directorio
for x in range (0,210):
    path = 'C:\\Users\\alvar\\Desktop\\Sistemas\\video\\frame%d.jpg' % x
    img = cv2.imread(path)
    img_array.append(img)

#Tamaño de la última imagen alto y ancho
height, width  = img.shape[:2]

video = cv2.VideoWriter('db1.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 5, (width,height))

#For para guardar frames en un video
for i in range(len(img_array)):
    video.write(img_array[i])

video.release()