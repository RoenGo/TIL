# 1. 모듈 불러오기
import random
# 2. 숫자 통(1~45)
numbers = range(1, 46)    # range(n,m) : n이상 m미만
# 3. 그 중에서 6개를 sample
# random.sample(통, 갯수)
print(sorted(random.sample(numbers, 6)))
# 4. 결과 출력