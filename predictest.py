import cv2
import numpy as np
import trials

model = trials.cnn()
def prediction(img):
    img = cv2.resize(img, (224,224),3)
    img = np.reshape(img, [-1,224,224,3])
    result = np.argmax(model.predict(img))
    return result
