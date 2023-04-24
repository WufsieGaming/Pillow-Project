import os
from time import sleep
from PIL import Image, ImageFilter

#modified picture files
os.mkdir('png_photos')#png
os.mkdir('size200_img')#new size
os.mkdir('size400_img')
os.mkdir('size600_img')
os.mkdir('rotated_img')#rotated
os.mkdir('black_white_img')#black and white
os.mkdir('blurred_img')#blurred 
os.mkdir('emboss_img')#emboss

#setting images into objects to call later
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

#setting the sizes
size_200 = (200,200)
size_400 = (400,400)
size_600 = (600,600)

#jpeg to png function
def transform(x):
      for f in os.listdir('.'):
            if f.endswith('.jpeg'):
                  if x == f:
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)
                        i.save('png_photos/{}.png'.format(fn))
                        i.show()
#changing size funtion
def size(x):
      for f in os.listdir('.'):
            if f.endswith('.jpeg'):
                  if x == f:
                        if choice2 == "200":
                              i = Image.open(f)
                              fn, fext = os.path.splitext(f)
                              i.thumbnail(size_200)
                              i.save('size200_img/{}_200{}'.format(fn, fext))
                              i.show()
                        elif choice2 == "400":
                              i = Image.open(f)
                              fn, fext = os.path.splitext(f)
                              i.thumbnail(size_400)
                              i.save('size400_img/{}_400{}'.format(fn, fext))
                              i.show()
                        elif choice2 == "600":
                              i = Image.open(f)
                              fn, fext = os.path.splitext(f)
                              i.thumbnail(size_600)
                              i.save('size600_img/{}_600{}'.format(fn, fext))
                              i.show()
#rotating picture to users desired length                  
def rotate(x):
      for f in os.listdir('.'):
            if f.endswith('.jpeg'):
                  if x == f:
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)
                        y = int(input("Please type in desired length to rotate: "))
                        i.rotate(y).save('rotated_img/{}_rotated{}'.format(fn, fext))
                        i.show()
#black and white photo
def color(x):
      for f in os.listdir('.'):
            if f.endswith('.jpeg'):
                  if x == f:
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)
                        i.convert(mode='L').save('black_white_img/{}_black_and_white{}'.format(fn, fext))                                                   
#blurring the image
def blur(x):
      for f in os.listdir('.'):
            if f.endswith('.jpeg'):
                  if x == f:
                        i = Image.open(f)
                        b = int(input("Enter the amount of blur you want: "))
                        fn, fext = os.path.splitext(f)
                        i.filter(ImageFilter.GaussianBlur(b)).save('blurred_img/{}_blurred{}'.format(fn, fext))
#emboss filter
def emboss(x):
      for f in os.listdir('.'):
            if f.endswith('.jpeg'):
                  if x == f:
                        i = Image.open(f)  
                        fn, fext = os.path.splitext(f)              
                        i.filter(ImageFilter.EMBOSS()).save('emboss_img/{}_emboss{}'.format(fn, fext))

def empty():
      #empties and deletes png folder
            for f in os.listdir('png_photos'):
                  os.remove('png_photos/'+f)  
            os.removedirs('png_photos')  
            #empties and deletes size folders
            for f in os.listdir('size200_img'):
                  os.remove('size200_img/'+f)  
            os.removedirs('size200_img')    
            for f in os.listdir('size400_img'):
                  os.remove('size400_img/'+f)  
            os.removedirs('size400_img')     
            for f in os.listdir('size600_img'):
                  os.remove('size600_img/'+f)  
            os.removedirs('size600_img')
            #empties and deletes rotated images folder
            for f in os.listdir('rotated_img'):
                  os.remove('rotated_img/'+f)
            os.removedirs('rotated_img')
            #empties black and white folder
            for f in os.listdir('black_white_img'):
                  os.remove('black_white_img/'+f)
            os.removedirs('black_white_img')
            #empties blurred folder
            for f in os.listdir('blurred_img'):
                  os.remove('blurred_img/'+f)
            os.removedirs('blurred_img')
            #empties emboss folder
            for f in os.listdir('emboss_img'):
                  os.remove('emboss_img/'+f)
            os.removedirs('emboss_img')
                             
choice = input("""
      Welcome to my photo library! In here there are 10 random pictures of cute dogs! Feel free to look at them, and if you want you can even do
      various edits to them. Enjoy!
      
      Type in a number between 1 to 10 to select a photo to open, or type in "quit" to exit. 
      """)

if choice.isdigit():
      if ("1" in choice) or ("2" in choice) or ("3" in choice) or ("4" in choice) or ("5" in choice) or ("6" in choice) or ("7" in choice) or ("8" in choice) or ("9" in choice) or ("10" in choice):
            choice1 = str(input("""
            First things first, would you like to save the image as a png instead of jpeg? \n
            Yes or no
            """))
            if choice1 == "yes":
                  transform(locals()["img" + choice])
            
            choice2 = str(input("""
            You can also change the size of the thumbnail for this picture! to change it to 200 type in "200", for 400 type "400",
            for 600 enter "600", or if you don't want to change the size simply enter in "no"
            """))
            if choice2 != "no":
                  size(locals()["img" + choice])
      
            choice3 = str(input("""
            Guess what, you can even rotate the picture! Would you like to rotate the picture?
            If yes just enter in yes, if no then simply enter no.
             """))     
            if choice3 == "yes":
                 rotate(locals()["img" + choice])
            
            choice4 = str(input("""
            Now, would you like to switch the picture to black and white? yes or no: 
            """))
            if choice4 == "yes":
                  color(locals()["img" + choice])
            
            choice5 = str(input("""
            You would never believe it... Another edit that you can do! This time you can choose if you want to blur
            the picture or not. So, do you want to blur it? yes or no: 
            """))
            if choice5 == "yes":
                  blur(locals()["img" + choice])
            
            choice6 = str(input("""
            Do you want to add the emboss filter to the image? yes or no: 
            """))
            if choice6 == "yes":
                  emboss(locals()["img" + choice])
            
      final = input("""
      Would you like to quit?
              """)

      if final == "yes":
            sleep(0.5)
            #empties and deletes png folder
            for f in os.listdir('png_photos'):
                  os.remove('png_photos/'+f)  
            os.removedirs('png_photos')  
            #empties and deletes size folders
            for f in os.listdir('size200_img'):
                  os.remove('size200_img/'+f)  
            os.removedirs('size200_img')    
            for f in os.listdir('size400_img'):
                  os.remove('size400_img/'+f)  
            os.removedirs('size400_img')     
            for f in os.listdir('size600_img'):
                  os.remove('size600_img/'+f)  
            os.removedirs('size600_img')
            #empties and deletes rotated images folder
            for f in os.listdir('rotated_img'):
                  os.remove('rotated_img/'+f)
            os.removedirs('rotated_img')
            #empties black and white folder
            for f in os.listdir('black_white_img'):
                  os.remove('black_white_img/'+f)
            os.removedirs('black_white_img')
            #empties blurred folder
            for f in os.listdir('blurred_img'):
                  os.remove('blurred_img/'+f)
            os.removedirs('blurred_img')
            #empties emboss folder
            for f in os.listdir('emboss_img'):
                  os.remove('emboss_img/'+f)
            os.removedirs('emboss_img')
            quit()
      
      elif final == "no":
            choice = input("Choose a new number between 1-10: ")
      
      else: 
            print("Sorry that isn't a number corresponding to a picture, please select a number between 1-10")
            choice = input()

elif choice == "quit":
      print("See you another time!")
      sleep(0.5)
      empty
      quit()
      
else:
      print("Sorry, that doesn't seem to be one of the choices for a picture! Please input a valid number, it has to be between 1-10.")
            
