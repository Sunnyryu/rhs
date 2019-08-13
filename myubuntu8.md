## My Ubuntu

#### db와 놀아보자!!

```
우분투와 db 연결을 활용하기 전에 db 용어 이해하기 !

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
필수 SQL 문

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
DELETE FROM 테이블이름 WHERE 조건; - 레코드 삭제
UPDATE 테이블이름 SET 필드이름=수정할값 ... WHERE 조건; - 레코드 수정

SELECT 필드이름1, 2 ... FROM 테이블이름 WHERE 조건; - 테이블 조회
```
