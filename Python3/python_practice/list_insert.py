a = [10,20,30]
a.insert(2, 10000)
print(a)
print(len(a))

b = [10,20,30]
b.insert(1, [1000,2000])
print(b)
print(len(b))

c = [10,20,30]
c[1:1] = [1000,2000]
print(c)

d = [10,20,30]
d.pop() # 마지막 요소 삭제
# d.pop(1) => 인덱스 1요소 삭제
# del d[1] => d[1] 삭제
# d.remove(20)=> 20인 값 삭제 (가장 먼저인 것 부터 제거!)
# d.index(10) 이면 10의 값을 가진 인덱스를 구할 수 있음
# d.count(값) => 값을 가진 개수를 구할 수 있음
# d.reverse() => 값의 순서를 뒤집음! 
# d.sort() / sort(reverse=False) : 리스트 값을 작은 순서대로 정렬(오름차순)
# d.clear() => 리스트에 있는 거 다 삭제! 

e = [10,20,30]
e[len(e):] = [500]
print(e)
