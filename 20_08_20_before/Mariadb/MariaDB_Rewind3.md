## MariaDB 3

#### 복습 !

```
MariaDB 데이터 형식 

숫자형 / 문자형 / 날짜, 시간 데이터 / 기타 데이터 형식이 있음 

숫자형 형식은 정수 , 실수 등 숫자를 표현하며 (INT 종류와 FLOAT, REAL, DECIMAL 등이 쓰임)
부호없는 정수를 사용시에는 UNSIGNED 형식을 쓰면 굿!!

문자형 데이터에는 CHAR, VARCHAR, BINARY, TEXT형식, BLOB 형식 등이 쓰임 !! 
CHAR 형식으로 설정하는 게 INSERT/UPDATE 시에 성능이 더 좋음 !!

마리아 DB의 문자 세트는 /etc/my.cnf.d 폴더에 보통 있는데.. 클라이언트 문자 세트는 default-character-set=utf8, 서버 문자는 [mysqld] character-set-server=utf-8 형식으로 사용됨 !!

날짜 시간 데이터형식은 DATE, TIME, DATETIME, TIMESTAMP, YEAR 등이 사용 / DATE는 YYYY-MM-DD 형식으로 사용되며, TIME은 HH:MM:SS 형식으로 사용되며 YEAR은 YYYY로 사용됨 !!

기타 데이터 형식에는 GEOMETRY, JSON 형식이 있음 !

LONGTEXT, LONGBLOB => 대량의 데이터를 저장하기 위해서 사용 !

변수의 사용 !
SET @변수이름 = 변수의 값 ; --- 변수의 선언 및 값 대입 
SELECT @변수이름 ; -- 변수의 값 출력 

PREPARE 쿼리이름 FROM '쿼리문' => 쿼리 이름에 '쿼리문'을 준비만 해놓고 실행하지는 않음 

데이터형식 변환함수 => CAST(), CONVERT()를 사용함 ! 
CAST ( expression AS 데이터형식 [ (길이) ]) / CONVERT ( expression, 데이터형식 [(길이)])
MariaDB [sqldb]> select AVG(amount) AS '평균 구매 개수' FROM buyTbl;
+----------------------+
| 평균 구매 개수       |
+----------------------+
|               2.9167 |
MariaDB [sqldb]> SELECT CAST(AVG(amount) AS SIGNED INTEGER) AS '평균 구매 개수' FROM buyTbl;
+----------------------+
| 평균 구매 개수       |
+----------------------+
|                    3 |
암시적인 형변환 => 명시적인 변환은 cast(), convert 함수르 이용한 변환이지만 암시적인 변환은 데이터형식 변환 함수를 사용하지 않고 변환하는 것임 !!

Maria db 내장 함수 ! 
제어 흐름 함수 (IF, IFNULL(수식1,수식2), NULLIF(수식1, 수식2), CASE ~ WHEN ~ ELSE ~ END 등이 있음 )
IF(수식,참,거짓)=> 수식이 참 OR 거짓인지 결과에 따라 2중분기 / IFNULL(수식1,수식2) => 수식1이 NULL이 아니면 수식1 반환 / 수식1이 NULL이면 수식2가 반환 
NULLIF(수식1,수식2) =>수식 1,2가 같으면 NULL / 다르면 수식1을 반환 / CASE ~ WHEN ~ ELSE ~ END는 CASE는 연산자로 보고 다중 분기에 사용가능 / CASE가 5일 때 WHEN이 1이면 넘기고 3이면 넘기고 5일 때 THEN으로 받는 값을 받으며, 만약 해당사항이 없으면 ELSE를 받음 
문자열 함수 ( 문자열 조작 !!)
ASCII / CHART (아스키 코드값으로 돌려주거나 , 숫자의 아스키 코드에 하당하는 값에 해당하는 문자를 돌려줌 !!)
BIT_LENGTH(문자열), CHAR_LENGTH(문자열), LENGTH(문자열) => 할당된 Bit 크기 or 문자 크기 반환 / CHAR_LENGTH()는 문자의 개수를 반환하며, LENGTH()는 할당된 Byte 수를 반환함 !!
CONCAT(문자열1, 문자열2, ...), CONCAT_WS(구분자,문자열1, 문자열2 ...) => 문자열을 이어줌 !!, CONCAT_WS()는 구분자와 함께 문자열을 이어줌 !(연결해줌)

ELT(위치, 문자열,문자열2 ...) , FIELD(찾을문자열, 문자열1, 문자열2,...), FIND_IN_SET(찾을문자열, 문자열 리스트), INSTR(기준 문자열, 부분 문자열), LOCATE(부분 문자열, 기준 문자열)
=> ELT()는 위치 번째에 해당하는 문자열 반환 / FIELD()은 찾은 문자열의 위치를 찾아서 반환 , FIELD()는 매치되는 문자열이 없으면 0을 반환, FIND_IN_SET()은 찾을 문자열을 문자열 리스트에서 찾아서 위치 반환 
문자열 리스트는 (,)로 구분되어 있어야 하며, 공백은 없어야 한다. INSTR()은 기준 문자열에서 부분 문자열을 찾아서 그 시작 위치를 반환, LOCATE()는 INSTR()과 동일하지만 파라미터 순서가 반대로 되어 있음 !
SELECT ELT(2, '하나', '둘','셋'), FIELD('둘', '하나','둘','셋'), FIND_IN_SET('둘','하나,둘,셋'), INSTR('하나둘셋', '둘'), LOCATE('둘','하나둘셋');
둘                            |                                  2 |                                   2 |                            3 |                            3 |

FORMAT(숫자, 소수점자리수)=> 숫자를 소수점 아래 자릿수 까지 표현한다 => 123456.123456, 4 => 123,456,1235 라는 값으로 나오게 됨 !!

BIN,HEX,OCT(숫자) => 2진수, 16진수 , 8진수로 바꿔줌 / INSERT(기준문자열, 위치, 길이, 삽입할 문자열) => 기준 문자열의 위치부터 길이만큼을 지우고 삽입할 문자열을 넣음 !!
LEFT(문자열,길이), RIGHT(문자열,길이) => 왼쪽 또는 오른쪽에서 문자열의 길이만큼 반환함 / UPPER(문자열), LOWER(문자열) => 소->대 / 대->소 문자로 변경 !
LPAD(문자열,길이,채울 문자열), RPAD(문자열, 길이, 채울 문자열) => 문자열을 길이만큼 늘린 후에 빈 곳을 문자열로 채운다 ! 

LTRIM(문자열), RTRIM(문자열) => 문자열의 왼쪽/오른쪽 공백을 제거한다.. 중간 공백은 제거 X  
TRIM(문자열), TRIM(방향 자를_문자열 FROM 문자열) => TRIM(문자열)은 문자열의 앞뒤 공백을 모두 없앰 / TRIM(방향 자를_문자열 FROM 문자열)에서 방향은 LEADING(앞), BOTH(양쪽), TRAILING(뒤)가 나올 수 있음 !!
REPEAT(문자열, 회수) +> 문자열을 횟수만큼 반복 / REPLACE(문자열, 원래문자열, 바꿀 문자열 )=> 문자열에서 원래 문자열을 찾아서 바꿀 문자열로 바꿔줌 / REVERSE(문자열)=> 문자열의 순서를 거꾸로 만듬 !!
SPACE(길이) => 길이 만큼의 공백을 반환 / SUBSTRING(문자열, 시작위치, 길이) 또는 SUBSTRING(문자열 FROM 시작위치 FOR 길이) => 시작 위치부터 길이만큼 문자를 반환한다. 길이가 생략되며 문자열의 끝까지 반환 !!
SUBSTRING_INDEX(문자열, 구분자, 횟수) => 문자열에서 구분자가 왼졲부터 횟수 번쨰 나오면 그 이후의 오른쪾은 버림 !! 횟수가 음수면 오른족 부터 세고 왼쪽을 버림 !!

수학함수 => ABS(숫자 / 숫자의 절대값을 계산), CONV(숫자, 원래 진수, 변환할 진수 => 숫자를 원래 진수에서 변환할 진수로 계산)
ACOS(숫자), ASIN(숫자),ATAN(숫자),ATAN2(숫자1, 숫자2),SIN(숫자),COS(숫자),TAN(숫자) / CEILING(숫자), FLOOR(숫자), ROUND(숫자) => 올림, 내림, 반올림 !
DEGREES(숫자), RADIANS(숫자), PI() => 라디안 값을 각도값으로, 각도값을 라디안 값으로 변환 / PI()는 파이 값인 3.141592를 반환한다. 
MariaDB [sqldb]> SELECT DEGREES(PI()), RADIANS(180);
+---------------+-------------------+
| DEGREES(PI()) | RADIANS(180)      |
+---------------+-------------------+
|           180 | 3.141592653589793 |
EXP(X), LN(숫자), LOG(숫자), LOG(밑수, 숫자), LOG2(숫자), LOG10(숫자) => 지수 , 로그와 관련된 함수 !
MOD(숫자1, 숫자2) 또는 숫자1 % 숫자2 또는 숫자1 MOD 숫자2 => 숫자 1을 숫자2로 나눈 나머지 값을 구함 / POW(숫자1, 숫자2), SQRT(숫자) => 거듭제곱값 및 제곱근을 구함 !!
RAND() => 0 이상 1미만의 실수를 구함 만약, 'M<= 임의의 정수 <n'을 구하고 싶다면 FLOOR(m + RAND() * (n-m))을 사용하면 됨 !! 
sign(숫자) => 숫자가 양수 0, 음수인지를 구함 결과는 1,0,-1 셋 중에 하나를 반환 ! / TRUNCATE(숫자,정수) => 숫자를 소수점을 기준으로 정수 위치까지 구하고 나머지는 버림 !
ADDDATE(날짜,차이), SUBDATE(날짜, 차이) => 날짜 및 시간을 조작하는 다양한 함수를 사용할 수 있음 / ADDTIME(날짜/시간, 시간), SUBTIME(날짜/시간, 시간) => 날짜/시간을 기준으로 시간을 더하거나 뺀 결과를 구함 ! 
CURDATE(), CURTIME(), NOW(), SYSDATE() => CURDATE()는 현재 연-월-일) / CURTIME() => 시:분:초 / NOW(), SYSDATE() => 현재 '연-월-일 시:분:초'를 구함

YEAR(날짜), MONTH(날짜), DAY(날짜), HOUR(시간), MINUTE(시간), SECON(시간), MICROSECOND(시간) => 날짜 또는 시간에서 연, 월,일, 시,분,밀리초를 구함 !!
DATEDIFF(날짜1, 날짜2), TIMEDIFF(날짜1 OR 시간1 , 날짜1 OR 시간2) => DATEDIFF()는 날짜1 - 날짜2 결과 구함 / 날짜 2 에서 날짜1 까지 몇일 남았는지 확인 가능 / TIMEDIFF()는 시간1 - 시간2 결과를 구함 !

DAYOFWEEK(날짜), MONTHNAME(), DAYOFYEAR(날짜) => 용일 (1:일, 2:월~7:토) 및 1년 중 몇 번째 날짜인지를 구할 수 있음 / LAST_DAY(날짜) => 주어진 날짜의 마지막 날짜를 구함, 주로 그 달이 몇 일까지 있는지 확인할 때 사용 가능.
MAKEDATE(연도,정수) => 연도에서 정수만큼 지난 날짜를 구함 / MAKETIME(시,분,초)=> 시,분,초를 이용해서 '시:분:초'의 TIME 형식을 만듬 
PERIOD_ADD(연월, 개월수), PERIOD_DIFF(연월1, 연월2) => 연월에서 개월만큼의 개월이 지난 연월을 구함 / 연월은 YYYY OR YYYYMM 형식 사용 / PERIOD_DIFF()는 연월1- 연월2의 개월수를 구함 ! 
QUARTER(날짜) => 날짜가 4분기 중에서 몇 분기 인지를 구함 / TIME_TO_SEC(시간) => 시간을 초 단위로 구함 

USER(), DATABASE() => 현재 사ㅛㅇ자 및 현재 선택된 데이터베이스를 구함 / FOUND_ROWS() 바로 앞의 SELECT문에서 조회된 행의 개수를 구함 / ROW_COUNT() 바로 앞의 INSERT, UPDATE, DELETE 문에서 입력, 수정, 삭제된 행의 개수를 구함 / CREATE , DROP문은 0을 반환 / SELECT 문은 -1을 반환 
VERSION() => 버전 확인 / SLEEP(초) 

영문자는 1Byte , 한글은 utf-8 코드이므로 3Byte를 차지하기 때문 / 

MariaDB 윈도우 함수 
- 원도우 함수는 행과 행 사이의 관계를 쉽게 정의하기 위해서 제공되는 함수 / 
집계함수 / 비집계함수 - AVG(),COUNT(), MAX(), MIN(), STDDEV(), SUM(), VARIANCE() 등이 있음 / 비집계함수는 CUME_DIST(), DENSE_RANK(), FIRST_VALUE(), LAG(), LAST_VALUE(), LEAD(), NTH_VALUE(), NTILE(), PERCENT_RANK(), RANK(), ROW_NUMBER() 등이 있음 !!

순위 함수 
- RANK(), NTILE(), DENSE_RANK(), ROW_NUMBER() 등 4가지 순위를 표현하는 함수를 사용하면 상당히 유용할 때가 있음 ! 
<순위함수이름>() OVER(
  [PARTITION BY <partition_by_list>]
  ORDER BY <Order_by_list>)
  MariaDB [sqldb]> select ROW_NUMBER() OVER(ORDER BY height DESC) "키큰순위", name, addr, height from userTbl;
+--------------+-----------+--------+--------+
| 키큰순위     | name      | addr   | height |
+--------------+-----------+--------+--------+
|            1 | 성시경    | 서울   |    186 |
|            2 | 임재범    | 서울   |    182 |
|            3 | 이승기    | 서울   |    182 |
|            4 | 김경호    | 전남   |    179 |
|            5 | 바비킴    | 서울   |    176 |
|            6 | 은지원    | 경북   |    174 |
|            7 | 김범수    | 경남   |    173 |
|            8 | 조관우    | 경기   |    172 |
|            9 | 윤종신    | 경남   |    170 |
|           10 | 조용필    | 경기   |    166 |

각 지역별로 하고 싶다면 partition by 절을 사용하면 됩니다. 

분석 함수 => CUME_DIST(), LEAD(), FIRST_VALUE(), LAG(), LAST_VALUE(), PERCENT_RANK() 등을 분석함수라고 함 / 이동평균, 백분율, 누계 등의 결과를 알 수 있음 
LEAD() 함수에서 사용되는 인자는 열이름, 다음 행위치를 지정할 수 있음 / lAG()는 이전 행과의 차이를 구하는 것임 !

피벗 => 한 열에 포함된 여러 값을 출력하고 이를 여러 열로 변환하여 테이블 반환 식을 회전하고 필요하면 집계까지 수행하는 것을 말함 !

JSON => 키와 벨류로 이루어져 있고 JSON_OBJECT(), 나 JSON_ARRAY() 함수를 이용 가능 ! / JSON_VALID() 함수는 문자열이 JSON 형식을 만족하면 1 / 아니면 0 반환 
JSON_SEARCH() 함수는 세번 째 파라미터에 주어진 문자열을 반환  / JSON_EXTRACT()는 서치와 반대로 지정된 위치의 값을 추출 
JSON_INSERT()는 새로운 값을 추가 / JSON_REPLACE() 값을 변경 / JSON_REMOVE() 지정된 항목에 값을 삭제 

조인 => 두개 이상으 ㅣ테이블을 서로 묶어서 하나의 결과 집합으로 만들어 내는 것임 !

INNER JOIN => 양쪽에 모두 내용이 있는 것만 조인되는 방식 / OUTER JOIN은 양쪽에 내용이 있으면 당연히 조인이 되고 한쪽에만 내용이 있어도 JOIN이 되는 방식이다. 

CROSS JOIN +> 한쪽 테이블의 모든 행들과 다른 쪽 테이블의 모든 행을 조인시키는 기능 !/ 결과 개수는 두 테이블 개수를 곱한 개수가 나옴 !!
SELF JOIN==> 자기 자신과 자기 자신이 조인을 한다는 것임 !!

SQL 프로그래밍 
DELIMITER $$
CREATE PROCEDURE 스토어드 프로시저이름()
BEGIN

(SQL 프로그래밍 코딩)

END $$
DELIMITER ;
CALL 스토어드 프로시저 이름();

IF <부울 표현식> THEN
    SQL문장들1.
ELSE
    SQL문장들2
END IF;

CASE => 다중 분기문을 사용해서 IF ELSEIF ELSE END IF를 사용함 ! 그런데 CASE WHEN THEN을 이용한다면 매우 낫베드임 ! 그리고 끝나면 END CASE;를 해줌 !!

WHILE / ITERATE/LEAVE ( WHILE은 다른 프로그래밍 언어의 WHILE가 동일한 개념 )
WHILE <부울 식> DO 
     SQL 명령문들 ....
END WHILE;

ITERATE 문을 만나면 바로 WHILE 문으로 이동해서 비교 (@i <= 100)을 다시하고 leave 문을 만다면 while문을 빠져나올 수 있음 

오류처리
DECLARE 액션 HANDLER FOR 오류 조건 처리할_문장;
액션 => 오류 발생시에 행동 정의 => CONTINUE 와 EXIT => CONTINUE가 나오면 제일 뒤의 처리할_문장 부분이 처리됨 !
오류조건 => 어떤 오류를 처리할 것인지 지정 ... SQLSATE, SQLEXCEPTION, SQL WARNING, NOT FOUND 등이 올 수 있으 

처리할 문장=> 처리할 문장이 하나라면 한 문장이 나오면ㄷ 되며, 처리할 문장이 여러 개일 경우에는 BEGIN ... END로 묶을 수 있음 

동적 SQL문 => PREPARE / EXECUTE 문을 쓴다고 보ㅕㄴ .. EXECUTE는 준비된 쿼리문을 실행시키며, DEALLOCATE PREFARE는 문장을 해제해 주는 것이 바람직하는 것임! 

테이블 

제약조건 => 데이터 무결성을 지키기 위한 제한된 조건 / 특정 데이터를 입력할 때 무조건적으로 입력되는 것이 아닌 어떠한 조건을 만족했을 때 입력되도록 제약할 수 있음 ! 
(PK 제약조건 / FK 제약조건 / UNIQUE 제약조건 / CHECK 제약조건 / DEFAULT 정의 / NULL 값 허용 ) 

기본키 제약 조건은 입력되는 값은 중복되거나 NULL 값이 입력 될 수 없다는 것이다. 
(기본키를 생성하면 자동으로 클러스터형 인덱스가 생성 !/ 테이블은 기본키를 가져야 된다고 생각하자.)
SHOW KEYS FROM 테이블이름; => 테이블에 지정된 키를 확인하는 구문 !
ALTER TABLE 테이블이름 
    ADD CONSTRAINT PK_테이블네임_테이블내용
        PRIMARY KEY (테이블내용);

외래키 제약 조건 => 두 테이블 사이의 관계를 선언함으로써, 데이터의 무결성을 보장해주는 역할을 함 ! / 하나의 테이블에 다른 테이블에 의존하게 됨 ! / 외래키를 정의하는 테이블이 외래키 테이블 / 외래키에 의해서 참조가 되는 테이블을 기준 테이블이라고 생각하자 

UNIQUE 제약조건 => 중복되지 않은 유일한 값을 입력해야함. NULL 값도 허용 !
CHECK 제약 조건 => 입력되는 데이터를 점검하는 기능을 함.. 키에 조건을 지정하여 .. 제약 사항을 설정함 ..
DEFAULT 정의 => 자동으로 입력되는 기본값을 정의하는 방법 

테이블 압축 => ex) ROW_FORMAT = COMPRESSED ; (압축하도록 설정 !!)
컬럼 압축 => 압축하고자 하는 컬럼뒤에 COMPRESSED 예약어를 써주면 되며, 여러 개의 컬럼에 지정할 수 있음 !!(모든 데이터 형식이 아닌 일부 형식에만 적용 가능 )

임시테이블 => TEMPORARY TABLE로 설정하여 임시로 사용하며, 세션 내에서만 존재하며 세션이 닫히면 자동으로 삭제 됨... 생성한 클라이언트에서만 접근이 가능하며, 다른 클라이언트는 접근 X / DROP TABLE 이나 MARIA DB를 종료시에 임시 테이블이 삭제됨!

테이블 삭제는 => DROP TABLE 이름; / 수정은 ALTER TABLE 테이블 이름 구문을 이용해서 함 !!

열을 추가할 때 ADD 이름 VARCHAR(30) 등 ... 하고 DEFAULT나 NULL의 허용을 정할 수 있음 ..(일반적으론느 가장 뒤에 추가되나.. FIRST를 사용하면 가장 앞열에 .. AFTER 열이름을 사용하면 열이름 다음에 추가)
열의 삭제 => DROP COLUMN을 사용 / 열의 이름 및 데이터 형식 변경 => CHAGE COLUMN 이름 바꾸려는 이름 데이터형식 NULL 등 쓰임 .. 

열의 제약 조건을 삭제 할 때에는 PK키와 FK가 있다면 FK를 삭제하고 PK 키를 삭제해야함 ! 

뷰 - 일반 사용자 입장에서는 테이블과 동일하게 사용하는 개체다. 뷰는 한 번 생성해 놓으면 테이블이라고 생각 해도 됨 .. 
( 뷰에 쿼리를 설정하고 돌리게 되면 쿼리를 실행시켜서 값을 보여줄 수 있음 !!)
CREATE VIEW 이런 식으로 만들 수 있음 
뷰는 보안성이 좋고 복잡한 쿼리를 단순화 시킬 수 있는 장점이 있음 
CREATE OR REPLACE VIEW로 생성되어 있는 것이 있어도 오류 방지를 할 수 있다. ALTER VIEW는 뷰의 수정을 담당한다. / 여러개의 테이블이 관련되는 복합 뷰를 생성하고 데이터를 입력 할 수 있으 !!

인덱스 => 책의 알림페이지나 찾아보기 페이지라고 생각하면 매우 편할 것이다 ./ 인덱스는 검색 속도가 빨라질 수 가 있고 해당 쿼리의 부하가 줄어들 수 있다. 
그렇지만 DB의 10% 정도의 추가공간이 필요하며, 인덱스 생성시간이 걸리며, 데이터 변경 작업이 자주 일어날 경우에는 역효과가 날 수 있다 ..

인덱스는 클러스터형 인덱스와 보조 인덱스(비클러스터형 인덱스)로 나눈다고 생각하면 굿!

클러스터형 인덱스는 테이블당 한개만 생성 가능 .. 보조 인덱스는 테이블 당 여러개를 생성 할 수 있음 .. 클러스터형 인덱스는 행 데이터를 인덱스로 지정한 열에 맞춰서 자동 정렬 !!

인덱스는 테이블 컬럼(열) 단위에 생성 .. 여러 열에 하나 거나 하나의 열에 인덱스 생성도 가능 !! / 제약조건 PK OR UNIQUE를 사용하면 자종으로 인덱스가 생성 !! 
이 때 유일한 인덱스가 생성되어 있는데  그것이 클러스터형 인덱스 이다 .

UNIQUE NOT NULL 이 아닌 UNIQUE (UNIQUE NULL)로 만든 것은 보조 인덱스가 생기며, PK로 지정할 열로 데이터가 오름차순 정렬함!!

인덱스의 내부 작동 
B-tree(Balanced Tree) / 노드로 구성되어 있고 노드는 트리 구조에서 데이터가 존재하는 공간 즉 마디라고 생각하자 ... 루트노드는 상위노드 .. 리프노드는 제일 마지막에 존재하는 노드라고생각하자.. 
노드에 해당되는 것이 페이지라고 생각하고 16Kbyte 크기의 최소한의 저장단위라고 생각하자 .. 

페이지 분할 => 데이터 변경 작업시 인덱시 구성이 되면 성능이 나빠질 수 있는데.. 이 때 페이지 분할이 발생하여 그렇다.. 하나의 값을 입력하기 위해 새로운 페이지에 여러번 할당되고 페이지 분할이 발생되기 때문에 느려짐!! 

클러스터형 인덱스는 알파벳 순서 같은 찾아보기(인덱스)로 구성되어 있어 리프 레벨이 데이터 페이지라고 생각하면 된다. 보조 인덱스으 ㅣ경우 데이터 페이지를 정렬하는 것이 아니라 뒤쪽 빈 부분에 삽입하므로 .. 페이지 분할을 이뤄지지 ㅇ낳았다. 

클러스터형은 인덱스 자체의 리프 페이지가 데이터.. 데이터 입력 / 수정 / 삭제시 느려짐 .. 테이블에 1개만 생성 가능 ..
보조 인덱스의 경우 .. 별도의 페이지에 인덱스 구성 .. 리프 페이지는 데이터가 위치하는 주소값(RID)임 .. 보조 인데스는 여러 개 생성할 수 있지만 필요치않은 부분에 생성하면 느려지니 .. 참조 바람 

OLTP는 수정을 하므로 .. 인덱스는 최소로 생성이 바람직하며.. OLAP는 크게 상관 없음 ..

CREATE INDEX 인덱스 이름 ON 테이블 이름 ();으로 가능 . ALTER TABLE .. ADD INDEX / ALTER TABLE .. ADD KEY로 가능 .. 

WHERE 절에서 사용되는 열에 인덱스를 만들어야 하지만 자주 사용해야 가치가 있음 ... 데이터의 중복도가 높은 열은 인덱스를 만들어도 별 효과가 없으며.. 외래 키를 지정한 열에는 자동으로 외래 키 인덱스가 생성됨 .. JOIN에 자주 사용되는 열에는 인덱스를 생성해 주는 것이 좋음 
UID가 얼마나 자주 일어나는 지를 고려해야함 .. 사용하지 않는 인덱스는 제거한다.




```