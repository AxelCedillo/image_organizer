from pathlib import Path
actual_dir = Path('.')

arc = actual_dir /'images_test'/'image_01.jpeg'
new_direc = actual_dir / 'images_exit' / ''

print(new_direc.resolve())