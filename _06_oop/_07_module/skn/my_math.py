# 사용자 모듈

pi: float = 3.14

x: int = 20

def get_circle_area(r: float) -> float:
    return pi * r * r

print("my_math.__name__: ", __name__)

if __name__ == "__main__":
    print("my_math.py를 직접 실행 하셨군요...")
    pass
else:
    print("__name__: ", __name__)
    print("다른 py 파일에 my_math..py가 import되었습니다.")

    print("*" * 100)
    print("*" * 100)

pi = 3.14
__z = 'hello'