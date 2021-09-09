from PIL import Image


def image_resizer(width,height,image_name):
    '''width: It is parameter  of width, how much height you want to define it.
       height: It is parameter of height, how much height you want to define it.
       image_name: In you have to put the image name with format and location in it where the image is located in your pc 
    '''
    image = Image.open(image_name)
    image = image.resize((width,height))
    image.save('image_resized.png')
    return "Image is resized with name: 'image_resized.png"


#i will call the function image_resizer
print(image_resizer(600,700,'D:github\\image.png'))