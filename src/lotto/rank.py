from enum import Enum

class Rank(Enum):
    """
    로또 당첨 순위 정의하는 클래스
    """

    FIFTH = (3, False, 5_000)
    FOURTH = (4, False, 50_000)
    THIRD = (5, False, 1_500_000)
    SECOND = (5, True, 30_000_000)
    FIRST = (6, False, 2_000_000_000)
    NONE = (0, False, 0)

    def __init__(self, match_cnt, bonus_match, prize):
        """
        Rank 객체 초기화
        """
        self.match_cnt = match_cnt
        self.bonus_match = bonus_match
        self.prize = prize

    @classmethod
    def get_rank(cls, match_cnt, bonus):
        """
        일치 개수와 보너스 번호 여부를 기반으로 당첨 순위 반환
        """
        for rank in cls:
            if rank.match_cnt == match_cnt and rank.bonus_match == bonus:
                return rank
        return cls.NONE