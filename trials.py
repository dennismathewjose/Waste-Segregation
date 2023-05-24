def cnn():
    import pandas as pd
    import numpy as np
    import cv2
    from tqdm import tqdm
    from glob import glob

    import tensorflow as tf
    from tensorflow.keras import layers

    train_path = "/home/ananya/Desktop/Dataset/TRAIN"
    test_path = "/home/ananya/Desktop/Dataset/TEST"

    x_data = []
    y_data = []

    for category in glob(train_path+'/*'):
        for file in tqdm(glob(category+'/*')):
            img_array = cv2.imread(file)
            img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
            x_data.append(img_array) 
            y_data.append(category.split("/")[-1])
            
    data=pd.DataFrame({'image': x_data,'label': y_data})

    model = tf.keras.models.Sequential([
        layers.Conv2D(filters = 32,kernel_size = (3,3),activation = 'relu',input_shape = (224,224,3)),
        layers.MaxPooling2D(),
        layers.Conv2D(filters = 64,kernel_size = (3,3),activation = 'relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(filters = 128,kernel_size = (3,3), activation = 'relu'),
        layers.MaxPooling2D(),
        
        layers.Flatten(),
        layers.Dense(256,activation = 'relu'),
        layers.Dropout(0.5),
        layers.Dense(64, activation = 'relu'),
        layers.Dropout(0.5),
        layers.Dense(2,activation = 'sigmoid')
    ])
    print(model)
    return model

