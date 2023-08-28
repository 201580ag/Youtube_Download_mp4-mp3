from pytube import YouTube
from pytube import Playlist
import os

DOWNLOAD_FOLDER = "./"

# 함수 정의: 파일 이름을 유효한 형식으로 정리합니다.
def clean_filename(filename):
    return "".join(c if c.isalnum() or c in ['-', '_', ' '] else '_' for c in filename)

# URL을 입력 받습니다.
url = input("유튜브 동영상 또는 플레이리스트 URL을 입력하세요: ")

# 입력한 URL이 플레이리스트인지 아니면 단일 동영상인지 확인합니다.
if "playlist" in url.lower():
    # 플레이리스트 URL인 경우
    playlist = Playlist(url)

    # 플레이리스트에 있는 모든 동영상을 반복하여 다운로드합니다.
    for video_url in playlist.video_urls:
        yt = YouTube(video_url)

        print("제목 : ", yt.title)
        print("길이 : ", yt.length)
        print("게시자 : ", yt.author)
        print("게시날짜 : ", yt.publish_date)
        print("조회수 : ", yt.views)
        print("키워드 : ", yt.keywords)
        print("설명 : ", yt.description)
        print("썸네일 : ", yt.thumbnail_url)

        # 사용자에게 영상 또는 음성 다운로드 옵션을 물어봅니다.
        download_option = input("영상을 다운로드하시겠습니까? (y/n): ").strip().lower()

        if download_option == 'y':
            stream = yt.streams.get_highest_resolution()
            stream.download(DOWNLOAD_FOLDER)
            print(f'{yt.title} 영상 다운로드 완료')
        elif download_option == 'n':
            # 오디오 스트림을 선택합니다.
            audio_stream = yt.streams.filter(only_audio=True).first()

            # Clean the title to make it suitable as a file name
            cleaned_title = clean_filename(yt.title)

            # Combine the cleaned title with the DOWNLOAD_FOLDER and extension
            file_path = os.path.join(DOWNLOAD_FOLDER, cleaned_title + ".webm")

            # WebM 형식으로 오디오 다운로드
            audio_stream.download(output_path=DOWNLOAD_FOLDER, filename=cleaned_title + ".webm")
            print(f'{yt.title} 오디오(WebM) 다운로드 완료')
        else:
            print("잘못된 입력입니다. 영상 또는 음성을 다운로드하지 않습니다.")

    print("플레이리스트의 모든 동영상 다운로드 완료")
else:
    # 단일 동영상 URL인 경우
    yt = YouTube(url)

    print("제목 : ", yt.title)
    print("길이 : ", yt.length)
    print("게시자 : ", yt.author)
    print("게시날짜 : ", yt.publish_date)
    print("조회수 : ", yt.views)
    print("키워드 : ", yt.keywords)
    print("설명 : ", yt.description)
    print("썸네일 : ", yt.thumbnail_url)

    # 사용자에게 영상 또는 음성 다운로드 옵션을 물어봅니다.
    download_option = input("영상을 다운로드하시겠습니까? (y/n): ").strip().lower()

    if download_option == 'y':
        stream = yt.streams.get_highest_resolution()
        stream.download(DOWNLOAD_FOLDER)
        print(f'{yt.title} 영상 다운로드 완료')
    elif download_option == 'n':
        # 오디오 스트림을 선택합니다.
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Clean the title to make it suitable as a file name
        cleaned_title = clean_filename(yt.title)

        # Combine the cleaned title with the DOWNLOAD_FOLDER and extension
        file_path = os.path.join(DOWNLOAD_FOLDER, cleaned_title + ".webm")

        # WebM 형식으로 오디오 다운로드
        audio_stream.download(output_path=DOWNLOAD_FOLDER, filename=cleaned_title + ".webm")
        print(f'{yt.title} 오디오(WebM) 다운로드 완료')
    else:
        print("잘못된 입력입니다. 영상 또는 음성을 다운로드하지 않습니다.")
