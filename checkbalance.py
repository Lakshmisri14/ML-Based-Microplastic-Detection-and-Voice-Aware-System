import os
TRAIN_DIR1 = "C:/Users/Lakshmi Sri M/OneDrive/Desktop/MP1/data/train/1_Training/1_Training"
TEST_DIR1 = "C:/Users/Lakshmi Sri M/OneDrive/Desktop/MP1/data/train/3_Testing/3_Testing"


train_dir1 = TRAIN_DIR1

for cls in os.listdir(train_dir1):
    path = os.path.join(train_dir1, cls)
    if os.path.isdir(path):
        print(cls, len(os.listdir(path)))
