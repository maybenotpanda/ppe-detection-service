from ultralytics import YOLO


model = YOLO("yolov8n.pt")

model.train(
    data="ppe_dataset.yaml",
    epochs=50,                # jumlah epoch
    imgsz=640,                # ukuran gambar
    batch=16,                 # batch size
    project="ppe_detection",  # folder output
    name="ppe_yolov8"         # nama folder project
)

print("Training selesai, model tersimpan")
