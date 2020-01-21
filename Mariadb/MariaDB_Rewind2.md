## MariaDB 2

#### 복습 !

```
SQL의 분류 

DML (데이터 조작 언어 - 선택/삽입/수정/삭제 하는데 사용되는 언어!)

SELECT / INSERT / UPDATE/ DELETE / Transaction 도 DML임 !!
트랜잭션이란 쉽게 표현하면, 테이블의 데이터를 변경(입력/수정/삭제) 할 때 실제 테이블에 완전히 적용 X, 임시로 적용시키는 것! 

DDL(데이터 정의 언어 - DB, Table, view, index 등의 db 개체를 생성/삭제/변경 하는 역할을 함 ! CREATE/DROP/ALTER / DDL은 트랜잭션은 발생시키지 않음 / ROLLBACK이나 COMMIT을 시킬 수 없음 ! / 실행 즉시 DB에 적용 !)

DCL (데이터 제어 언어로 권한을 부여하거나 뺴앗을 때 주로 사용하는 구문, GRANT/REVOKE/DENY 등이 해당함!)

INSERT => 테이블 데이터 삽입 / INSERT [INTO] TABLE[(열1, 열2 ...)] VALUES (값1, 값2 ...) 

열이 있는데 생략시 NULL이 들어갑니다 ..

AUTO_INCREMENT => 해당 열이 없다고 생각하고 입력/ 오토 인크레먼트는 자동으로 1부터 증가하는 값을 입력 / 지정시 PK나 UNIQUE로 지정해 줘야함 !/ 데이터 형은 숫자 형식만 사용 가능 !

ALTER TABLE testTBL2 AUTO_INCREMENT=100;
INSERT INTO testTBL2 VALUES (NULL, '아이', 23);
이렇게 되면 NULL에 100이 들어가게 됨! 

증가값을 지정하려면 서버 변수인 @@auto_increment_increment 변수를 변경하면 하면 됩니다. (ex) SET @@auto_increment_increment=3; 3씩 증가하게 됨!! )

대량의 샘플 데이터를 생성할 경우 INSERT INTO 테이블명 (열이름1, 열이름2, ...)
SELECT 문; 을 사용할 수 있음 (이 때 SELECT 문의 결과 열의 개수 = INSERT 할 테이블의 열 개수 !!)

그리고 한번에 INSERT를 하기 위해서 VALUES 들어갈 것을 ,로 끊어서 입력 가능 !!

UPDATE (데이터의 수정)
UPDATE 테이블 이름 SET 열1=값1, 열2=값2 ... WHERE 조건 ;
MariaDB [sqldb]> update buyTbl2 SET price = price * 1.5;
Query OK, 12 rows affected (0.003 sec)
Rows matched: 12  Changed: 12  Warnings: 0

DELETE (데이터의 삭제)
DELETE FROM 테이블이름 WHERE 조건;
조건 뒤에 LIMIT 숫자;를 붙어주면 상위 숫자건 만큼 삭제가 됨!

DML DELETE로 삭제할 경우 트랜잭션 로그를 기록하는 작업으로 인해 affected rows가 표시되며 drop은 테이블 자체를 삭제하기에 트랜잭션 발생 x / Truncate 문도 결과는 delete와 동일하지만 Truncate는 트랙잭션 로그를 기록 x 

조건부 데이터 입력, 변경 

ex) 
USE sqlDB;
CREATE TABLE memberTbl (SELECT userID, name, addr FROM userTbl LIMIT 3);
ALTER TABLE memberTbl ADD CONSTRAINT pk_memberTbl PRIMARY KEY (userID); -- PK 지정  / userID가 값으면 제약조건으로 인해서 에러 발생 !
SELECT * FROM memberTbl;
| userID | name      | addr   |
+--------+-----------+--------+
| BBK    | 바비킴    | 서울   |
| EJW    | 은지원    | 경북   |
| JKW    | 조관우    | 경기   |
Query OK, 0 rows affected, 1 warning (0.026 sec)
Records: 0  Duplicates: 0  Warnings: 1

에러가 발생 

이 때는 insert ignore 문으로 넣으면 잘 들어감 
INSERT IGNORE INTO memberTbl VALUES('BBK', '바비킴', '미국');
INSERT IGNORE INTO memberTbl VALUES('SJH', '서장훈', '서울');
INSERT IGNORE INTO memberTbl VALUES('HJY', '현주엽', '경기');
| userID | name      | addr   |
+--------+-----------+--------+
| BBK    | 바비킴    | 서울   |
| EJW    | 은지원    | 경북   |
| HJY    | 현주엽    | 경기   |
| JKW    | 조관우    | 경기   |
| SJH    | 서장훈    | 서울   |
기존의 겹치는 것은 추가 되지 않고 나머지는 문제 없이 삽입이 됨 !

INSERT INTO memberTbl VALUES('BBK', '바비킴짱', '미국') ON DUPLICATE KEY UPDATE name='바비킴짱', addr='미국';
| userID | name         | addr   |
+--------+--------------+--------+
| BBK    | 바비킴짱     | 미국   |
| EJW    | 은지원       | 경북   |
| HJY    | 현주엽       | 경기   |
| JKW    | 조관우       | 경기   |
| SJH    | 서장훈       | 서울   |
DUPLICATE KEY UPDATE는 기본키가 중복되면 데이터 수정!

WITH / CTE 
WITH절은 CTE(일반 테이블 표현을 위한 구문!)을 표현하기 위한 구문 / CTE는 기존의 뷰, 파생 테이블, 임시 테이블 등으로 사용되던 것을 대신 할 수 있었음 !!

CTE는 비재귀적 / 재귀적 CTE 두가지가 있음 

비재귀적 CTE => 단순한 형태, 복잡한 쿼리 문장을 단순화 시키는데 적합하게 사용 
WITH CTE_테이블이름(열이름)
AS 
( <쿼리문>
)
SELECT 열이름 FROM CTE_테이블이름;
ORDER 문을 사용할 때 CTE를 사용해보자
WITH cte(userid, total)
AS
(SELECT userid, SUM(price*amount)
FROM buyTbl GROUP BY userID)
SELECT * FROM cte ORDER BY total DESC;
| userid | total |
+--------+-------+
| BBK    |  1920 |
| KBS    |  1210 |
| JYP    |   200 |
| EJW    |    95 |
| SSK    |    75 |
cte는 실존하는 테이블이 아니라 WITH 문으로 만든 SELECT 결과이며 , AS( SELECT 문에서 조회하는 열과 WITH cte(..'과 개수는 일치해야함 !!)
#여기서는 WITH 문 2개 / SELECT 문 2개로 결과가 같다!


WITH
cte1 (컬럼들)
AS (cte1의 쿼리문),
   cte2 (컬럼들)
      AS (cte2의 쿼리문),
      cte3 (컬럼들)
        AS (cte3의 쿼리문)
select * from [cte1 or cte2 or cte3]

주의할 점은 cte3의 쿼리문에서는 cte1, cte2를 참조할 수 있지만 cte1의 쿼리문이나 cte2의 쿼리문에서는 cte3 쿼리문의 cte3를 참조할 수 없음 !!
정의가 되어있어야 참조가능 !!
```
