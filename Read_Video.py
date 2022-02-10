import cv2

# Usar "0" para la cámara web
#vid = cv2.VideoCapture(0)

vid = cv2.VideoCapture("AnthonyShkraba.mp4")

if(vid.isOpened()==False):
    print("No es posible leer la entrada.")


height  = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

out = cv2.VideoWriter('Boxing.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, (width,height))

while(True):
      
    # Captura el video
    # cuadro a cuadro
    ret, frame = vid.read()

    cv2.imshow("Camara web", frame) #cv2 no acepta caracteres especiales como el acento en "Cámara"
    out.write(frame)
    if cv2.waitKey(25) == 32:
        break

vid.release()
out.release()

cv2.destroyAllWindows()
