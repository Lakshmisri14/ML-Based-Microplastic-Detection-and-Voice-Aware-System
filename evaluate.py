import numpy as np
from tensorflow.keras.models import load_model
from sklearn.metrics import classification_report, confusion_matrix
from config import TEST_DIR, IMG_HEIGHT, IMG_WIDTH, BATCH_SIZE, MODEL_SAVE_PATH
from utils import get_data_generators

def evaluate():
    _, _, test_gen = get_data_generators(TEST_DIR, TEST_DIR, IMG_HEIGHT, IMG_WIDTH, BATCH_SIZE)
    model = load_model(MODEL_SAVE_PATH)

    Y_pred = model.predict(test_gen)
    y_pred = np.round(Y_pred).astype(int)

    print("Classification Report:")
    print(classification_report(test_gen.classes, y_pred))

    print("Confusion Matrix:")
    print(confusion_matrix(test_gen.classes, y_pred))

if __name__ == "__main__":
    evaluate()
