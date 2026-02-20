import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRAIN_DIR = "C:/Users/Lakshmi Sri M/OneDrive/Documents/Desktop/MP1/data/train/1_Training/1_Training"
TEST_DIR = "C:/Users/Lakshmi Sri M/OneDrive/Documents/Desktop/MP1/data/train/3_Testing/3_Testing"

MODEL_SAVE_PATH = os.path.join(BASE_DIR, 'microplastic_model.h5')

# Image and training configs
IMG_HEIGHT = 128
IMG_WIDTH = 128
BATCH_SIZE = 32
EPOCHS = 20
