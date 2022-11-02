from PIL import Image
from config import FORMAT_NAME, EXIT_EXTENSION, QUALITY_IMG

def img_compresser(filename_dir, newname, new_dir):
    image = Image.open(filename_dir)
    image = image.convert('RGB')
    print(f'{new_dir}{newname}{FORMAT_NAME}' + f'{EXIT_EXTENSION}')
    image.save(f'{new_dir}\{newname}{FORMAT_NAME}' + f'{EXIT_EXTENSION}', optimize = True, quality = QUALITY_IMG)
