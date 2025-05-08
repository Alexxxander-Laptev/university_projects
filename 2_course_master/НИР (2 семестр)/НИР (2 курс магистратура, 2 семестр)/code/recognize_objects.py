from ultralytics import YOLO

# Загрузка модели
model = YOLO("yolov8m-seg.pt")  # Загрузка предобученной лёгкой модели
# Дообучение модель
model.train(
    data="../datasets/image_dataset/image_captcha.yaml",  # Путь к файлу конфигурации
    epochs=35,
    imgsz=640,
    batch=8,
    workers=4,
    device="cpu",
    name="captcha_seg"  # Название директории для сохранения результатов обучения
)
