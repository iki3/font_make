import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import glob
import os

# 使うフォント，サイズ，描くテキストの設定

fontsize = 64


# 画像サイズ，背景色，フォントの色を設定
canvasSize    = (64, 64)
backgroundRGB = (255, 255, 255)
textRGB       = (0, 0, 0)

# 文字を描く画像の作成
print(os.path.exists('C:/Windows'))
font_list=[os.path.basename(p) for p in glob.glob('C:/Windows/Fonts/**/*.ttf', recursive=True) if os.path.isfile(p)]
print(len(font_list))
input()


im=PIL.Image.open('iro.jpg')
im_resize=im.resize((64,64))
im_resize.save('iro_resize.jpg')
# im_resize=im_resize.convert('RGB')
# im2=Image.new('RGBA',(64,64))

print(im.size)
print(type(im.size))
input()



for i in font_list:

    #os.mkdir('{dir}'.format(dir=i))
    ttfontname = 'C:/Windows/Fonts/**/{}'.format(i)
    print(ttfontname)
    ttfontname="C:/Windows/Fonts/meiryob.ttc"
    for j in range(26):
        text = chr(12354 + j)
        print(type(text))
        print(len(text))
        print(text)
        #print(text[1])
    
        img = PIL.Image.new('RGB', canvasSize, backgroundRGB)



        draw = PIL.ImageDraw.Draw(img)
        # 用意した画像に文字列を描く
        font = PIL.ImageFont.truetype(ttfontname, fontsize)
        textWidth, textHeight = draw.textsize(text, font=font)
        # print(canvasSize[1], textWidth)
        # print(canvasSize[1] // 2 - textHeight // 2)

        textTopLeft = (canvasSize[0] // 2 - textWidth // 2, canvasSize[1]//2-textHeight//2)  # 前から1/6，上下中央に配置
        draw.text(textTopLeft, text, fill=textRGB, font=font)

        for x in range(64):
            for y in range(64):
                ima=img.getpixel((x,y))
                #print(sum(ima))
                if(sum(ima)!=255*3):
                    r,g,b=im_resize.getpixel((x,y))
                    img.putpixel((x,y),(r,g,b,0))



        img.save("image{num}.png".format(dir=i,num=j))

    break
#
# for i in range(60):
#     text=chr(65+i)
#     img  = PIL.Image.new('RGB', canvasSize, backgroundRGB)
#     draw = PIL.ImageDraw.Draw(img)
#
#     # 用意した画像に文字列を描く
#     font = PIL.ImageFont.truetype(ttfontname, fontsize)
#     textWidth, textHeight = draw.textsize(text,font=font)
#     print(canvasSize[1],textWidth)
#     print(canvasSize[1]//2-textHeight//2)
#
#     textTopLeft = (canvasSize[0]//2-textWidth//2, 0) # 前から1/6，上下中央に配置
#     draw.text(textTopLeft, text, fill=textRGB, font=font)
#
#     img.save("image{}.png".format(i))
#
# print([os.path.basename(p) for p in glob.glob('/usr/share/fonts/truetype/**/*.ttf', recursive=True) if os.path.isfile(p)])
