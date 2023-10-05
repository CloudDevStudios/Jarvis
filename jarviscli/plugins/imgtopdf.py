import img2pdf
from PIL import Image
import os
from plugin import plugin
from colorama import Fore


@plugin('image to pdf')
class ImageToPDF:
    """
    A tool to converrt images to pdf file
    """

    def __init__(self):
        # Path of the folder or image to be converted
        self.path = None
        self.image = None

    def __call__(self, jarvis, s):
        self.imgtopdf(jarvis)

    def imgtopdf(self, jarvis):
        jarvis.say('')
        jarvis.say('This tool will help you convert image to pdf')
        while True:

            self.available_options(jarvis)
            user_input = jarvis.input('Your choice: ')
            user_input = user_input.lower()

            if user_input in ['q', 'quit', '3']:
                jarvis.say("See you next time :D", Fore.CYAN)
                break

            elif user_input == '1':
                while True:
                    image_path = jarvis.input(
                        'Enter the full path of the image: ')
                    if os.path.exists(image_path) and (image_path.endswith('.jpg') or image_path.endswith('.png')):
                        break
                    else:
                        jarvis.say(
                            'Opps! Looks like you entered an invalid path. Kindly Re-enter', Fore.RED)
                pdf_bytes = self.single_image_to_pdf(jarvis, image_path)

            elif user_input == '2':
                while True:
                    folder_path = jarvis.input(
                        'Enter the full path of the folder: ')
                    if os.path.exists(folder_path):
                        break
                    else:
                        jarvis.say(
                            'Opps! Looks like you entered an invalid path. Kindly Re-enter', Fore.RED)
                pdf_bytes = self.folder_to_pdf(jarvis, folder_path)

            else:
                jarvis.incorrect_option()
                continue

            destination = jarvis.get_saving_directory(self.path)
            # Naming and saving the pdf file
            file_name = jarvis.input('What would you like to name your pdf? ')
            pdf_destination = f'{destination}/{file_name}.pdf'
            print(f'Final Destination {pdf_destination}')
            self.save_pdf(jarvis, pdf_bytes, pdf_destination)

    def available_options(self, jarvis):
        """
        Message displayed to prompt the user about converting
        images to pdf
        """
        jarvis.say('Select one of the following options:')
        jarvis.say('1: Convert a single image')
        jarvis.say('2: Convert all images of the folder')
        jarvis.say('3: Quit')

    def single_image_to_pdf(self, jarvis, image_path):
        """
        This function is used to convert a single image
        with a given path to a pdf file.
        """
        self.path = image_path
        self.image = Image.open(image_path)
        pdf_bytes = img2pdf.convert(self.image.filename)
        self.image.close()
        return pdf_bytes

    def folder_to_pdf(self, jarvis, folder_path):
        """
        This function is used to convert all the images
        in a given folder path to a single PDF file
        """
        self.path = folder_path
        os.chdir(self.path)
        source_images = [
            image
            for image in os.listdir(os.getcwd())
            if image.endswith('.jpg') or image.endswith('.png')
        ]
        return img2pdf.convert(source_images)

    def save_pdf(self, jarvis, pdf_bytes, destination):
        """
        Save the pdf to the thus supplied location
        or prompt the user to choose a new location
        """
        with open(destination, 'wb') as pdf_file:
            pdf_file.write(pdf_bytes)
        jarvis.say('Your pdf is created successfully', Fore.GREEN)
