## MariaDB 

#### 복습 !

```
데이터베이스 => Data의 집합? / DBMS  => 데이터베이스 관리 운영하는 역할 !(대용량을 관리하거나 여러 명의 사용자가 공유하는 개념!?)

데이터 무결성 => 데이터에 오류가 있으면 안됨!/ 제약조건을 가짐 !
데이터 독립성 => 크기를 변경하거나 파일의 저장소 변경하더라도 기존에 작성된 응용 프로그램은 영향을 받으면 안됨 ! So 독립적인 관계!
보안 => db는 허용된 사람이 데이터 접근이 가능해야함 !!
중복의 최소화 / 제작 및 수정이 쉽고 안전성 향상이 필요함 !!

DBMS는 계층형, 망형, 관계형, 객체지향형, 객체 관계형으로 나눔 !!
(DataBase Management System)
RDBMS 에서 DB는 테이블이라 불리는 최소 단위로 구성 !(하나 이상의 열 !)
모든 데이터는 테이블에 저장되므로 RDBMS에서 가장 중요한 역할 !!(테이블 ! )
테이블의 관계는 기본키와 외래키를 맺어주므로 연관이 되옴 !

SQL = DB 언어 ! (DBMS 제작 회사와 독립적 / 다른 시스템으로 이식성이 좋음 / 표준이 계속 발전 / 대화식 언어 / 분산형 클라이언트/서버 구조)

열 (컬럼, 필드) / 행(로우, 레코드) 

(db 생성 -> 테이블 생성 -> 데이터 입력 -> 데이터 조회/활용 ) -> 테이블 외에 db 개체의 활용 -> 데이터 백업 관리  / 응용프로그램에서 구축된 데이터 활용 (웹서비스 / 어플리케이션)

인덱스 => 찾아보기(색인)과 같은 개념 !  / 책의 내용 중 특정 단위를 찾고자 할 때 유용함 

데이터베이스 튜닝 => 데이터 베이스 성능을 향상시키거나 응답하는 시간을 단축시키는 것 !/ 쿼리의 응답을 줄이기 위해서 가장 집중적으로 보는 중 하나가 인덱스 임 !!

뷰 -> 가상의 테이블이라고 생각하자 / 뷰는 실제 데이터를 가지고 있지 않음 

스튜어드 프로시저 => 마리아 디비에서 제공해주는 프로그래밍 기능 ! / procedure로 묶어서 sql 쿼리문을 만들고 CALL로 부를 수 있음 !!

트리거 => 테이블에 부착되서 테이블에 insert / update 또는 delete 작업이 발생되면 실행되는 코드임 !! trggier name 형식으로 사용됩니다.

데이터베이스 모델링 
작업이나 사물들을 DBMS의 DataBase 개체로 옮기기 위한 과정 ! 
크게 개념적 / 논리적 / 물리적 모델링으로 나눌 수 있음 ( 개념적 모델링은 주로 업무 분석 단계 / 논리적 모델링은 업무 분석 후반부와 시스템 설계의 전반부 걸쳐서 진행 / 물리적 모델링은 시스템 설계의 후반부에 주로 진행 )

SQL 기본 

SELECT 문 
SELECT FROM  / SELECT 열이름 FROM 테이블이름 WHERE 조건 
USE 구문 / USE DATABASE NAME; /

SELECT * FROM table_name;
maria db에서는 -- (주석으로 처리 /) / 여러 열 주석은 /* */ 입니다.

DB 확인 SHOW DATABASES;
TABLE 확인 SHOW tables;

테이블에 열이 있는 지 확인 desc table_name;
```

```
ex1) 
create databases sqldb;
use sqldb;

Create TABLE userTbl
( userID CHAR(8) NOT NULL PRIMARY KEY,
  name VARCHAR (10) NOT NULL,
  birthYear INT NOT NULL,
  addr CHAR(2) NOT NULL,
  mobile1 CHAR(3),
  Mobile2 CHAR(8),
  height SMALLINT,
  mDate DATE 
);

CREATE TABLE buyTbl
( num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  userID CHAR(8) NOT NULL,
  prodName CHAR(6) NOT NULL,
  groupName CHAR(4),
  price INT NOT NULL,
  amount SMALLINT NOT NULL,
  FOREIGN KEY (userID) REFERENCES userTbl(userID) -- 외래 키 지정
  );

INSERT INTO userTbl VALUES ('LSG', N'이승기', 1987, N'서울', '011', '11111111', 182, '2008-8-8');
INSERT INTO userTbl VALUES ('KBS', N'김범수', 1979, N'경남', '011', '22222222', 173, '2012-4-4');
INSERT INTO userTbl VALUES ('KKH', N'김경호', 1971, N'전남', '019', '33333333', 179, '2007-7-7');
INSERT INTO userTbl VALUES ('JYP', N'조용필', 1950, N'경기', '011', '44444444', 166, '2009-4-4');
INSERT INTO userTbl VALUES ('SSK', N'성시경', 1979, N'서울', NULL, NULL, 186, '2013-12-12');
INSERT INTO userTbl VALUES ('LJB', N'임재범', 1963, N'서울', '016', '66666666', 182, '2009-9-9');
INSERT INTO userTbl VALUES ('YJS', N'윤종신', 1969, N'경남', NULL, NULL, 170, '2005-5-5');
INSERT INTO userTbl VALUES ('EJW', N'은지원', 1972, N'경북', '011', '88888888', 174, '2014-3-3');
INSERT INTO userTbl VALUES ('JKW', N'조관우', 1965, N'경기', '018', '99999999', 172, '2010-10-10');
INSERT INTO userTbl VALUES ('BBK', N'바비킴', 1973, N'서울', '010', '00000000', 176, '2013-5-5');

INSERT INTO buyTbl VALUES(NULL, 'KBS', N'운동화', NULL, 30, 2);
INSERT INTO buyTbl VALUES(NULL, 'KBS', N'노트북', N'전자', 1000, 1);
INSERT INTO buyTbl VALUES(NULL, 'JYP', N'모니터', N'전자', 200, 1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', N'모니터', N'전자', 200, 5);
INSERT INTO buyTbl VALUES(NULL, 'KBS', N'청바지', N'의류', 50, 3);
INSERT INTO buyTbl VALUES(NULL, 'BBK', N'메모리', N'전자', 80, 10);
INSERT INTO buyTbl VALUES(NULL, 'SSK', N'책', N'서적', 15, 5);
INSERT INTO buyTbl VALUES(NULL, 'EJW', N'책', N'서적', 15, 2);
INSERT INTO buyTbl VALUES(NULL, 'EJW', N'청바지', N'의류', 50, 1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', N'운동화', NULL, 30, 2);
INSERT INTO buyTbl VALUES(NULL, 'EJW', N'책', N'서적', 15, 1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', N'운동화', NULL, 30, 2);

SELECT * FROM userTbl;
SELECT * FROM buyTbl;

여기서는 userID를 Primary Key로 지정했기 때문에 자동으로 클러스터형 인덱스가 생성되어 입력 시에 userID열로 정렬되기 때문 !

```


```
SELECT 필드이름 FROM 테이블이름 WHERE 조건식; / USE sqlDB; SELECT * FROM userTbl where name = '김경호';
KKH    | 김경호    |      1971 | 전남   | 019     | 33333333 |    179 | 2007-07-07 |

SELECT userID, Name FROM userTbl WHERE birthYear >= 1970 AND height >= 182;
>= , <= >, <, = , <>, >, != / not , and , or 등이 쓰임 !!

SELECT Name, height FROM userTbl WHERE height >= 180 AND height <= 183;
| Name      | height |
+-----------+--------+
| 임재범    |    182 |
| 이승기    |    182 |
=> SELECT Name, height FROM UserTbl WHERE height BETWEEN 180 AND 183;

SELECT Name, addr FROM userTbl WHERE addr='경남' OR addr ='전남' OR addr='경북';
| Name      | addr   |
+-----------+--------+
| 은지원    | 경북   |
| 김범수    | 경남   |
| 김경호    | 전남   |
| 윤종신    | 경남   |
SELECT Name, addr from userTbl WHERE addr IN ('경남','전남','경북'); # 이산적인 값을 위해 IN()을 사용할 수 있음 

SELECT Name, height FROM userTbl WHERE name LIKE '김%'; # %은 무엇이든 허용 하며, 김%는 김이 제일 앞글자 인 것을 추출 !
| Name      | height |
+-----------+--------+
| 김범수    |    173 |
| 김경호    |    179 |
SELECT Name, height FROM userTbl WHERE name LIKE '_종신'; # _는 한 글자이며, _종신은 종신 앞에 아무거나 한글자가 올 수 있음 !!
| Name      | height |
+-----------+--------+
| 윤종신    |    170 |

# 추가적으로 _재% 이면 앞에는 1글자가 아무거나 뒤에는 몇글자든 아무거나 오는 사람을 쓸 수 있음 ! (EX) 임재범 / 수재입니다. / 기재바람)

ANY / ALL / SOME / SubQuery

SELECT Name, height FROM userTbl WHERE height > (SELECT height FROM userTbl WHERE Name = '김경호');
| Name      | height |
+-----------+--------+
| 임재범    |    182 |
| 이승기    |    182 |
| 성시경    |    186 |

height는 179를 돌려주게 되며 where height > 179가 되는 식이 완성됨 !!

ANY는 서브쿼리의 여러 개의 결과 중 한 가지만 만족해도 되지만, ALL은 서브쿼리의 여러 개의 결과를 모두 만족시켜야한다 ! / SOME은 ANY와 덩일한 의미이다.!
만약 173보다 크거나 170보다 큰 조건이라면 ANY는 170보다 큰사람 / ALL은 173보다 큰 사람이 될 것이다!

SELECT Name, height FROM userTbl WHERE height IN (SELECT height FROM userTbl WHERE addr ='경남');
| Name      | height |
+-----------+--------+
| 김범수    |    173 |
| 윤종신    |    170 |

ORDER BY => 원하는 순서대로 정렬하여 출력해주는 것 (기본적으로 값을 넣어주지 않으면 오름차순(ASC)으로 정렬 가장 빠른 값부터 나오게 됨 ! / 내림차순은 DESC를 넣어줘야 함 !)
SELECT Name, mDate FROM userTbl ORDER BY mDate;
| Name      | mDate      |
+-----------+------------+
| 윤종신    | 2005-05-05 |
| 김경호    | 2007-07-07 |
| 이승기    | 2008-08-08 |
| 조용필    | 2009-04-04 |
| 임재범    | 2009-09-09 |
| 조관우    | 2010-10-10 |
| 김범수    | 2012-04-04 |
| 바비킴    | 2013-05-05 |
| 성시경    | 2013-12-12 |
| 은지원    | 2014-03-03 |

DISTINCT(중복된 것은 하나만 남김!)
SELECT DISTINCT addr FROM userTbl;
| addr   |
+--------+
| 서울   |
| 경북   |
| 경기   |
| 경남   |
| 전남   |

LIMIT 출력하는 개수를 제한 !
EX) Limit 5면 5개만 출력이 됨 !
Limit 0, 5 # LIMIT 5 OFFSET 0 과 동일하며  0 부터 시작 5개 까지 라고 할 수 있음 !! --,

CREATE TABLE ... SELECT (ㅔ이블 복사 구문 )
CREATE TABLE newtable (SELECT 복사할열 FROM 기존 테이블 )

CREATE TABLE buyTbl2 (SELECT * FROM buyTbl);
SELECT * FROM buyTbl2;
| num | userID | prodName  | groupName | price | amount |
+-----+--------+-----------+-----------+-------+--------+
|   1 | KBS    | 운동화    | NULL      |    30 |      2 |
|   2 | KBS    | 노트북    | 전자      |  1000 |      1 |
|   3 | JYP    | 모니터    | 전자      |   200 |      1 |
|   4 | BBK    | 모니터    | 전자      |   200 |      5 |
|   5 | KBS    | 청바지    | 의류      |    50 |      3 |
|   6 | BBK    | 메모리    | 전자      |    80 |     10 |
|   7 | SSK    | 책        | 서적      |    15 |      5 |
|   8 | EJW    | 책        | 서적      |    15 |      2 |
|   9 | EJW    | 청바지    | 의류      |    50 |      1 |
|  10 | BBK    | 운동화    | NULL      |    30 |      2 |
|  11 | EJW    | 책        | 서적      |    15 |      1 |
|  12 | BBK    | 운동화    | NULL      |    30 |      2 |

CREATE TABLE buyTbl3 (SELECT userID, prodName FROM buyTbl);
SELECT * FROM buyTbl3;
| userID | prodName  |
+--------+-----------+
| KBS    | 운동화    |
| KBS    | 노트북    |
| JYP    | 모니터    |
| BBK    | 모니터    |
| KBS    | 청바지    |
| BBK    | 메모리    |
| SSK    | 책        |
| EJW    | 책        |
| EJW    | 청바지    |
| BBK    | 운동화    |
| EJW    | 책        |
| BBK    | 운동화    |

GRUOP BY & Having 

SELECT userID, sum(amount) FROM buyTbl GROUP BY userID;
| userID | sum(amount) |
+--------+-------------+
| BBK    |          19 |
| EJW    |           4 |
| JYP    |           1 |
| KBS    |           6 |
| SSK    |           5 |
SELECT userID AS '사용자 아이디', SUM(amount) AS '총 구매 개수' FROM buyTbl GROUP BY userID;
| 사용자 아이디       | 총 구매 개수      |
+---------------------+-------------------+
| BBK                 |                19 |
| EJW                 |                 4 |
| JYP                 |                 1 |
| KBS                 |                 6 |
| SSK                 |                 5 |

집계 함수 
SUM / AVG(평균) / MIN 최소값 / MAX 최대값 / COUNT 행의 개수 / COUNT(DISTINCT) => 행의 개수를 샘 (중복은 1개만 인정) / STDEV 표준편차를 구함 / VAR_SAMP 분산을 구함 

SELECT Name, MAX(height), MIN(height) FROM userTbl GROUP BY Name;
| Name      | MAX(height) | MIN(height) |
+-----------+-------------+-------------+
| 김경호    |         179 |         179 |
| 김범수    |         173 |         173 |
| 바비킴    |         176 |         176 |
| 성시경    |         186 |         186 |
| 윤종신    |         170 |         170 |
| 은지원    |         174 |         174 |
| 이승기    |         182 |         182 |
| 임재범    |         182 |         182 |
| 조관우    |         172 |         172 |
| 조용필    |         166 |         166 |

SELECT Name, height FROM userTbl WHERE height = (SELECT MAX(height) FROM userTbl) OR height = (SELECT MIN(height) FROM userTbl);
| Name      | height |
+-----------+--------+
| 조용필    |    166 |
| 성시경    |    186 |

Having 절 (group 절 뒤에 나와야 돼!)
SELECT userID AS '사용자', SUM(price*amount) AS '총구매액' FROM buyTbl GROUP BY userID HAVING SUM(price*amount) > 1000 ORDER BY SUM(price*amount);
| 사용자    | 총구매액     |
+-----------+--------------+
| KBS       |         1210 |
| BBK       |         1920 |

ROLLUP ( 총합 또는 중간 합계가 필요하다면 GROUP BY 절과 함께 WITH ROLLUP을 사용하면 되옵니다.)
SELECT groupName, SUM(price * amount) AS '비용' FROM buyTbl GROUP BY groupName WITH ROLLUP;
| groupName | 비용   |
+-----------+--------+
| NULL      |    180 |
| 서적      |    120 |
| 의류      |    200 |
| 전자      |   3000 |
| NULL      |   3500 |
모든 값을 더한건 null + 나머지 라 NULL이 되옵니다.!
```
