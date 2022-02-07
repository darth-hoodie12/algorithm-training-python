from seqSearch import seq_search

a = (3, 9, 3.2, 4.98, 6.5, 2983)
b = 'string'
c = ['MP4', 'PKG', 'DAT', 'JPEG']

print(f'{a}에서 4.98의 인덱스는 {seq_search(a, 4.98)}입니다.')
print(f'{b}에서 "r"의 인덱스는 {seq_search(b, "r")}입니다.')
print(f'{c}에서 "PKG"의 인덱스는 {seq_search(c, "PKG")}입니다.')
