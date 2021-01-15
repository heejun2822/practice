# 함수
# 특정 역할을 하는 코드의 집합
# 하나의 함수는 하나의 역할만 해야한다.

# 함수 정의
# def funcname(parameter_list):
#     """
#     설명서
#     """
#     pass
def sum(a, b):
    result = a + b
    return result

# 함수 실행(호출)
sum(1, 2)
print(sum(1,2))

# 함수 실행 결과(return)값 변수에 할당
result = sum(1, 2)
print(result)