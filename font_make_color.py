import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import glob
import os
import time
from pathlib import Path
import numpy as np
import itertools

path = Path(__file__).parent   # test.pyのあるディレクトリ
path /= '../font_datasets_color' #/name/A/train　穴抜き全部ある
                                       #A/test  穴抜き
                                       #B/train 全部ある
                                       #B/test 一個ずつある
print(path)
print(os.path.exists(path))


# 使うフォント，サイズ，描くテキストの設定

fontsize = 64


# 画像サイズ，背景色，フォントの色を設定
canvasSize    = (64, 64)
backgroundRGB = (255, 255, 255)
textRGB       = (0, 0, 0)

# 文字を描く画像の作成
font_list_kari=[os.path.basename(p) for p in glob.glob('../down_font_list/*.ttf', recursive=True) if os.path.isfile(p)]
print(font_list_kari)

print(len(font_list_kari))
katakana='アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン'
font_list=[]
con=0
for i in font_list_kari:

    con+=1
    if(con in [293,295,303,481]):
        pass
    else:

        print(con)
        print(i)
        ttfontname = '../down_font_list/{}'.format(i)

        text = chr(12451)
        text = katakana[0]
        text2=katakana[1]
        img = PIL.Image.new('RGB', canvasSize, backgroundRGB)
        img2=PIL.Image.new('RGB',canvasSize,backgroundRGB)

        draw = PIL.ImageDraw.Draw(img)
        draw2=PIL.ImageDraw.Draw(img2)

        font = PIL.ImageFont.truetype(ttfontname, fontsize)
        textWidth, textHeight = draw.textsize(text, font=font)
        textHeight = textHeight * 0.21 + textHeight
        length = canvasSize[0] - textWidth
        height = canvasSize[1] - textHeight
        font_size_offset = 0

        # print(fontsize-font_size_offset)
        textTopLeft = (canvasSize[0] // 2 - textWidth // 2, canvasSize[1] // 2 - textHeight // 2)  # 前から1/6，上下中央に配置

        draw.text(textTopLeft, text, fill=textRGB, font=font)
        draw2.text(textTopLeft,text2,fill=textRGB,font=font)
        if(img!=img2):
            font_list.append(i)

print(len(font_list))
input()




katakana='アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン'
print(len(katakana))
katakana_list=[katakana[i] for i in range(46)]
print(len(font_list))
con=0
start_time=time.time()

im=PIL.Image.open('iro.jpeg')
im_resize=im.resize((64,64))
im_resize.save('iro_resize.jpeg')

for i in font_list:

    print(con)
    # if(2<con):
    #     break
    con+=1

    ttfontname = '../down_font_list/{}'.format(i)

    new_dir_path = str(path)+'/'+i
    os.mkdir(new_dir_path)
    print(new_dir_path)
    os.mkdir(new_dir_path+'/B')
    os.mkdir(new_dir_path+'/B/test')
    os.mkdir(new_dir_path+'/B/train')
    os.mkdir(new_dir_path+'/A')
    os.mkdir(new_dir_path+'/A/test')
    os.mkdir(new_dir_path+'/A/train')

    hidari=64
    migi=0
    arr=np.arange(46)
    np.random.shuffle(arr)
    arr_list=arr[0:5]
    kumi = itertools.combinations(arr_list, 4)
    kumi = list(kumi)
    print(arr_list)
    print('arr_list')
    img = PIL.Image.new('RGB', (64 * 46, 64), (255, 255, 255))
    for jjj in arr_list:
        print('jjj')
        print(jjj)

        text = chr(12451 + jjj)
        text = katakana[jjj]
        img2 = PIL.Image.new('RGB', canvasSize, backgroundRGB)
        draw = PIL.ImageDraw.Draw(img2)

        font = PIL.ImageFont.truetype(ttfontname, fontsize)
        textWidth, textHeight = draw.textsize(text, font=font)
        textHeight = textHeight * 0.21 + textHeight
        length = canvasSize[0] - textWidth
        height = canvasSize[1] - textHeight
        font_size_offset = 0

        while canvasSize[0] < textWidth or canvasSize[1] < textHeight:
            font = PIL.ImageFont.truetype(ttfontname, fontsize - font_size_offset)
            # draw.textsizeで描画時のサイズを取得
            textWidth, textHeight = draw.textsize(text, font=font)
            textHeight = textHeight * 1.21
            font_size_offset += 1

        # print(fontsize-font_size_offset)
        textTopLeft = (canvasSize[0] // 2 - textWidth // 2, canvasSize[1] // 2 - textHeight // 2)  # 前から1/6，上下中央に配置

        draw.text(textTopLeft, text, fill=textRGB, font=font)
        for x in range(64):
            for y in range(64):
                ima = img2.getpixel((x, y))
                # print(ima)

                # print(sum(ima))
                if (sum(ima) != 255 * 3):
                    r, g, b = im_resize.getpixel((x, y))
                    img2.putpixel((x, y), (r, g, b, 0))
        img.paste(img2, (hidari * jjj, 0))

    path_last = str(path) + '/' + str(i) + '/A/test/' + str(i) + '.png'
    path_last = Path(path_last)
    img.save(path_last)
    print('processing time is:{ima}'.format(ima=time.time() - start_time))

    print('jijiji')

    for jj in kumi:
        print(jj)
        hidari=64
        img = PIL.Image.new('RGB', (64 * 46, 64), (255,255,255))
        for kk in jj:



            text = chr(12451 + kk)
            text=katakana[kk]
            img2 = PIL.Image.new('RGB', canvasSize, backgroundRGB)
            draw = PIL.ImageDraw.Draw(img2)


            font = PIL.ImageFont.truetype(ttfontname, fontsize)
            textWidth, textHeight = draw.textsize(text, font=font)
            textHeight=textHeight*0.21+textHeight
            length=canvasSize[0]-textWidth
            height=canvasSize[1]-textHeight
            font_size_offset=0

            while canvasSize[0]< textWidth or canvasSize[1]< textHeight:
                font = PIL.ImageFont.truetype(ttfontname, fontsize - font_size_offset)
                # draw.textsizeで描画時のサイズを取得
                textWidth,textHeight= draw.textsize(text, font=font)
                textHeight=textHeight*1.21
                font_size_offset += 1

            #print(fontsize-font_size_offset)
            textTopLeft = (canvasSize[0] // 2 - textWidth // 2, canvasSize[1]//2-textHeight//2)  # 前から1/6，上下中央に配置


            draw.text(textTopLeft, text, fill=textRGB, font=font)
            for x in range(64):
                for y in range(64):
                    ima=img2.getpixel((x,y))
                    #print(ima)

                    #print(sum(ima))
                    if(sum(ima)!=255*3):
                        r,g,b=im_resize.getpixel((x,y))
                        img2.putpixel((x,y),(r,g,b,0))


            path_last=str(path)+'/'+str(i)+'/image'+str(kk)+'.png'
            path_last = Path(path_last)

            img.paste(img2,(hidari*kk,0))


        for kkk in arr_list:
            if(kkk in jj):
                pass
            else:
                num=kkk
        path_last=str(path)+'/'+str(i)+'/A/train/'+str(i)+'_'+str(num)+'.png'
        path_last=Path(path_last)
        img.save(path_last)
        print('processing time is:{ima}'.format(ima=time.time()-start_time))



    print('finisahed')

    for j in range(len(katakana)):



        text = chr(12451 + j)
        text=katakana[j]
        img2 = PIL.Image.new('RGB', canvasSize, backgroundRGB)
        draw = PIL.ImageDraw.Draw(img2)


        font = PIL.ImageFont.truetype(ttfontname, fontsize)
        textWidth, textHeight = draw.textsize(text, font=font)
        textHeight=textHeight*0.21+textHeight
        length=canvasSize[0]-textWidth
        height=canvasSize[1]-textHeight
        font_size_offset=0

        while canvasSize[0]< textWidth or canvasSize[1]< textHeight:
            font = PIL.ImageFont.truetype(ttfontname, fontsize - font_size_offset)
            # draw.textsizeで描画時のサイズを取得
            textWidth,textHeight= draw.textsize(text, font=font)
            textHeight=textHeight*1.21
            font_size_offset += 1

        #print(fontsize-font_size_offset)
        textTopLeft = (canvasSize[0] // 2 - textWidth // 2, canvasSize[1]//2-textHeight//2)  # 前から1/6，上下中央に配置


        draw.text(textTopLeft, text, fill=textRGB, font=font)
        for x in range(64):
            for y in range(64):
                ima=img2.getpixel((x,y))
                #print(ima)

                #print(sum(ima))
                if(sum(ima)!=255*3):
                    r,g,b=im_resize.getpixel((x,y))
                    img2.putpixel((x,y),(r,g,b,0))


        path_last=str(path)+'/'+str(i)+'/image'+str(j)+'.png'
        path_last = Path(path_last)
        if(j in arr_list):
            path_last=str(path)+'/'+str(i)+'/B/train/'+str(i)+'_'+str(j)+'.png'
            img2.save(path_last)
        img.paste(img2,(hidari*j,0))

    path_last=str(path)+'/'+str(i)+'/B/test/'+str(i)+'.png'
    path_last=Path(path_last)
    img.save(path_last)
    print('processing time is:{ima}'.format(ima=time.time()-start_time))



print('finissuhuihuihed')










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
#
