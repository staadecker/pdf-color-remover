# PDF colour remover

This short script will generate a copy of a given PDF with all the colour removed (replaced by white pixels instead).

The script was created as a way to erase the solutions from past university exam.
This allows me to practice writing the exam without seeing the solutions.
This only works if the solutions are in colour and the exam questions are not.

## Usage

Pre-requisites: Python 3.

1. In terminal clone the repository to your computer. 

    `git clone https://github.com/staadecker/pdf-colour-remover.git`

2. Navigate to the folder. 

    `cd pdf-colour-remover`

3. Install the required dependencies. 

    `pip install -r requirements.txt`

4. Copy the PDF you'd like to process to the current directory.

5. Run the script with the file name as the argument.

    `python script.py my_document_to_convert.pdf`

6. `processed_my_document_to_convert.pdf` will be generated in the current directory.

## Notes

- Internally, the script converts your PDF to an image. This means that in the generated PDF, you won't be able to copy text or work with PDF elements. After the script runs it's all just one image!

- If you find that the script is filtering out too much or too little content you can edit `STD_CUTOFF` in `script.py`.
The smaller the value the more content is filtered out. See code comments for further details.

- The script adds a blank page at the start of your document. If this bothers you, feel free to remove the blank page with one of the many online editors.