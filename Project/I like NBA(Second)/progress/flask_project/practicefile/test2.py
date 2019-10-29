from functools import update_wrapper

def wrapper(*args, **kwargs):
    pass

def add(a, b):
    """ ADD a + b """
    return a + b

print(wrapper.__doc__) # None
print(wrapper.__name__) # wrapper

update_wrapper(wrapper, add)

print(wrapper.__doc__) # None → ADD a + b
print(wrapper.__name__) # wrapper → add

from functools import partial

# adder 함수는 3개의 위치 인자와, 가변 인자를 모두 받는다
def adder(a, b, c, *args): return a + b + c

# 새롭게 생성된 partial application 이다
# 3개의 인자를 받아야 하지만 일부러 5개를 넘겼다
new_adder = partial(adder, 1, 2, 3, 4, 5)

# 답은 15? 6? 뭘까요?
result = new_adder(4, 5, 6)
