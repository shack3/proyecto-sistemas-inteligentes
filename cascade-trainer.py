import cv2
import os
import time

# Definicion de la ventana de visualizacion.
window_name = 'Projector'
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


# Analisis de la carpeta de input de videos.

input_path = "cascade-trainer/input-videos/"
input_list = os.listdir(input_path)

output_positive = "cascade-trainer/output-images/positive-images/"
output_negative = "cascade-trainer/output-images/negative-images/"

"""
for i in range(len(input_list)):
    name = input_path + '/' + input_list[i]
    new_name = input_path + '/' + str(i) + '.mp4'
    os.rename(name, new_name)
"""

exit = False

for i in range(len(input_list)):
    
    if(not exit):

        cap = cv2.VideoCapture('cascade-trainer/input-videos/' + input_list[i])
        n_frame = 0
        while(cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = cap.read()
            n_frame = n_frame + 1
            if ret == True:
                
                ##time.sleep(0/1000)

                if not ret:
                    print('No hay mas tramas, saliendo')
                    break

                cv2.imshow(window_name, frame)

                pressedKey = cv2.waitKey(1)

                if pressedKey == ord('s'):
                    print('hola!')
                elif pressedKey == ord('q'):
                    break
                elif pressedKey == ord('z'):
                    exit = True
                    break
                elif pressedKey == ord('p'):
                    cv2.imwrite(output_positive + str(n_frame) + '.jpeg', frame)
                elif pressedKey == ord('n'):
                    cv2.imwrite(output_negative + str(n_frame) + '.jpeg', frame)
            else:
                break

        # When everything done, release the video capture object
        cap.release()
    else:
        break

"""
cap = cv2.VideoCapture('cascade-trainer/input-videos/' + input_list[0])

while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    
    ##time.sleep(0/1000)

    if not ret:
      print('No hay mas tramas, saliendo')
      break

    cv2.imshow(window_name, frame)

    pressedKey = cv2.waitKey(1)

    if pressedKey == ord('s'):
      print('hola!')
    elif pressedKey == ord('q'):
      break
  else:
    break
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows() 
"""
