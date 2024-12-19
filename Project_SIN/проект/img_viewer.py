import PySimpleGUI as sg
import cv2
import numpy as np
import os
from datetime import datetime

def add_noise(image, noise_level):
    row, col, ch = image.shape
    mean = 0
    stddev = noise_level
    gauss = np.random.normal(mean, stddev, (row, col, ch))
    noisy_image = image + gauss
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image

def apply_hist_equalization(image):
    ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    ycrcb_image[:, :, 0] = cv2.equalizeHist(ycrcb_image[:, :, 0])
    equalized_image = cv2.cvtColor(ycrcb_image, cv2.COLOR_YCrCb2BGR)
    return equalized_image

def apply_color_correction(image):
    lab_frame = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab_frame)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    corrected_image = cv2.merge((cl, a, b))
    corrected_image = cv2.cvtColor(corrected_image, cv2.COLOR_LAB2BGR)
    return corrected_image

def rotate_image(image, angle):
    center = (image.shape[1] // 2, image.shape[0] // 2)
    rot_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rot_matrix, (image.shape[1], image.shape[0]))
    return rotated_image

def rescale_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    rescaled_image = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)
    return rescaled_image

def main():
    sg.theme("Dark")
    sg.theme_button_color(('white', '#1E90FF'))

    # Определяем макет интерфейса
    layout = [
        [sg.Text("Редактор", size=(60, 1), justification="center", font=("Helvetica", 16), expand_x=True)],
        [sg.Image(filename="", key="-IMAGE-", expand_x=True, expand_y=True)],
        [sg.Radio("None", "Radio", True, size=(15, 1))],
        [sg.Radio("Шум", "Radio", size=(15, 1), key="-NOISE-"), sg.Slider((0, 100), 0, 1, orientation="h", size=(40, 15), key="-NOISE SLIDER-", expand_x=True)],
        [sg.Radio("Эквализация", "Radio", size=(15, 1), key="-HIST EQUAL-")
         
        ],
        [
            sg.Radio("Цветокоррекция", "Radio", size=(15, 1), key="-COLOR CORR-")
        ],
        [sg.Radio("Поворот", "Radio", size=(15, 1), key="-ROTATE-"), sg.Slider((-180, 180), 0, 1, orientation="h", size=(40, 15), key="-ROTATE SLIDER-", expand_x=True)],
        [sg.Radio("Масштаб", "Radio", size=(15, 1), key="-RESCALE-"), sg.Slider((10, 200), 100, 1, orientation="h", size=(40, 15), key="-RESCALE SLIDER-", expand_x=True)],
        [sg.Button("Choose Image"), sg.Button("Save Image"), sg.Button("Exit", size=(10, 1))]
    ]

    # Создаем окно
    window = sg.Window("OpenCV Image Processing", layout, location=(800, 400), size=(1200, 900), resizable=True)

    image_path = None
    frame = None

    while True:
        event, values = window.read(timeout=20)

        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "Choose Image":
            image_path = sg.popup_get_file("Choose an image file", file_types=(("Image Files", "*.png *.jpg *.jpeg"),))
            if image_path:
                frame = cv2.imread(image_path)
                frame = cv2.resize(frame, (200, 200), interpolation=cv2.INTER_LINEAR)
                imgbytes = cv2.imencode(".jpg", frame)[1].tobytes()
                window["-IMAGE-"].update(data=imgbytes)

        if image_path and frame is not None:
            original_frame = cv2.imread(image_path)
            frame = cv2.resize(original_frame, (200, 200), interpolation=cv2.INTER_LINEAR)

            if values["-NOISE-"]:
                noise_level = values["-NOISE SLIDER-"]
                frame = add_noise(frame, noise_level)
            elif values["-HIST EQUAL-"]:
                frame = apply_hist_equalization(frame)
            elif values["-COLOR CORR-"]:
                frame = apply_color_correction(frame)
            elif values["-ROTATE-"]:
                angle = values["-ROTATE SLIDER-"]
                frame = rotate_image(frame, angle)
            elif values["-RESCALE-"]:
                scale_percent = values["-RESCALE SLIDER-"]
                frame = rescale_image(frame, scale_percent)

            success, imgbytes = cv2.imencode(".png", frame)
            if success:
                window["-IMAGE-"].update(data=imgbytes.tobytes())

        if event == "Save Image" and frame is not None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            default_filename = f"edited_image_{timestamp}.png"
            save_path = sg.popup_get_file(
                'Save Image', save_as=True, no_window=True, default_extension=".png",
                default_path=default_filename, file_types=(('PNG Files', '*.png'), ('JPEG Files', '*.jpg'), ('All Files', '*.*'))
            )

            if save_path:
                cv2.imwrite(save_path, frame)

    window.close()


main()
