import os, requests
folder_to_download = 'DOWNLOAD'
if not os.path.exists(folder_to_download):
    os.mkdir(folder_to_download)
page = requests.get(url = 'https://dysphonic.eu/songs.html').content

items = page.split(b'class="song-expand">')
for item in items:
    name = item.split(b'<')[0].decode('utf-8')
    if len(name)<2:
        continue
    safename = name.replace('/','-')
    name = f"ИМЕ НА ПЕСЕНТА: {name} \n\n"
    other = item.split(b'<div id="')
    lyrics = other[1].split(b'<a href=')
    with open(os.path.join(folder_to_download, f'{safename}.txt'),'wb') as f:
        f.write(name.encode('utf-8'))
        f.write(lyrics[0].split(b'>')[1].split(b'<')[0])
    with open(os.path.join(folder_to_download, f'{safename}.txt'),'r',encoding="utf-8") as f:
        text = f.read()
    with open(os.path.join(folder_to_download, f'{safename}.txt'),'w',encoding="utf-8") as f:
        f.write(text.replace('\n','\r\n'))
