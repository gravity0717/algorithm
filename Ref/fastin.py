# input을 쓰면 이렇게 Overlap이 된다. 이 경우 원래 input 함수를 쓸 수 없다.
# input 함수와 sys.stdin.readline 함수의 차이
# input은 개행문자가 자동 삭제되고, prompt를 띄울 수 있다.
# sys.stdin.readline은 개행문자를 우리가 직접 삭제해야 하고, prompt를 띄울 수 없다.

import sys
input = sys.stdin.readline

t = int(input("Hello"))
print(t)
addingPairs = [tuple(map(int, input().rstrip().split())) for _ in range(t)]
for addingPair in addingPairs:
    print(addingPair[0] + addingPair[1])