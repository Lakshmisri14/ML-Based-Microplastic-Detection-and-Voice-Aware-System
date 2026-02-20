from config import TRAIN_DIR, TEST_DIR, IMG_HEIGHT, IMG_WIDTH, BATCH_SIZE, EPOCHS, MODEL_SAVE_PATH
from model import build_cnn
from utils import get_data_generators, plot_history

def train():
    train_gen, val_gen, _ = get_data_generators(TRAIN_DIR, TEST_DIR, IMG_HEIGHT, IMG_WIDTH, BATCH_SIZE)
    model = build_cnn(input_shape=(IMG_HEIGHT, IMG_WIDTH, 3))
    history = model.fit(train_gen, epochs=EPOCHS, validation_data=val_gen)
    model.save(MODEL_SAVE_PATH)
    print(f"Model saved at {MODEL_SAVE_PATH}")
    plot_history(history)


if __name__ == "__main__":
    train()
