from pytube import YouTube

def video_download(url):
    YouTube(url).streams[1].download(output_path='./downloads')


def main():
    url = input('Digite a url do video do YouTube: ')
    video_download(url)


if __name__ == '__main__':
    main()