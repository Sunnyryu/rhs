## Python3

#### Image 

```
이미지 데이터는 픽셀(pixel)

파이썬에서는 NumPy의 ndarray 클래스 배열로 표현 (N-dimensional array ) n차 배열!

픽셀의 색을 숫자로 표현하는 방식을 색공간(color space) -> 그레이스케일(gray scale), RGB(Red-Green-Blue), HSV(Hue-Saturation-Value) 방식

그레이스 스케일 : 모든 색이 흑백이다. 각 픽셀은 명도를 나타내는 숫자로 표현된다. 0은 검은색을 나타내고 숫자가 커질수록 명도가 증가하여 하얀색이 된다. 숫자는 보통 0~255의 8비트 부호없는 정수로 저장

인수는 gray = True / 이미지 크기 => 배열의 shape로 확인 가능!!

RGB
RGB 색공간에서 색은 적(Red), 녹(Green), 청(Blue)의 3가지 색의 명도를 뜻하는 숫자 3개가 합쳐진 벡터로 표현된다. 8비트 부호없는 정수를 사용하는 경우 (255, 0, 0)은 빨간색, (0, 255, 0)은 녹색, (0, 0, 255)는 파란색이다.

픽셀 데이터가 스칼라가 아닌 벡터이므로 이미지 데이터는 (세로픽셀수 x 가로픽셀수) 형태의 2차원 배열로 표현하지 못하고 (세로픽셀수 x 가로픽셀수 x 색채널) 형태의 3차원 배열로 저장 

HSV(Hue, Saturation, Value) 색공간에서는 색이 다음 세가지 값 (색상 / 채도 / 명도)

Pillow를 이용한 이미지 처리 ( 파이썬 PIL 패키지 대체 가능!!)

Image 클래스를 사용하면 여러가지 다양한 포맷의 이미지를 읽고 변환하여 저장
(open, show, save => Image.open/ Image.show / Image.save)
파일로 저장할 때는 save 메서드를 사용

copy() => 복사 / eval() 밝기, 색상 조정 / convert() : 모드 변경 

ImageFilter ! / ImageDraw !


Image 클래스 객체를 NumPy 배열로 변환할 때는 np.array 함수를 사용
imshow 명령으로 볼 수 있음 

NumPy 배열을 Image 객체로 바꿀 때는 fromarray 클래스 메서드를 사용 (Image.fromarray)
이미지의 크기를 확대 또는 축소하려면 resize 메서드를 사용 (a.resize((x,y)))

썸네일(thumbnail) 이미지를 만들고 싶다면 Image객체의 thumbnail 메서드를 사용한다. resize 메서드는 원래 객체는 그대로 유지한 채 변환된 이미지를 반환하지만 thumbnail 메서드는 원래 객체 자체를 바꾸는 인플레이스(in-place) 메소드이므로 주의


이미지를 회전하기 위해서는 rotate 메서드를 호출

crop 메서드를 사용하면 이미지에서 우리가 관심이 있는 특정 부분(ROI: region of interest)만 추출 할 수 있음 !!

Scikit-Image(Skimage)

Scikit-Image는 data라는 모듈을 통해 샘플 이미지 데이터를 제공 => 이미지는 넘파이 배열 자료형 !!

Scikit-Image 패키지로 이미지를 읽고 쓸 때는 io 서브패키지의 imsave, imread 명령을 사용 (skimage.io.imsave / skimage.io.imread)

Scikit-Image는 그레이스케일, RGB, HSV 등의 색공간을 변환하는 기능을 color 서브패키지에서 제공

OpenCV(Open Source Computer Vision)은 이미지 처리, 컴퓨터 비전을 위한 라이브러리

실시간 이미지 프로세싱에 중점을 둔 라이브러리이며 많은 영상처리 알고리즘을 구현

cv2로 import 하며, cvtColor 명령을 사용하면 더 간단하게 색공간을 변환할 수도 있음 !!

이미지 파일을 만들 때는 imwrite 명령을 사용(cv2.imwrite)

resize() 명령으로 이미지 크기 변환 기능을 제공(cv2.resize())

Numpy 정리 후 계속 정리

numpy - arrange / linspace

arrange_1 = arrange(0,11) => array([0,1,2,3,4,5,6,7,8,9,10])
linspace_1 = linspace(0., 3.5, 8) => array([0, 0.5, 1 ... 3. , 3.5])

zeros / ones

zeros((1,2)) => array([0., 0.])
ones((2,2,2)) => array([[[1., 1.],[1.,1.]],
                        [1.,1.],[1.,1.]] )
transpose()
=> trans_array = ([1,2], [3,4])
=> trans_array.transpose() => array([1,3], [2,4])

sort() => 순서를 맞춰줌!!

max() => max_array = array([1,2], [3,4])
max_array.max() => 4 / max_array(axis=0) => array([3,4])
max_array(1) => array([2,4])



```
