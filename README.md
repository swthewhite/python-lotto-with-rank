# 미션 - 로또

> [!NOTE]  
> 이 코드는 원래 [java-lotto-6](https://github.com/woowacourse-precourse/java-lotto-6)에서 제공된 **Java 기반의 로또 게임**을 **Python**에 맞게 변환한 과제입니다. 프로젝트 구조, 요구 사항, 기능 구현 방식은 원본 저장소를 바탕으로 Python 환경에 맞추어 수정하였습니다.

---

## 🔍 진행 방식

- 미션은 **기능 요구 사항, 프로그래밍 요구 사항, 과제 진행 요구 사항** 세 가지로 구성되어 있습니다.
- 세 가지 요구 사항을 만족하기 위해 노력해야 하며, 특히 기능을 구현하기 전에 기능 목록을 작성하고 기능 단위로 커밋하는 방식으로 진행해야 합니다.
- 기능 요구 사항에 명시되지 않은 부분은 스스로 판단하여 구현할 수 있습니다.

## 📮 미션 제출 방법

- 미션 구현을 완료한 후 GitHub을 통해 제출해야 합니다.
  - **Pull Request로 최종 제출**

## 🚨 과제 제출 전 체크 리스트 - 0점 방지

- 기능을 모두 정상적으로 구현했더라도 **요구 사항에 명시된 출력값 형식을 지키지 않을 경우 0점 처리**됩니다.
- 기능 구현을 완료한 뒤 아래 가이드에 따라 테스트를 실행하고 모든 테스트가 성공하는지 확인합니다.
- **테스트가 실패할 경우 0점 처리**되므로, 반드시 확인 후 제출해야 합니다.



### 테스트 실행 가이드

- 터미널에서 `python --version`을 실행하여 Python 버전이 3.9 이상인지 확인합니다.
- 프로젝트의 의존성 패키지를 설치하기 위해 `pip install -r requirements.txt` 명령어를 실행합니다.
- 아래 명령어를 실행하여 모든 테스트가 성공하는지 확인합니다.

```bash
pytest
```

테스트 실행 시 출력 예시는 다음과 같습니다.

```bash
=========================== test session starts ============================
platform darwin -- Python 3.9.x, pytest-6.2.5
rootdir: /path/to/project
collected 5 items

tests/lotto/test_main.py ....                                   [ 80%]
tests/lotto/test_lotto.py ..                                            [100%]

============================ 100% passing in Xs =============================
```

---

## 🚀 기능 요구 사항

로또 게임 기능을 구현해야 합니다. 로또 게임은 아래와 같은 규칙으로 진행됩니다.

```
- 로또 번호의 숫자 범위는 1~45까지입니다.
- 1개의 로또를 발행할 때 중복되지 않는 6개의 숫자를 뽑습니다.
- 당첨 번호 추첨 시 중복되지 않는 숫자 6개와 보너스 번호 1개를 뽑습니다.
- 당첨은 1등부터 5등까지 있습니다. 당첨 기준과 금액은 아래와 같습니다.
    - 1등: 6개 번호 일치 / 2,000,000,000원
    - 2등: 5개 번호 + 보너스 번호 일치 / 30,000,000원
    - 3등: 5개 번호 일치 / 1,500,000원
    - 4등: 4개 번호 일치 / 50,000원
    - 5등: 3개 번호 일치 / 5,000원
```

- 로또 구입 금액을 입력하면 구입 금액에 해당하는 만큼 로또를 발행해야 합니다.
- 로또 1장의 가격은 1,000원입니다.
- 당첨 번호와 보너스 번호를 입력받습니다.
- 사용자가 구매한 로또 번호와 당첨 번호를 비교하여 당첨 내역 및 수익률을 출력하고 로또 게임을 종료합니다.
- 사용자가 잘못된 값을 입력할 경우 `ValueError`를 발생시키고, "[ERROR]"로 시작하는 에러 메시지를 출력 후 그 부분부터 입력을 다시 받습니다.

### 입출력 요구 사항

#### 입력

- 로또 구입 금액을 입력받습니다. 구입 금액은 1,000원 단위로 입력받으며 1,000원으로 나누어 떨어지지 않는 경우 예외 처리합니다.

```
14000
```

- 당첨 번호를 입력받습니다. 번호는 쉼표(,)를 기준으로 구분합니다.

```
1,2,3,4,5,6
```

- 보너스 번호를 입력받습니다.

```
7
```

#### 출력

- 발행한 로또 수량 및 번호를 출력합니다. 로또 번호는 오름차순으로 정렬하여 보여줍니다.

```
8개를 구매했습니다.
[8, 21, 23, 41, 42, 43] 
[3, 5, 11, 16, 32, 38] 
[7, 11, 16, 35, 36, 44] 
[1, 8, 11, 31, 41, 42] 
[13, 14, 16, 38, 42, 45] 
[7, 11, 30, 40, 42, 43] 
[2, 13, 22, 32, 38, 45] 
[1, 3, 5, 14, 22, 45]
```

- 당첨 내역을 출력합니다.

```
3개 일치 (5,000원) - 1개
4개 일치 (50,000원) - 0개
5개 일치 (1,500,000원) - 0개
5개 일치, 보너스 볼 일치 (30,000,000원) - 0개
6개 일치 (2,000,000,000원) - 0개
```

- 수익률은 소수점 둘째 자리에서 반올림합니다. (ex. 100.0%, 51.5%, 1,000,000.0%)

```
총 수익률은 62.5%입니다.
```

- 예외 상황 시 에러 문구를 출력해야 합니다. 단, 에러 문구는 "[ERROR]"로 시작해야 합니다.

```
[ERROR] 로또 번호는 1부터 45 사이의 숫자여야 합니다.
```

#### 실행 결과 예시

```
구입금액을 입력해 주세요.
8000

8개를 구매했습니다.
[8, 21, 23, 41, 42, 43] 
[3, 5, 11, 16, 32, 38] 
[7, 11, 16, 35, 36, 44] 
[1, 8, 11, 31, 41, 42] 
[13, 14, 16, 38, 42, 45] 
[7, 11, 30, 40, 42, 43] 
[2, 13, 22, 32, 38, 45] 
[1, 3, 5, 14, 22, 45]

당첨 번호를 입력해 주세요.
1,2,3,4,5,6

보너스 번호를 입력해 주세요.
7

당첨 통계
---
3개 일치 (5,000원) - 1개
4개 일치 (50,000원) - 0개
5개 일치 (1,500,000원) - 0개
5개 일치, 보너스 볼 일치 (30,000,000원) - 0개
6개 일치 (2,000,000,000원) - 0개
총 수익률은 62.5%입니다.
```

---

## 🎯 프로그래밍 요구 사항

- Python 3.9 이상에서 실행 가능해야 합니다. **정상적으로 동작하지 않을 경우 0점 처리**됩니다.
- 프로그램 실행의 시작점은 `src/lotto/main.py`의 `main()` 함수입니다.
- 외부 라이브러리를 사용하지 않습니다.
- [Python 코드 스타일 가이드(Python PEP8)](https://peps.python.org/pep-0008/)을 준수하며 프로그래밍합니다.
- 프로그램 종료 시 `sys.exit()`를 호출하지 않습니다.
- 프로그램 구현이 완료되면 `tests/lotto/test_main.py`의 모든 테스트가 성공해야 합니다. **테스트가 실패할 경우 0점 처리**됩니다.
- 프로그래밍 요구 사항에서 별도로 명시하지 않는 한 파일과 패키지 이름을 수정하거나 이동하지 않습니다.
- 들여쓰기(인덴트) 깊이를 3을 넘지 않도록 구현합니다. 2까지만 허용합니다.
  - 예를 들어, while문 안에 if문이 있으면 들여쓰기는 2입니다.
  - 함수나 메서드를 분리해 들여쓰기 깊이를 줄이는 것이 좋습니다.
- 삼항 연산자를 사용하지 않습니다.
- 함수나 메서드는 한 가지 일만 하도록 작게 작성해야 합니다.
- Pytest와 Assert를 이용해 본인이 정리한 기능 목록이 정상 동작하는지 테스트 코드로 확인합니다.

### 추가된 요구 사항

- 함수나 메서드의 길이는 15라인을 넘지 않도록 구현합니다.
- else 예약어를 사용하지 않습니다.
  - 힌트: if 조건절에서 값을 반환하면 else를 생략할 수 있습니다.
- Python의 Enum을 적용합니다.
- 도메인 로직에 단위 테스트를 구현해야 합니다. 단, UI(System.out, input) 로직은 제외합니다.
  - 핵심 로직을 구현하는 코드와 UI를 담당하는 로직을 분리합니다.
    - src/lotto/lotto.py: 핵심 로직을 구현
    - src/lotto/main.py: UI(입출력)를 담당하는 로직 구현
  - 단위 테스트 작성이 익숙하지 않다면 `tests/lotto/test_lotto.py`를 참고하여 학습한 후 테스트를 구현합니다.

---

## ✏️ 과제 진행 요구 사항

- 미션은 [python-lotto](https://github.com/swthewhite/python-lotto) 저장소를 Fork & Clone하여 시작합니다.
- **기능을 구현하기 전 `docs/README.md`에 구현할 기능 목록을 정리**해 추가합니다.
- **Git의 커밋 단위는 앞 단계에서 `docs/README.md`에 정리한 기능 목록 단위**로 추가합니다.
  - [커밋 메시지 컨벤션](https://gist.github.com/stephenparish/9941e89d80e2bc58a153) 가이드를 참고해 커밋 메시지를 작성합니다.