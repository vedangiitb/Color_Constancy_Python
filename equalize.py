import cv2
import sys
from skimage.exposure import match_histograms


def equalize_v_channel(input_image_path, output_image_path):
    # Read image (OpenCV reads in BGR)
    img = cv2.imread(input_image_path)

    if img is None:
        print("Error: Unable to read the image.")
        return

    # Convert to HSV (Hue Saturation Value)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Equalize channel V
    img_hsv[:,:,2] = cv2.equalizeHist(img_hsv[:,:,2])

    # Convert to RGB
    equ_out = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)

    # Save the equalized image
    cv2.imwrite(output_image_path, equ_out)
    print(f"Equalized image saved as {output_image_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py input_image output_image")
    else:
        input_image_path = sys.argv[1]
        ref_img_path = sys.argv[2]
        output_image_path = sys.argv[3]
        original_img = cv2.imread(input_image_path)
        reference_img = cv2.imread(ref_img_path)

        matched = match_histograms(original_img, reference_img, channel_axis = 1)

        cv2.imwrite(output_image_path,matched)
