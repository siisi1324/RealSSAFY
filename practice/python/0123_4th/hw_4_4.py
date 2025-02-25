list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
    '위대한 개츠비',
    '데미안',
    '난중일기'
]

rental_book = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]
     
missing_book = [book for book in rental_book if book not in list_of_book]
print(missing_book)


if not missing_book:
    print(f'모든 도서가 대여 가능한 상태입니다.')
else:
    for book in missing_book:
        print(f'{book} 을/를 보충하여야 합니다. ')

# 여기서 if missing_book == None: 이라고 하면, missing_book은 리스트형식이므로 항상 None이 아니라 []형태로
# 출력을 하게되는데, 그래서 if not missing_book: 라는 식으로 써줘야 한다. 
