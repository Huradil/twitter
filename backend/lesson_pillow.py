from PIL import Image,ImageDraw,ImageFont

file_path='media/jelly.png'

image = Image.open(file_path)

# # show image
# image.show()]

# # cut image
# cropped_image=image.crop((0,80,200,400))
# cropped_image.save('media/jelly_crop.png')

# поворот image
# rotated_image=image.rotate(90)
# rotated_image.save('media/rotated_jelly.png')

# img_draw=ImageDraw.Draw(image)
#
# text='This is codify property'
#
# font=ImageFont.truetype('arial.ttf',size=32)
#
# img_draw.text((10,10),text,font=font)
# image.save('media/jelly_watermark.png')

# # convert image to JPEG
# image=image.convert('RGB')
# image.save('media/jelly.jpg','JPEG')

# changed size
# image_resized = image.resize((400,400))
# image_resized.save('media/jelly_resized.png')

print(image.size)
width,height=image.size
new_height=300
new_width=int(width*new_height/height)
image_resized = image.resize(
    (new_width,new_height)
)
# image_resized.save('media/jelly_correct_resized.png')

image_resized_2=image.resize((400,int(height*400/width)))
image_resized_2.save('media/jelly_resized_2.png')




