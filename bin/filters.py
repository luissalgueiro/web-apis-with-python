from PIL import Image, ImageFilter
import io

def apply_filter(file: object, filter: str) -> object:
    """
    ToDo:
      1. accept image file and filter operation
      2. Open the image with PIL, 
      3. Apply filter 
      4. Convert the PIL image object into a file object
      5. return the file object
    """
    image = Image.open(file)
    image = image.filter(eval(f"ImageFilter.{filter.upper()}"))
    file = io.BytesIO()
    image.save(file,'JPEG')
    file.seek(0)
    
    return file
    