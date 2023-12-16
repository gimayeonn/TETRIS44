# TETRIS44
오픈소스프로그래밍 고효율 팀입니다.


오픈소스코드 주소 : https://github.com/CSID-DGU/2020-2-OSSP-CP--YamiYami_Z_Z-5

License : GPLv3

python 3.6

pygame = 1.9.3

1. 목적

   기존의 테트리스 게임에 추가적인 기능을 구현하여, 더 발전된 테트리스 게임을 만들기 위함이다.

     <추가 기능>
     - AWS의 RDS와 MySQL을 이용한 회원가입/로그인 기능 구현
     - 모드별 랭킹 구현 및 랭킹 실시간 업데이트 기능 구현
     - 캐릭터 선택 기능 + 진화 구현
     - BGM 선택

3. 게임 실행 방식
   1. 현재 repository의 소스 코드를 모두 다운 또는 clone을 통해 local에 저장한다.
   2. 추가 모듈에 표기한 모듈들을 다운 받고 run.py에서 실행한다.

4. 조작 방식

   a, 왼쪽 방향키 : 블럭을 왼쪽으로 한칸 이동시킨다   
   
   d, 오른쪽 방향키 : 블럭을 오른쪽으로 한칸 이동시킨다 
   
   w, 위쪽 방향키 : 블럭을 오른쪽으로 90도 회전시킨다
   
   s, 아래쪽 방향키 : 블럭을 아래쪽으로 한칸 이동시킨다
   
   e, 스페이스바 : 블럭을 아래쪽으로 떨군다
   
   p : 게임을 일시정지한다
   
   m : 배경음악을 키고 끈다
   
   
   -기본, AI, MINI 모드에서는 방향키와 a,w,s,d, space로 블럭 조작
   
   -two hands 모드에서는 awsd와 e, 방향키와 space를 통해 각각의 블럭을 조작





## 추가 설명

> AWS 데이터베이스

  aws 프리티어를 이용하여 데이터베이스를 구성

  따라서 테스트가 필요할 경우, 본인 aws 계정으로 로그인 후 실행 

  (database_user.py 계정정보 수정)




> 회원가입

  - ID -> Enter

  - PW -> Enter

  - Sign up -> Enter




> 로그인

  - ID -> Enter

  - PW -> Enter

  - Sign in -> Enter




## 게임 화면

  ![image](https://user-images.githubusercontent.com/63901647/121522975-a88d3700-ca30-11eb-94e7-b6e424be65ff.png)

  ![image](https://user-images.githubusercontent.com/63901647/121523001-b0e57200-ca30-11eb-9714-1a189682e35c.png)

![image](https://user-images.githubusercontent.com/63901647/121523010-b478f900-ca30-11eb-8031-b0f7f8c07d95.png)

