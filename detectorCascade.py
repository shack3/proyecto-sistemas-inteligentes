import cv2
stop_color = (0,0,255)
ceda_color = (255,255,255)
rotonda_color =(255,0,0)
peatones_color =(0,255,0)

stop_cascade = cv2.CascadeClassifier('C:\\Users\\alvar\\Desktop\\Sistemas\\Stop.xml')
ceda_cascade = cv2.CascadeClassifier('C:\\Users\\alvar\\Desktop\\Sistemas\\Ceda.xml')
rotonda_cascade = cv2.CascadeClassifier('C:\\Users\\alvar\\Desktop\\Sistemas\\Rotonda.xml')
peatones_cascade= cv2.CascadeClassifier('C:\\Users\\alvar\\Desktop\\Sistemas\\Peatones.xml')

capture = cv2.VideoCapture('C:\\Users\\alvar\\Desktop\\Sistemas\\videoprueba.mp4')

while(capture.isOpened()):
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    stopSigns = stop_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in stopSigns:
        frame = cv2.putText(frame,'STOP',(x-5,y-10),cv2.FONT_HERSHEY_DUPLEX,1,stop_color,2)
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),stop_color,2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cedaSigns = ceda_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in cedaSigns:
        frame = cv2.putText(frame,'CEDA',(x-5,y-10),cv2.FONT_HERSHEY_DUPLEX,1,ceda_color,2)
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),ceda_color,2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    rotondaSigns = rotonda_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in rotondaSigns:
        frame = cv2.putText(frame,'ROTONDA',(x-5,y-10),cv2.FONT_HERSHEY_DUPLEX,1,rotonda_color,2)
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),rotonda_color,2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w] 

    peatonesSings = peatones_cascade.detectMultiScale(gray, 1.3, 5)  
    for (x,y,w,h) in peatonesSings:
        frame = cv2.putText(frame,'PEATONES',(x-5,y-10),cv2.FONT_HERSHEY_DUPLEX,1,peatones_color,2)
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),peatones_color,2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv2.imshow('frame',frame)
    pressedKey = cv2.waitKey(1)
    if pressedKey ==  ord('q'):break
capture.release()
cv2.destroyAllWindows()

    