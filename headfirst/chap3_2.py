vowels = ['a','e','i','o','u']  # vowels 변수 리스트 선언

word = input('Provive a word to search for vowels:')  # 검색할 단어 입력

found = {} # 검색된 모음 딕셔너리로 담기

for letter in word:      # 입력한 단어에서 한글자씩 추출
    if letter in vowels: # 추출한 한글자가 모음 리스트에 있는지 확인
        found.setdefault(letter, 0) # 초기화 setdefault
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')
