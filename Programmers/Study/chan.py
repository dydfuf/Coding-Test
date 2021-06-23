if __name__ == "__main__":
    song = "\n동해물과 백두산이 마르고 닳도록\n" \
           "하느님이 보우하사 우리나라 만세\n" \
           "무궁화 삼천리 화려강산\n" \
           "대한사람 대한으로 길이 보전하세\n"

    # 대한의 개수 찾기
    num_of_DaeHan = 0
    for aSong in song:
        if aSong == "대":
            if song[song.index(aSong)+1] == "한":
                num_of_DaeHan += 1

    # 동해의 인덱스 찾기
    idx_of_DongHae = -1
    for aSong in song:
        if aSong == "동":
            if song[song.index(aSong)+1] == "해":
                idx_of_DongHae = song.index(aSong) + 1

    # 사랑의 인덱스 찾기
    idx_of_SaRang = -1
    for aSong in song:
        if aSong == "사":
            if song[song.index(aSong)+1] == "랑":
                idx_of_DongHae = song.index(aSong) + 1

    # 동해를 남해로, 백두산을 한라산으로 바꾸기
    change_song = song.replace("동해", "남해")
    change_song = change_song.replace("백두산", "한라산")

    # 맨앞 맨뒤 공백 제거
    change_song2 = change_song[1:]
    change_song2 = change_song2[:len(change_song2)-1]

    # \n을 기준으로 스플릿
    split_song = change_song2.split("\n")

    print("=" * 20)
    print(song)
    print("=" * 20)
    print("\"대한\" 은 몇번 등장 : ", num_of_DaeHan)
    print("\"동해\"의 인덱스 : ", idx_of_DongHae)
    print("\"사랑\"의 인덱스 : ", idx_of_SaRang)
    print("=" * 20)
    print(change_song)
    print("=" * 20)
    print(change_song2)
    print("=" * 20)
    print(split_song)
    print("=" * 20)
    for aSplitSong in split_song:
        print(aSplitSong)
    print("=" * 20)