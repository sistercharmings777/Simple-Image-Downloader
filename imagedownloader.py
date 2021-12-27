import requests

def download_files(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        print("downloading information.....")
        with open('C:/Users/Prince Asante/Desktop/'+ local_filename, 'wb') as f:
            print("writing data to file")
            for chunk in r.iter_content(chunk_size=1042):
                f.write(chunk)
    f.close()
    print("Download complete")
    print("File saved as "+ local_filename)
            
while 1:
    print("welcome to the image downloader")
    image_url = input(str("Image url: "))
    download_files(image_url)
    