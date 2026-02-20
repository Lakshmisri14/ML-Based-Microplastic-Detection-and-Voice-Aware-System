from tensorflow.keras.preprocessing.image import ImageDataGenerator
from config import TRAIN_DIR, TEST_DIR, IMG_HEIGHT, IMG_WIDTH, BATCH_SIZE

# --- Training data generator ---
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
train_gen = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='training'
)

print("=== Training Data ===")
print("Class indices:", train_gen.class_indices)
for imgs, labels in train_gen:
    print("First 10 labels in training batch:", labels[:10])
    break

# --- Validation data generator ---
val_gen = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='validation'
)

print("\n=== Validation Data ===")
print("Class indices:", val_gen.class_indices)
for imgs, labels in val_gen:
    print("First 10 labels in validation batch:", labels[:10])
    break

# --- Testing data generator ---
test_datagen = ImageDataGenerator(rescale=1./255)
test_gen = test_datagen.flow_from_directory(
    TEST_DIR,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='binary',
    shuffle=False
)

print("\n=== Testing Data ===")
print("Class indices:", test_gen.class_indices)
for imgs, labels in test_gen:
    print("First 10 labels in testing batch:", labels[:10])
    break

all_labels = []
for _, labels in test_gen:
    all_labels.extend(labels)
    if len(all_labels) >= test_gen.samples:
        break

print("Unique labels in test set:", set(all_labels))
