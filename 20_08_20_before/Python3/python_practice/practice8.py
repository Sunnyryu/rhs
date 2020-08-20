def bigger_price(limit: int, data: list) -> list:
    return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]
    # price라는 키가 있는 값(것)을 정렬해줌, reverse = True 는 내림차순으로 다시 정렬


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')

#k=[] - k를 빈 리스트로 생
#k=sorted(data, key = lambda price1: price1['price'], reverse = True) - 람다라는 함수를 이용해서 정의
# k=k[0:limit] - k 0부터 limit을 받아와서 상위 몇개를 뽑아줌, 위에서 2이므로 상위 2개를 뽑아
#   return k - k를 돌려줌
# pprint는 글씨를 예쁘게 써준다는 것임!?

#   import operator, heapq, functools
#bigger_price = functools.partial(heapq.nlargest, key=operator.itemgetter('price'))
