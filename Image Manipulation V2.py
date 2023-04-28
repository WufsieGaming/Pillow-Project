import os
from time import sleep
from PIL import Image, ImageFilter

# Create directories for modified picture files
os.makedirs('png_photos', exist_ok=True)  # png
os.makedirs('size200_img', exist_ok=True)  # new size
os.makedirs('size400_img', exist_ok=True)
os.makedirs('size600_img', exist_ok=True)
os.makedirs('rotated_img', exist_ok=True)  # rotated
os.makedirs('black_white_img', exist_ok=True)  # black and white
os.makedirs('blurred_img', exist_ok=True)  # blurred
os.makedirs('emboss_img', exist_ok=True)  # emboss

# Setting images into objects to call later
img1 = 'picture1.jpeg'
img2 = 'picture2.jpeg'
img3 = 'picture3.jpeg'
img4 = 'picture4.jpeg'
img5 = 'picture5.jpeg'
img6 = 'picture6.jpeg'
img7 = 'picture7.jpeg'
img8 = 'picture8.jpeg'
img9 = 'picture9.jpeg'
img10 = 'picture10.jpeg'

# Setting the sizes
size_200 = (200, 200)
size_400 = (400, 400)
size_600 = (600, 600)

# Function to transform JPEG to PNG
def transform(x):
    for f in os.listdir('.'):
        if f.endswith('.jpeg') and x == f:
            i = Image.open(f)
            fn, _ = os.path.splitext(f)
            i.save(f'png_photos/{fn}.png')
            i.show()

# Function to change size
def size(x, choice2):
    for f in os.listdir('.'):
        if f.endswith('.jpeg') and x == f:
            i = Image.open(f)
            fn, fext = os.path.splitext(f)
            if choice2 == "200":
                i.thumbnail(size_200)
                i.save(f'size200_img/{fn}_200{fext}')
            elif choice2 == "400":
                i.thumbnail(size_400)
                i.save(f'size400_img/{fn}_400{fext}')
            elif choice2 == "600":
                i.thumbnail(size_600)
                i.save(f'size600_img/{fn}_600{fext}')
            i.show()

# Function to rotate picture
def rotate(x):
    for f in os.listdir('.'):
        if f.endswith('.jpeg') and x == f:
            i = Image.open(f)
            fn, fext = os.path.splitext(f)
            y = int(input("Please type in desired length to rotate: "))
            i.rotate(y).save(f'rotated_img/{fn}_rotated{fext}')
            i.show()

# Function to convert to black and white
def color(x):
    for f in os.listdir('.'):
        if f.endswith('.jpeg') and x == f:
            i = Image.open(f)
            fn, fext = os.path.splitext(f)
            i.convert(mode='L').save(f'black_white_img/{fn}_black_and_white{fext}')

# Function to blur the image
def blur(x):
    for f in os.listdir('.'):
        if f.endswith('.jpeg') and x == f:
            i = Image.open(f)
            b = int(input("Enter the amount of blur you want: "))
            fn, fext = os.path.splitext(f)
            i.filter(ImageFilter.GaussianBlur(b)).save(f'blurred_img/{fn}_blurred{fext}')
# Function to apply emboss filter
def emboss(x):
    for f in os.listdir('.'):
        if f.endswith('.jpeg') and x == f:
            i = Image.open(f)
            fn, fext = os.path.splitext(f)
            i.filter(ImageFilter.EMBOSS()).save(f'emboss_img/{fn}_emboss{fext}')

# Function to empty and delete directories
def empty():
    # Empties and deletes png folder
    for f in os.listdir('png_photos'):
        os.remove(os.path.join('png_photos', f))
    os.removedirs('png_photos')

    # Empties and deletes size folders
    for folder in ['size200_img', 'size400_img', 'size600_img']:
        for f in os.listdir(folder):
            os.remove(os.path.join(folder, f))
        os.removedirs(folder)

    # Empties and deletes rotated images folder
    for f in os.listdir('rotated_img'):
        os.remove(os.path.join('rotated_img', f))
    os.removedirs('rotated_img')

    # Empties black and white folder
    for f in os.listdir('black_white_img'):
        os.remove(os.path.join('black_white_img', f))
    os.removedirs('black_white_img')

    # Empties blurred folder
    for f in os.listdir('blurred_img'):
        os.remove(os.path.join('blurred_img', f))
    os.removedirs('blurred_img')

    # Empties emboss folder
    for f in os.listdir('emboss_img'):
        os.remove(os.path.join('emboss_img', f))
    os.removedirs('emboss_img')


while True:
    choice = input("""
Welcome to my photo library! Here are 10 random pictures of cute dogs. Feel free to explore and make edits to them.
Pick a number between 1 and 10 to select a photo, or enter 'quit' to exit.
""")

    if choice.isdigit() and 1 <= int(choice) <= 10:
        img_choice = globals()['img' + choice]

        choice1 = input("First things first, would you like to save the image as a PNG instead of JPEG? (yes/no): ")
        if choice1.lower() == "yes":
            transform(img_choice)

        choice2 = input("You can also change the size of the thumbnail for this picture. Enter 200, 400, 600, or 'no': ")
        if choice2 != "no":
            size(img_choice, choice2)

        choice3 = input("Would you like to rotate the picture? (yes/no): ")
        if choice3.lower() == "yes":
            rotate(img_choice)

        choice4 = input("Now, would you like to convert the picture to black and white? (yes/no): ")
        if choice4.lower() == "yes":
            color(img_choice)

        choice5 = input("Would you like to apply a blur effect to the picture? (yes/no): ")
        if choice5.lower() == "yes":
            blur(img_choice)

        choice6 = input("Do you want to add the emboss filter to the image? (yes/no): ")
        if choice6.lower() == "yes":
            emboss(img_choice)

        final = input("Would you like to quit? (yes/no): ")
        if final.lower() == "yes":
            sleep(0.5)
            empty()
            break
    elif choice.lower() == "quit":
        print("See you another time!")
        sleep(0.5)
        empty()
        break