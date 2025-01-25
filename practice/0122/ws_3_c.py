def power(base, exponent):
    '''
        함수(2, 3) 실행
            base에 2 할당, exponent에 3할당
            지수가 0이 된 경우, 1을 반환 | 2의 0승은 1

            아닌경우, 지수가 0이 될 때까지 [exponent - 1] 을 다시 지수에 할당하여 함수 호출
                2 * 함수(2, 3-1)

            모든 상황을 반복하는 과정
            2 * (2 * (2 * 1))  
            결과 : 8
    '''
    if exponent == 0:
        return 1
    else: 
        return base*power(base, exponent-1)
        
        
result_2 = power(2, 3)
print(result_2) 


def sum_of_digits(number):

    if number<10:
        return number
    else:
        return (number%10)+sum_of_digits(number//10)
result_3 = sum_of_digits(321)
print(result_3)
