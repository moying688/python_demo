# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

# 生成彩色字符画
def CharPic(text):  # 输入参数为text文字
    font_size = 20  # 字体大小
    img_path = "QQ图片20230506202431.jpg"  # 图片路径
    font_path = 'C:/Windows/Fonts/simhei.ttf'  # 黑体字体路径,windows电脑可以在C:\Windows\Fonts里找到
    # PIL.ImageFont.truetype(font=None, size=10, index=0, encoding=”) 返回一个字体对象
    font = ImageFont.truetype(font_path, font_size)

    img = Image.open(img_path)
    w, h = img.size
    new_img = Image.new("RGBA", (w, h))

    num = 0
    for i in range(0, h, font_size):
        for j in range(0, w, font_size):
            r,g,b= img.getpixel((j, i))
            # print(r,g,b)
            draw = ImageDraw.Draw(new_img)
            draw.text((j, i), text[num % len(text)], fill=(r, g, b), font=font)
            num += 1
    new_img.show()  # 显示图片
    new_img.save(text+'西瓜song.png') # 保存为'.jpg'文件打不开


if __name__ == "__main__":
    CharPic("宋")  #字体控制
