# PDF color remover

This short script will generate a copy of a given PDF with all the color removed (replaced by white pixels instead).
It was created as a way to remove the the colored solutions from past exams such that I could practice without seeing the solutions.

## Usage

Pre-requisites: Python 3.

1. Clone the repository to your computer. 

    `git clone https://github.com/staadecker/pdf-colour-remover.git`

2. Navigate to the folder. 

    `cd pdf-colour-remover`

3. Install the required dependencies. 

    `pip install -r requirements.txt`

4. Copy the PDF you'd like to process to the current folder.

5. Run the script.

    `python script.py <my-pdf-to-convert.pdf> <generated-document.pdf>`

## Notes

- Internally, the script converts your PDF to an image. This means that in the generated PDF, you won't be able to copy text or work with PDF elements. After the script runs it's all just one image!
 