from typing import Union

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y

def subtract(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x - y

if __name__ == "__main__":
    print(add(1, 2))
    print(subtract(1, 2))