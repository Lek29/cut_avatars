from PIL import Image

image_path = 'images/merrilin.jpg'
path_save = 'images/avatar.jpeg'
image = Image.open(image_path)

red_channel, green_channel, blue_channel = image.split()

coordinates_left_cropped = (100, 0, image.width, image.height)
coordinates_middle_cropped = (50, 0, 1150, red_channel.height)
cropped_red_channel_left = red_channel.crop(coordinates_left_cropped)
cropped_red_channel_middle = red_channel.crop(coordinates_middle_cropped)
offset_red_channel = Image.blend(cropped_red_channel_left, cropped_red_channel_middle, 0.5) #смещенный красный канал

coordinates_rigth_cropped = (0, 0, 1100,  image.height)
coordinates_middle_cropped_blue = (50, 0, 1150, image.height)
cropped_blue_chanel_right = blue_channel.crop(coordinates_rigth_cropped)
cropped_blue_channel_middle = blue_channel.crop(coordinates_middle_cropped_blue)
offset_blue_channel = Image.blend(cropped_blue_chanel_right, cropped_blue_channel_middle, 0.5) #смещенный синий канал

coordinates_green_cropped = (50, 0, 1150, green_channel.height)
cropped_green_channel_middle = green_channel.crop(coordinates_green_cropped)

offset_finish_image = Image.merge('RGB', (offset_red_channel, cropped_green_channel_middle, offset_blue_channel))
offset_finish_image.save('images/finish_image.jpeg')
offset_finish_image.thumbnail((80, 80))
offset_finish_image.save(path_save)




