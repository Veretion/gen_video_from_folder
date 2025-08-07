import cv2
import os
import re


frames_folder = "folder"  # Путь к папке с кадрами
output_video_path = "name_output_video.mp4"  # Название видео
fps = 30  # Количество кадров в секунду


# Получаем список всех файлов в папке с кадрами
frame_files = os.listdir(frames_folder)

# Функция для извлечения числа из имени файла
def extract_number(filename):
    match = re.search(r'_\d+', filename)  # Ищем подстроку вида '_<число>'
    if match:
        return int(match.group()[1:])  # Возвращаем число без символа '_'
    return 0

# Сортируем файлы по числовому значению
frame_files = sorted(frame_files, key=extract_number)

# Проверяем, что папка не пуста
if not frame_files:
    print("Папка с кадрами пуста!")
    exit()

# Загружаем первый кадр для определения размера
first_frame = cv2.imread(os.path.join(frames_folder, frame_files[0]))
height, width, layers = first_frame.shape

# Определяем параметры видео
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Кодек для MP4

# Создаем объект VideoWriter
video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# Проходим по всем кадрам и добавляем их в видео
for frame_file in frame_files:
    frame_path = os.path.join(frames_folder, frame_file)
    frame = cv2.imread(frame_path)
    video_writer.write(frame)

# Закрываем видео
video_writer.release()

print(f"Видео успешно создано: {output_video_path}")
