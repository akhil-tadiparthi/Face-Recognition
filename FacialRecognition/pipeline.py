import os

print("Creating Datset...")
os.system("python 01_create_dataset.py")
print("Dataset Created")

print("Training Model...")
os.system("python 02_train_model.py")
print("Model Trained")

print("Starting Recognition...")
os.system("python 03_live_recognition.py")

