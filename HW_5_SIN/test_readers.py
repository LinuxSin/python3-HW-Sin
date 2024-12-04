# #import sys - задание 1
# import argparse
# 
# from utils.reader import image_reader as imread
# from utils.reader import csv_reader, bin_reader, txt_reader, json_reader
# from utils.processor import histogram
# from utils.writer import csv_writer, bin_writer, txt_writer, image_writer, json_writer
# 
# from utils.image_toner import stat_correction
# 
# 
# # def print_args_1():                   |
# #     print(type(sys.argv))             |
# #     if (len(sys.argv) > 1):           |
# #         for param in sys.argv[1:]:    | 1 задание
# #             print(param, type(param)) |
# #     return sys.argv[1:]               |
# 
# def init_parser():
#     parser = argparse.ArgumentParser()
#     parser.add_argument ('-img','--img_path', default ='', help='Path to image')
#     parser.add_argument ('-p','--path', default ='', help='Input file path ')
#     parser.add_argument('-t','--type', default='txt', help='Input file format ')
#     parser.add_argument('-o', '--output', help='Save file path')
# 
#     return parser
# 
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     parser = init_parser()
#     args = parser.parse_args() # убрал sys.argv[1:] - 1 задание
# 
#     #image = None| 1 задание
#     #hist = None |
# 
#     image = imread.read_data(args.img_path)
#     hist = histogram.image_processing(image)
#   
#     hist_template = None
# 
#     match args.type:
#         case 'img':
#             img2 = imread.read_data(args.path)
#             hist_template = histogram.image_processing(img2)
#         case 'csv':
#             hist_template = csv_reader.read_data(args.path)
#         case 'bin':
#             hist_template = bin_reader.read_data(args.path)
#         case 'txt':
#             hist_template = txt_reader.read_data(args.path)
#         case 'json':
#             hist_template = json_reader.read_data(args.path)
#         case _:
#             pass
# 
#     res_image = stat_correction.processing(hist_template, image)
#     image_writer.write_data(args.output, res_image)
# ------------------------------------------------------------------------------------


# import argparse
# import cv2  # Import OpenCV
# from utils.reader import image_reader as imread
# from utils.reader import csv_reader, bin_reader, txt_reader, json_reader
# from utils.processor import histogram
# from utils.writer import csv_writer, bin_writer, txt_writer, image_writer, json_writer
# 
# from utils.image_toner import stat_correction
# 
# def init_parser():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-img', '--img_path', default='', help='Path to image')
#     parser.add_argument('-p', '--path', default='', help='Input file path')
#     parser.add_argument('-t', '--type', default='txt', help='Input file format')
#     parser.add_argument('-o', '--output', help='Save file path')
#     parser.add_argument('--equalize', action='store_true', help='Apply histogram equalization')
# 
#     return parser
# 
# def equalize_histogram(image):
#     """Apply histogram equalization to the image."""
#     # Check if image is in color or grayscale
#     if len(image.shape) == 2:  # Grayscale image
#         return cv2.equalizeHist(image)
#     elif len(image.shape) == 3:  # Color image
#         # Convert image to YCrCb color space
#         ycrcb_img = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
#         # Equalize the histogram of the Y channel
#         ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])
#         # Convert back to BGR color space
#         return cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)
#     else:
#         raise ValueError("Unrecognized image format")
# 
# if __name__ == '__main__':
#     parser = init_parser()
#     args = parser.parse_args()
# 
#     image = imread.read_data(args.img_path)
# 
#     # Apply histogram equalization if specified
#     if args.equalize:
#         image = equalize_histogram(image)
# 
#     hist = histogram.image_processing(image)
# 
#     hist_template = None
# 
#     match args.type:
#         case 'img':
#             img2 = imread.read_data(args.path)
#             hist_template = histogram.image_processing(img2)
#         case 'csv':
#             hist_template = csv_reader.read_data(args.path)
#         case 'bin':
#             hist_template = bin_reader.read_data(args.path)
#         case 'txt':
#             hist_template = txt_reader.read_data(args.path)
#         case 'json':
#             hist_template = json_reader.read_data(args.path)
#         case _:
#             pass
# 
#     res_image = stat_correction.processing(hist_template, image)
#     image_writer.write_data(args.output, res_image)
# ---------------------------------------------------------------------------------------

# import argparse
# import cv2  # Import OpenCV
# import numpy as np  # Import numpy
# from utils.reader import image_reader as imread
# from utils.reader import csv_reader, bin_reader, txt_reader, json_reader
# from utils.processor import histogram
# from utils.writer import csv_writer, bin_writer, txt_writer, image_writer, json_writer
# 
# from utils.image_toner import stat_correction
# 
# def init_parser():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-img', '--img_path', default='', help='Path to image')
#     parser.add_argument('-p', '--path', default='', help='Input file path')
#     parser.add_argument('-t', '--type', default='txt', help='Input file format')
#     parser.add_argument('-o', '--output', help='Save file path')
#     parser.add_argument('--equalize', action='store_true', help='Apply histogram equalization')
#     parser.add_argument('--gamma', type=float, default=1.0, help='Gamma correction value (1.0 means no correction)')
# 
#     return parser
# 
# def equalize_histogram(image):
#     """Apply histogram equalization to the image."""
#     if len(image.shape) == 2:  # Grayscale image
#         return cv2.equalizeHist(image)
#     elif len(image.shape) == 3:  # Color image
#         ycrcb_img = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
#         ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])
#         return cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)
#     else:
#         raise ValueError("Unrecognized image format")
# 
# def apply_gamma_correction(image, gamma):
#     """Apply gamma correction to an image."""
#     # Build a lookup table mapping the pixel values [0, 255] to their adjusted gamma values
#     invGamma = 1.0 / gamma
#     table = (255.0 * (np.arange(0, 256) / 255.0) ** invGamma).astype("uint8")
# 
#     # Apply gamma correction using the lookup table
#     return cv2.LUT(image, table)
# 
# if __name__ == '__main__':
#     parser = init_parser()
#     args = parser.parse_args()
# 
#     image = imread.read_data(args.img_path)
# 
#     # Apply histogram equalization if specified
#     if args.equalize:
#         image = equalize_histogram(image)
# 
#     # Apply gamma correction if a value is specified
#     if args.gamma != 1.0:
#         image = apply_gamma_correction(image, args.gamma)
# 
#     hist = histogram.image_processing(image)
# 
#     hist_template = None
# 
#     match args.type:
#         case 'img':
#             img2 = imread.read_data(args.path)
#             hist_template = histogram.image_processing(img2)
#         case 'csv':
#             hist_template = csv_reader.read_data(args.path)
#         case 'bin':
#             hist_template = bin_reader.read_data(args.path)
#         case 'txt':
#             hist_template = txt_reader.read_data(args.path)
#         case 'json':
#             hist_template = json_reader.read_data(args.path)
#         case _:
#             pass
# 
#     res_image = stat_correction.processing(hist_template, image)
#     image_writer.write_data(args.output, res_image)
# -------------------------------------------------------------------------------------------------------------

import argparse
import cv2  
import numpy as np  
from utils.reader import image_reader as imread
from utils.reader import csv_reader, bin_reader, txt_reader, json_reader
from utils.processor import histogram
from utils.writer import csv_writer, bin_writer, txt_writer, image_writer, json_writer
from utils.image_toner import stat_correction

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-img', '--img_path', default='', help='Path to image')
    parser.add_argument('-p', '--path', default='', help='Input file path')
    parser.add_argument('-t', '--type', default='txt', help='Input file format')
    parser.add_argument('-o', '--output', help='Save file path')
    parser.add_argument('--equalize', action='store_true', help='Apply histogram equalization')
    parser.add_argument('--gamma', type=float, default=1.0, help='Gamma correction value (1.0 means no correction)')
    parser.add_argument('--mode', type=str, choices=['histogram', 'transform'], default='transform', 
                        help='Mode of operation: histogram for histogram calculation, transform for image transformation')

    return parser

def equalize_histogram(image):
   
    if len(image.shape) == 2:  
        return cv2.equalizeHist(image)
    elif len(image.shape) == 3:  
        ycrcb_img = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
        ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])
        return cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)
    else:
        raise ValueError("Unrecognized image format")

def apply_gamma_correction(image, gamma):
    invGamma = 1.0 / gamma
    table = (255.0 * (np.arange(0, 256) / 255.0) ** invGamma).astype("uint8")
    return cv2.LUT(image, table)

if __name__ == '__main__':
    parser = init_parser()
    args = parser.parse_args()

    if args.mode == 'histogram':    
        image = imread.read_data(args.img_path)
        hist = histogram.image_processing(image)      
        json_writer.write_data(args.output, hist)
    elif args.mode == 'transform':
        image = imread.read_data(args.img_path)   
        if args.equalize:
            image = equalize_histogram(image)     
        if args.gamma != 1.0:
            image = apply_gamma_correction(image, args.gamma)
        hist = histogram.image_processing(image)
        hist_template = None
        match args.type:
            case 'img':
                img2 = imread.read_data(args.path)
                hist_template = histogram.image_processing(img2)
            case 'csv':
                hist_template = csv_reader.read_data(args.path)
            case 'bin':
                hist_template = bin_reader.read_data(args.path)
            case 'txt':
                hist_template = txt_reader.read_data(args.path)
            case 'json':
                hist_template = json_reader.read_data(args.path)
            case _:
                pass
        res_image = stat_correction.processing(hist_template, image)
        image_writer.write_data(args.output, res_image)
