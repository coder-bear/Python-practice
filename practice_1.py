from PIL import Image, ImageDraw, ImageFont
font = ImageFont.truetype('Dengb.ttf', 50) #读取相应字体和设置字体大小
image_1 = Image.open("D:\\new folder\\tiny_wechat\\static\\images\\123.jpg")
draw = ImageDraw.Draw(image_1) #读取一个图片
draw.text((574, 62), '4', fill=(255,0,0), font=font) #像素位置，文本内容，填充颜色，所用字体
image_1.show()
