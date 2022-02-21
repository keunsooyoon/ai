vowels = ['a','e','i','o','u']  # vowels 변수 리스트 선언

word = input('Provive a word to search for vowels:')  # 검색할 단어 입력

found = [] # 검색된 모음 담기

for letter in word:      # 입력한 단어에서 한글자씩 추출
    if letter in vowels: # 추출한 한글자가 모음 리스트에 있는지 확인
        if letter not in found: # 기존 리스트에 같은 모음이 있는지 확인(중복제거)
            found.append(letter)# 기존 리스트에 없으면 담기 (중복 회피)

# for vowel in found:
#     print(vowel)

print(found)




# vowels = ['a','e','i','o','u']

# word = 'Milliways'

# found = []

# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)

# for vowel in found:
#     print(vowel)

