# photo.py
# Name: James Speed and John Cannon
# email: speedjp@mail.uc.edu and cannonjp@mail.uc.edu
# Assignment Title: Fulcher Final
# Due Date: 12/7/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates that we can use Eclipse to create a PyDev project that executes all the desired functions and code.
# Citations: CHATGPT and Stack Overflow
# Anything else that's relevant: We really do not like SAND!

from PIL import Image, ImageShow, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def load_and_display_image(image_path):
    
    '''
    author: Jack Cannon
    purpose: loads image, flips it from being mirrored, and displays it
    '''
    
    try:
        myimage = Image.open(image_path)

      
        flipped_image = myimage.transpose(Image.Transpose.ROTATE_180)

       
        flipped_image.save("flipped_image.jpg", format="JPEG")

        
        ImageShow.show(flipped_image)

    except Exception as e:
        print(f"Error loading and displaying the image: {e}")
        return None



