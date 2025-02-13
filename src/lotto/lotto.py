import random


class Lotto:
    """
    로또 번호 생성 및 유효성 검증하는 클래스
    """

    def __init__(self, numbers: list[int]):
        """
        로또 객체 초기화
        """
        self._validate(numbers)
        self._numbers = sorted(numbers)

    def _validate(self, numbers: list[int]):
        """
        로또 번호 유효성 검사
        (로또 번호 6개, 중복 불가, 1~45의 범위)
        """
        if len(numbers) != 6:
            raise ValueError("로또 번호는 6개여야 합니다.")
        if len(set(numbers)) < 6:
            raise ValueError("로또 번호는 중복되어서는 안됩니다.")
        if max(numbers) > 45 or min(numbers) < 1:
            raise ValueError("로또 번호의 숫자 범위는 1~45까지입니다.")

    @classmethod
    def generate_num(cls):
        """
        1~45 사이의 랜덤한 6개의 숫자로 로또 객체 생성
        """
        return cls(random.sample(range(1, 46), 6))

    def get_numbers(self):
        """
        로또 번호 리스트 반환
        """
        return self._numbers

    def __str__(self):
        """
        로또 번호 문자열로 반환
        """
        return str(self._numbers)
