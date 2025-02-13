from .lotto import Lotto  # 🎲 로또 번호 생성 및 검증을 위한 클래스
from .rank import Rank  # 🏆 로또 당첨 순위를 정의하는 Enum 클래스

# 패키지 외부에서 `from lotto import *` 사용 시 제공할 모듈을 명시적으로 정의합니다.
__all__ = ["Lotto", "Rank"]
