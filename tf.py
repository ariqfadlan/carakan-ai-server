import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class Model:
    def __init__(self):
        self.model = load_model('carakan-ai.h5')
        self.label = {0:'ba', 1: 'ca', 2: 'da', 3: 'dha', 4: 'ga',
            5: 'ha', 6: 'ja', 7: 'ka', 8: 'la', 9: 'ma',
            10:'na', 11:'nga', 12:'nya', 13:'pa', 14:'ra',
            15:'sa', 16:'ta', 17:'tha', 18:'wa', 19:'ya'
        }

    def compile(self):
        self.model.compile(loss='categorical_crossentropy',
                optimizer='rmsprop',
                metrics=['accuracy'])
    def predict_model(self, img):
        arr_prediction = self.model.predict(img)
        return self.label[np.argmax(arr_prediction)]
