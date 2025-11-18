from ultralytics import YOLO
import cv2
import os
import numpy as np

model = YOLO("best.pt")
# print(model.names)

def process_image(file_path):
    results = model.predict(file_path, verbose=False)[0]
    img = cv2.imread(file_path)
    if img is None:
        raise FileNotFoundError(f"File {file_path} tidak ditemukan atau gagal dibaca.")

    alert = "success"

    for box in results.boxes:
        xyxy = box.xyxy.cpu().numpy().flatten()
        x1, y1, x2, y2 = map(int, xyxy)

        cls = int(box.cls)
        if cls in [6,7,8,9,10]:
            alert = "PPE Tidak Lengkap"

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f"{cls}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    os.makedirs("results", exist_ok=True)
    result_path = os.path.join("results", os.path.basename(file_path))
    success = cv2.imwrite(result_path, img)
    if not success:
        raise RuntimeError(f"Gagal menyimpan hasil di {result_path}")

    return result_path, alert
