## My Ubuntu

#### Ubuntu 8

```
우분투와 db 연결을 활용하기 전에 Mariadb 용어 이해하기 !

data : 자료
table : 데이터를 표 형식으로 표현
database : 테이블을 저장하는 저장 공간 또는 테이블의 집합
DBMS : Database들을 관리하는 소프트웨어
레코드 or 로우 : 테이블의 행
필드 or 컬럼 : 테이블의 열
데이터 타입 : 각 필드에 입력할 값의 타입(정수, 문자, 날짜 etc)
필드 이름 : 각 필드(열)의 이름
주 키 필드 : 레코드를 식별하기 위한 유일한 값을 갖고 있으며 비어있지 않은 필드
외래 키 필드: 다른 테이블의 주 키와 대응되는 필드
RDBMS : 관계형 RDBMSSQL : 구조화된 질의 언어란 의미로 쓰임, DB에서 정보를 얻거나, 생성하거나, 갱신하려고 정의한 표준 언어(규약)
```

```
기본 sql 문

SHOW DATABASES; (데이터베이스 이름 조회)
USE 데이터베이스이름; (사용할 데이터베이스 지정)
Create Database 데이터베이스이름;(데이터베이스 생성)
DROP DATABASE 데이터베이스이름;(데이터베이스 완전 삭제)

SHOW TABLES;(테이블 이름 조회)
EXPLAIN 테이블이름; or DESC 테이블이름; (테이블 구조(형태) 조회)
CREATE TABLE 테이블이름 (필드이름1 필드타입1, 필드이름2 필드타입2- 테이블생성);
DROP TABLE 테이블이름; (테이블 삭제)
ALTER TABLE 옵션; (테이블 수정)

INSERT INTO 테이블이름 VALUES (값1, 값2) - 레코드 입력
  AUTO_INCREMENT(자동으로 증가하는 조건)
DELETE FROM 테이블이름 WHERE 조건; - 레코드 삭제
UPDATE 테이블이름 SET 필드이름=수정할값 ... WHERE 조건; - 레코드 수정
```

```
SELECT 필드이름
FROM 테이블이름
WHERE 조건식
ORDER BY [이름] ASC or DESC;
GROUP BY [그룹으로 묶을 이름들]
HAVING 조건식
```

```
WHERE 절
  WHERE 이름 >=, >, <, <= 값
  WHERE 이름 BETWENN A AND B;
  WHERE 이름 LIKE 's%';
  WHERE 이름 IN
  등 사용
  ANY / ALL / SOME - A,B 조건 두개다 성립한다고 생각하면 됌 / a.b 조건 중에서 더 좁은 조건만 적용 됌 / some은 any와 동일한 의미로 쓰임
```

```
SubQuery - 간단하게는 쿼리문 안에 쿼리문이 들어 있는 것임!
ex) select name height from userinfo
where height IN (SELECT FROM userinfo WHERE addr = "인천");
```

```
ORDER BY (순서를 정렬 하기 위해 사용)
ASC (오름차순 - 일반적으로 생략) / DESC (내림차순)
Distinct (중복된 것 한 개만 출력)
Limit(출력 개수를 제한하는 것! ex Limit5 = 5개로 제한함)

GROUP BY 절 / HAVING 절 : GROUP BY절은 그룹으로 묶어주는 역할, 집계함수와 자주 쓰임(SUM 등) / HAVING절은 WHERE 절과 다르게 집계 함수에 대해서 조건을 제한하는 것임

ROLLUP : GROUP BY와도 사용하며 WITH ROLLUP의 형태로도 사용한다.(분류 별로 합계 및 그 총합을 구하고 싶을 떄?)
```

```
DML : 데이터를 조작하는 데 사용하는 언어 (SELECT / INSERT / UPDATE / DELETE)
DDL : 데이터베이스, 테이블, 뷰, 인덱스 등의 DB 개체를 생성/삭제/변경 하는 역할을 함(CREATE,DROP,ALTER)
      mariadb에서는 ddl을 사용하면 즉시 적용되어 commit이나 rollback 등의 TCL 처리를 할 수 없음
DCL : 사용자에게 어떤 권한을 부여하거나 빼앗을 때 사용 (GRANT/REVOKE/DENY)
```

```
WITH 절과 CTE

WITH CTE_TABLE명(열 이름)
AS
(
  <쿼리문>
  )
SELECT 열이름 FROM CTE_TABLE명;
```

```
SET @변수이름 = 변수의 값 -> 변수의 선언 및 값 대입
SELECT @변수이름; -> 변수의 값 출력
```

```
데이터 형식 변환 함수
CAST() / CONVERT()

CAST (expression AS 데이터형식 [ (길이)])
CONVERT (expression, 데이터 형식 [ (길이)])

암시적 / 명시적 형변환
명시적인 형변환은 cast나 connvert 함수를 이용하여 데이터 형식을 변환하는 것이며 암시적 형변환은 함수를 사용하지 않고 형을 변환되는 것임
```

```
MariaDB 내장 함수

제어 흐름 함수
IF (수식, 참, 거짓) - 수식이 참 또는 거짓인지 결과에 따라서 2중 분기
IFNULL(수식1, 수식2) - 수식1이 NULL이 아니면 수식1이 반환하고 NULL이면 수식2가 반환
NULLIF(수식1, 수식2) - 수식1과 2가 같으면 Null 반환 / 다르면 수식1을 반환
CASE ~ WHEN ~ ELSE ~ END (CASE는 내장함수는 아니고 연산자로 분류됨.)

문자열함수
ASCII(아스키코드), CHAR(숫자) - 문자의 아스키 코드값을 돌려주거나 숫자의 아스키 코드값에 해당하는 문자를 돌려줌

BIT_LENGTH(문자열), CHAR_LENGTH(문자열), LENGTH(문자열) - Bit 크기 또는 문자 크기 반환 / CHAR_LENGTH()는 문자의 개수를 반환, LENGTH()는 할당된 Byte 수 반환

CONCAT(문자열1, 문자열2...), CONCAT_WS(구분자, 문자열1, 문자열2...) - 문자열을 이어줌 / CONCAT_WS는 구분자와 함께 문자열을 이어줌

LPAD(문자열, 길이, 채울문자열), RPAD(문자열, 길이, 채울 문자열) - 문자열을 길이만큼 늘린 후에 빈곳을 채울 문자열로 채움

LTRIM(문자열), RTRIM(문자열) - 문자열의 왼쪽/오른쪽 공백을 제거 / 중간의 공백 제거 X
TRIM(문자열), TRIM(방향 자를_문자열 FROM 문자열) - TRIM은 문자열의 앞뒤 공백을 모두 없앰, LEADING(앞), BOTH(양쪽), TRAILING(뒤)
SUBSTRING(문자열, 시작위치, 길이) OR SUBSTRING(문자열 FROM 시작위치 FOR 길이) - 시작 위치부터 길이만큼 문자를 반환 / 길이 생략시 문자열의 끝까지 반환, SUBSTRING() = SUBSTR() = MID()

수학함수
ABS(숫자) - 숫자의 절대값을 계산
CEILING,FLOOR,ROUND(숫자) - 올림, 내림, 반올림
CONV(숫자, 원래진수, 변환할 진수) - 숫자를 원래 진수에서 변환할 진수로 계산
MOD(숫자1, 숫자2) OR 숫자1 % 숫자2 OR 숫자1 MOD 숫자2 0 숫자1을 숫자2로 나눈 나머지 값
POW(숫자1, 숫자2), SQRT(숫자) - 거듭제곱 값 / 제곱근 구함 (POW() = POWER())
RAND() - 0 이상 1 미만의 실수 구함
SIGN(숫자) - 숫자가 양수면 1, 0이면 0, 음수면 -1
TRUNCATE(숫자, 정수) - 숫자를 소수점을 기준으로 정수 위치까지 구하고 나머지는 버림

날짜 및 시간 함수

ADDDATE,SUBDATE(날짜, 차이) / (날짜/사간, 시간) - 날짜를 기준으로 차이를 더하거나 뺸 날짜를 구함 / (날짜/시간)을 기준으로 시간을 더하거나 뺸 결과 구함

CURDATE(), CURTIME(), NOW(), SYSDATE() - 현재 연-월-일 / 현재 시:분:초 / 현재 연-월-일 시:분:초 (NOW() = SYSDATE())

DATE(), TIME() - 연-월-일 및 시:분:초만 추출

시스템 정보 함수
USER(), DATABASE() - 현재 사용자 및 현재 선택된 DB 구함
FOUND_ROWS() - 바로 앞의 SELECT 문에서 조회된 행의 개수 구함
ROW_COUNT() - 바로 앞의 INSERT, UPDATE, DELETE 문에서 입력, 수정, 삭제된 행의 개수를 구함 (CREATE,DROP - 0, SELECT문은 -1을 반환)
VERSION() - MariaDB 버전 구함 / SLEEP(초) - 쿼리 실행을 잠깐 멈춤
```

```
MariaDB 윈도우 함수

윈도우 함수는 행과 행 사이의 관계를 쉽게 정의하기 위해서 제공되는 함수

순위 함수 : RANK(), NTILE(), DENSE_RANK(), ROW_NUMBER() [순번 또는 순위를 메기는 역할을 함]
(Partition by 이름 : 이름으로 나눈 후에 순위를 매길 때 사용)
RANK /DENSE_RANK - 순위를 매기는데 RANK는 중복이 있으면 1.2.2.4 이런 식으로 된다면 /DENSE_RANK는 1.2.2.3으로 다름
NTILE - NTILE(나눌 그룹 개수) 함수로 나누고 싶을 때 사용함

분석함수 : CUME_DIST(), LEAD(), FIRST_VALUE(), LAG(), LAST_VALUE(), PERCENT_RANK() (이동 평균, 백분율, 누계 등의 결과를 계산 할 수 있음)
- 비집계함수

LEAD는 다음 행 위치를 지정할 수 있음 (열이름도) / LAG는 이전 행 위치를 지정할 수 있음 (열이름도)
FIRST_VALUE/LAST_VALUE는 첫번재 값과 마지막 값임
CUME_DIST는 누적 백분율...
PERCENT_RANK는 0~1 사이에서 백분율로 나타냄
```

```
피벗 - 한 열에 포함된 여러 값을 출력하고 이를 여러 열로 변환하여 테이블 반환 식을 회전하고 필요하면 집계까지 수행하는 것을 말함
JSON 데이터도 MariaDB에서는 넣을 수 있음
JOIN - 두개 이상의 테이블을 묶어준다고 생각하면 편함

INNER JOIN (내부 조인)
일반적으로 가장 많이 사용되는 join / join을 할 때에는 어디서 추출하는 지 적어주는 것이 좋음 / 양쪽 테이블에 모두 내용이 잏는 것만 join되는 방식
중복을 빼기 위해서는 Distinct / exists 문을 사용하여야 함

OUTER JOIN (외부 조인)
조인의 조건에 만족되지 않은 행까지도 포함시키는 것!
LEFT / RIGHT /FULL로 나뉩니다.

CROSS JOIN / SELF JOIN

CROSS JOIN은 한쪽 테이블의 모든 행들과 다른 쪽 테이블의 모든 행을 조인시키는 기능 (두 테이블 개수를 곱한 개수)

SELF JOIN (자기 자신과 자기 자신이 조인한다는 의미)

UNION / UNION ALL / NOT IN / IN

UNION - 두 쿼리의 결과를 합침 (중복 제외) / UNION ALL - 중복 포함
NOT IN / IN (첫번째 쿼리의 결과 중에서 두번째 쿼리에 해당하는 것을 제외하기 위한 구문 / 첫번째 쿼리의 결과 중에서 두번째 쿼리에 해당하는 것만 죄회하기 위해서는 IN을 사용)

IF.. ELSE ..
IF <BOOLEAN 표현식> THEN
 sql
 ELSE
 sql
 END IF;

 Begin ... END
 Begin
    declare

    if

    else

    end if
END $$
DELIMITER ;
CALL ifProc();

CASE 문
WHILE / ITERATE/LEAVE 문
오류처리 / 동적 SQL
```
