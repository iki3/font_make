import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import glob
import os
import time
from pathlib import Path

path = Path(__file__).parent   # test.pyのあるディレクトリ
path /= '../font_datasets'
print(path)
print(os.path.exists(path))


# 使うフォント，サイズ，描くテキストの設定

fontsize = 64


# 画像サイズ，背景色，フォントの色を設定
canvasSize    = (64, 64)
backgroundRGB = (255, 255, 255)
textRGB       = (0, 0, 0)

# 文字を描く画像の作成
font_list=[os.path.basename(p) for p in glob.glob('/usr/share/fonts/truetype/**/*.ttf', recursive=True) if os.path.isfile(p)]

print(font_list[292])
ttfontname = 'usr/share/fonts/truetype/**/{}'.format(font_list[292])
#
#
# print(len(font_list))
# con=0
# start_time=time.time()
# for i in font_list:
#     print(con)
#     con+=1
#
#     ttfontname = 'usr/share/fonts/truetype/**/{}'.format(i)
#
#     new_dir_path = str(path)+'/'+i
#     os.mkdir(new_dir_path)
#
#
#     for j in range(26):
#         text = chr(65 + j)
#         img = PIL.Image.new('RGB', canvasSize, backgroundRGB)
#         draw = PIL.ImageDraw.Draw(img)
#
#
#         font = PIL.ImageFont.truetype(ttfontname, fontsize)
#         textWidth, textHeight = draw.textsize(text, font=font)
#         textHeight=textHeight*0.21+textHeight
#         length=canvasSize[0]-textWidth
#         height=canvasSize[1]-textHeight
#         font_size_offset=0
#         while canvasSize[0]< textWidth or canvasSize[1]< textHeight:
#             font = PIL.ImageFont.truetype(ttfontname, fontsize - font_size_offset)
#             # draw.textsizeで描画時のサイズを取得
#             textWidth,textHeight= draw.textsize(text, font=font)
#             textHeight=textHeight*1.21
#             font_size_offset += 1
#
#         #print(fontsize-font_size_offset)
#         textTopLeft = (canvasSize[0] // 2 - textWidth // 2, canvasSize[1]//2-textHeight//2)  # 前から1/6，上下中央に配置
#
#
#
#         draw.text(textTopLeft, text, fill=textRGB, font=font)
#         path_last=str(path)+'/'+str(i)+'/image'+str(j)+'.png'
#         path_last = Path(path_last)
#         img.save(path_last)
#         if(canvasSize[0]<textWidth or canvasSize[1]/0.79<textHeight/1.21) :
#             print(textWidth,textHeight)
#             break
#     else:
#         print('processing time is:{ima}'.format(ima=time.time()-start_time))
#         continue
#
#     print(i,j)
#     print('breaked')
#     break
# print('finisshed')













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
