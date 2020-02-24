import turtle as t
 
t.shape('turtle')
t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
for i in range(300):    # 300번 반복
    t.forward(i)        # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
    t.right(91)         # 오른쪽으로 91도 회전



#터틀의 shape에는 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic' 등을 지정하여 여러 가지 터틀 모양을 사용할 수 있습니다. 특히, t.shape()와 같이 shape를 그대로 호출하면 현재 모양을 알아낼 수 있습니다.
