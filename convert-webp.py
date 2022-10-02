import os
import time
from PIL import Image

print('\n========================================')
print('Develope by jeffersonespinoza.com \n')
print('30 sep 2022')
print('==========================================\n')

folder = 'images'

star = time.time()

## Convert png to webp
## Does not save transparency
## Do not use with images that have transparent backgrounds 
## because it distorts the image.

## Todo:
## Create a folder with name images
## and put your image to converted here


# Find jpg files in folder
for root, dirs, files in os.walk(folder):
    for file in files:
        # Fin file with you extention 
        if file.endswith(( '.png' )):
            file = os.path.join(root, file)
            # Extention to convert
            newFile = file.replace( '.png', '.webp' )

            # Convert to webp
            im = Image.open(file).convert('RGB')
            im.save(newFile,'webp')

            ## Open file
            im = Image.open(file)
            width, heigth = im.size
            
            ## Resize you image
            ## Use of 1 - 6 for resize
            ## For use uncomment next line 

            ## Change quality image -> quality = (1/100)
            ## Reduce quality uncomment next line

            # im.save(newFile, quality =  60)

            print(im.size)
            print(newFile)  

# Find jpg files in folder
for root, dirs, files in os.walk(folder):
    for file in files:
        # Fin file with you extention 
        if file.endswith(( '.jpg' )):
            file = os.path.join(root, file)
            # Extention to convert
            newFile = file.replace( '.jpg', '.webp' )

            # Convert to webp
            im = Image.open(file).convert('RGB')
            im.save(newFile,'webp')

            ## Open file
            im = Image.open(newFile)
            width, height = im.size
            
            ## Resize you image
            ## Use of 1 - 6 for resize
            ## Uncomment next line 

            #im = im.resize((width//1, heigth//1))

            ## Change quality image -> quality = (1/100)
            ## For use uncomment next line

            # im.save(newFile, quality =  60)

            print(im.size)
            print(newFile)        


end = time.time()

print("\n  Work end ! time execution: ")
print(end-star)