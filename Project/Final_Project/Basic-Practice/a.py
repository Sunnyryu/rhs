#x = int(input("input number please:"))
#print(x)

#for c in "string":
#    print(c)


#for i in range(0,5):
#    print(i, i**2)
    #print(i, i**i)

score = {
    "a": {
    "math": 80,
    "english": 90,
    "music":100
    },
    "b": {
    "math": 85,
    "english": 100,
    "music": 80
    }
}

#total_score = sum(score.values())
#avg = total_score / len(score)
#print(score.values())

#print(total_score, avg)

a_sum = sum(score["a"].values())
b_sum = sum(score["b"].values())

avg = (a_sum + b_sum) / len(score["a"])
avg2 = (a_sum +b_sum) / len(score)
#print(len(score)) # len(score) = "a" + "b" => 2
#print(avg)
#print(avg2)


city = {
    "서울": [-6, -10,5],
    "대전": [-3,-5,2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}
for name, temp in city.items():
    avg_temp = sum(temp) / len(temp)
    print(f'{name}:평균 기온은 {avg_temp}입니다.')

print("있어요") if 2 in city["서울"] else print("없어요")
