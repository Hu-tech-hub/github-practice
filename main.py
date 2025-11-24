from typing import Union, Optional

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    try:
        if not isinstance(x, (int, float)):
            raise TypeError(f"x는 숫자 타입이어야 합니다. 현재 타입: {type(x).__name__}")
        if not isinstance(y, (int, float)):
            raise TypeError(f"y는 숫자 타입이어야 합니다. 현재 타입: {type(y).__name__}")
        return x + y
    except TypeError as e:
        print(f"타입 오류: {e}")
        raise
    except Exception as e:
        print(f"예상치 못한 오류: {e}")
        raise

def subtract(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    try:
        if not isinstance(x, (int, float)):
            raise TypeError(f"x는 숫자 타입이어야 합니다. 현재 타입: {type(x).__name__}")
        if not isinstance(y, (int, float)):
            raise TypeError(f"y는 숫자 타입이어야 합니다. 현재 타입: {type(y).__name__}")
        return x - y
    except TypeError as e:
        print(f"타입 오류: {e}")
        raise
    except Exception as e:
        print(f"예상치 못한 오류: {e}")
        raise

def power(base: Union[int, float], exponent: Optional[int] = None) -> Union[int, float]:
    """거듭제곱 함수. 지수가 None이면 기본값 2를 사용합니다."""
    try:
        if not isinstance(base, (int, float)):
            raise TypeError(f"base는 숫자 타입이어야 합니다. 현재 타입: {type(base).__name__}")
        if exponent is not None and not isinstance(exponent, int):
            raise TypeError(f"exponent는 정수 타입이거나 None이어야 합니다. 현재 타입: {type(exponent).__name__}")

        exp = exponent if exponent is not None else 2  # Optional 처리: None이면 기본값 2 사용
        return base ** exp
    except TypeError as e:
        print(f"타입 오류: {e}")
        raise
    except Exception as e:
        print(f"예상치 못한 오류: {e}")
        raise

if __name__ == "__main__":
    print("add(1, 2):", add(1, 2))
    print("subtract(5, 3):", subtract(5, 3))

    # Optional 예제: 지수를 지정하지 않으면 기본값 2 사용
    print("power(3):", power(3))  # 3^2 = 9
    print("power(2, 3):", power(2, 3))  # 2^3 = 8
    print("power(1.5, 2):", power(1.5, 2))  # 1.5^2 = 2.25