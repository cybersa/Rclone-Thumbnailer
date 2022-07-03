import cv2
import glob
import os
import imutils
from pathlib import Path


def thumbnail(file,save_path):
    
    try:
        Path(os.path.dirname(save_path)).mkdir(parents=True, exist_ok=True)  
        save_name=os.path.basename(file)
        print(file,save_path,save_name)

        if not file.startswith("http://"):
            original = cv2.imread(file)
        else:
            original = imutils.url_to_image(file)

        if original is None:
            print("Not able to read",file)
            return False

        height, width, channels = original.shape
        if height > width:
            im=imutils.resize(original,width=400)
        else:
            im=imutils.resize(original,width=600)

        cv2.imwrite(os.path.join(save_path,save_name), im) 
        return True
    except Exception as e:
        raise e