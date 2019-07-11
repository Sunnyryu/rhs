def computepay(hour, rate):
    if hour > 40 :
        commonpay = rate * hour
        overtimepay = (hour-40.0) * (rate * 0.5)
        pay = commonpay + overtimepay
    else :
        pay = hour * rate
    return pay

inputhour = input("Enter Hour")
inputrate = input("Enter Rate")
floathour = float(inputhour)
floatrate = float(inputrate)

compay = computepay(floathour, floatrate)

print("Pay: ", compay)
