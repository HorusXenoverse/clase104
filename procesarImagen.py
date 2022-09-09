import cv2

import numpy as np

poster = cv2.imread("poster.jpg")

rocket2 = poster[120:360, 400:500]
poster[0:240, 500:600] = rocket2


texto = "Amo progamar en Byjust"
cv2.putText(poster, texto, (20,200), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale= 1, color=(0,0,255) )


cv2.imshow("Poster", poster)
cv2.waitKey(0)