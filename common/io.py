import numpy as np
import cv2 as cv

def load_image(filename: str, downscale_factor:int = 1)->np.ndarray:
    img = cv.imread( filename )
    if(downscale_factor > 1):
        img = cv.resize(img, (img.shape[1]//downscale_factor, img.shape[0]//downscale_factor))
    return img