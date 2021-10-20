import pdf2image
import fpdf
import sys, os, tempfile
import numpy as np
from PIL import Image

# Represents the maximum allowed standard deviation in the R, G, & B values.
# The greater the standard deviation the further the pixel is from grey.
STD_CUTOFF = 5

filename = sys.argv[1]
(path, tail) = os.path.split(filename)
output_filename = os.path.join(path, "processed_" + tail)

print("Loading pdf...")
pages = pdf2image.convert_from_path(filename)

# Create an output pdf
output_pdf = fpdf.FPDF(unit="cm", format="letter")

# Constants
LETTER_PAGE_WIDTH = 21.6 * 0.95  # Reduce by 95% since for some reason there's a margin
BLACK = np.array([0, 0, 0])
WHITE = np.array([255, 255, 255])


def erase_colour(image):
    img_data = np.array(image, np.uint8)

    # Find all indexes for where the standard deviation of the RGB is greater than STD_CUTOFF
    # This indicates that the color is not close to grey
    i, j = np.where(np.std(img_data, -1) > STD_CUTOFF)
    # For all pixels where the color is not close to grey, replace with white
    img_data[i, j] = WHITE

    return Image.fromarray(img_data)


# Create temporary directory
tempdir = tempfile.TemporaryDirectory()

output_pdf.add_page()  # Must add a blank page for some reason

n = len(pages)

# For each page, convert, save and then write to PDF
for i, page in enumerate(pages):
    print("Processing page %d of %d..." % (i, n))

    temp_file_name = os.path.join(tempdir.name,
                                  "temp" + str(i) + ".jpeg")  # Use a different file each time to avoid issues

    processed_image = erase_colour(page)
    processed_image.save(temp_file_name, format='JPEG')

    output_pdf.image(temp_file_name, w=LETTER_PAGE_WIDTH, x=0, type="JPEG")

print(f"Saving file to {output_filename}...")
output_pdf.output(output_filename)
