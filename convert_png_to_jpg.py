import pathlib

from PIL import Image

root_dir = pathlib.Path(".")
for f_name in root_dir.rglob("*.png"):
	img = Image.open(str(f_name))
	#img = img.convert("RGB")
	img.save(str(f_name.with_suffix(".2.png")), optimize=True)
	print(f_name)