def bigger_price(limit: int, data: list) -> list:
    return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]


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
# k=k[0:limit] - k 0부터 끝까지
#   return k - k를 돌려줌
   

#   import operator, heapq, functools
#bigger_price = functools.partial(heapq.nlargest, key=operator.itemgetter('price'))
