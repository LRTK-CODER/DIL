# De-Identification Library
[![codecov](https://codecov.io/gh/LRTK-CODER/DIL-Project/branch/main/graph/badge.svg?token=OC4ELDAQQF)](https://codecov.io/gh/LRTK-CODER/DIL-Project)

## DIL이란?
빅데이터, AI 등 다양한 융·복합 산업에서의 데이터 이용 수요가 급증하고 있다.<br>
데이터 활용의 핵심인 가명 정보 활용에 대한 법적 근거가 마련되어 체계적인 데이터 활용 기반(가명처리 기술·절차·관리체계 등)이 조성됐다.

하지만 가명처리 기술을 구현할 대표적인 파이썬 라이브러리가 없다.<br>
이에 가명처리 기술을 구현하기 손쉽게 사용할 수 있는 라이브러리를 제작하여 개인정보 보호에 이바지하고자 개발하기로 했다.

## 사용된 오픈소스
- pandas
- pycryptodomex
- pyope
- pyffx

## 구현한 기술
### 삭제기술
- 일반 삭제
- 부분 삭제
- 행 항목 삭제
- 로컬 삭제
- 마스킹
- 주소 부분 삭제

### 통계도구
- 총계처리
    - 평균값
    - 최댓값
    - 최솟값
    - 최빈값
    - 중간값
- 부분총계
    - 평균값
    - 최댓값
    - 최솟값
    - 최빈값
    - 중간값

### 일반화
- 일반 라운딩
- 랜덤 라운딩
- 로컬 일반화
- 문자데이터 범주화

### 암호화
- 양방향
    - AES-256
- 일방향
    - SHA-256
- 순서보존 암호화
- 형태보존 암호화

### 무작위화
- 잡음 추가
- 순열(치환)
    - 전체


### 기타기술
- 표본추출
- 해부화

---

# DIL 기여
모든 버그 보고서, 버그 수정, 문서 개선, 로직 개선 및 아이디어를 환영합니다.<br>
기여 방법에 대한 자세한 개요는 기여 가이드에서 참고하시길 바랍니다.

## 개인정보 보호 기술 참고 자료
- [개인정보 비식별 조치 가이드라인](https://www.kisa.or.kr/public/laws/laws2_View.jsp?cPage=1&mode=view&p_No=282&b_No=282&d_No=3&ST=T&SV=)
- [보건의료 데이터 활용 가이드라인](http://www.mohw.go.kr/react/al/sal0101vw.jsp?PAR_MENU_ID=04&MENU_ID=040101&CONT_SEQ=363309&page=1)
- [가명정보 처리 가이드라인](https://www.pipc.go.kr/np/default/page.do?mCode=D040010000#LINK)
- [의료데이터 활용을 위한 개인정보 비식별화 기술 및 프로그램 동향](https://www.khidi.or.kr/board/view?pageNum=1&rowCnt=10&no1=1&linkId=48762098&menuId=MENU01783&maxIndex=00487620989998&minIndex=00487620989998&schType=1&schText=%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4&schStartDate=&schEndDate=&boardStyle=&categoryId=&continent=&country=)
