from gg import download_json, download_img

url = 'https://www.dcard.tw/_api/forums/pet/posts?popular=true'
path = 'D:\py\spider\pet'

all_medias = download_json(url)
all_medias = [i['media'] for i in all_medias]

# download_img(a[0]['media'][0]['url'], f'{path}\img.jpg')

count = 0

for medias in all_medias:
    for media in medias:  # 一篇文可能有不只一張圖片
        download_img(media['url'], f'{path}\img{count}.jpg')
        count += 1


