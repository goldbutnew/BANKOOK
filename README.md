# 내 입맛대로 금융을 요리하다, BANKOOK


### 목차
1. GOAL
2. TECH STACK 
3. API
4. Prototype
5. ERD
6. 역할분담
---

### 📌 GOAL
- 금융상품 추천 서비스를 포함한 금융 상품 비교 웹 애플리케이션 구현

### 💻 TECH STACK
- front: JavaScript, Vue, Node.js
- back: Django, SQLite

### 📚 API
* Kakao Maps API
* 한국수출입은행 환율 API
* 금융감독원 API
* 대한민국 법정동 코드 조회 API (juso.dev)

### 🎨 Prototype (using Kakao Oven)
![목업](https://github.com/goldbutnew/BANKOOK/assets/149566915/b26b22fe-07b7-425e-b8f7-6cef77701015)


### ⚙ ERD (using django-extentions graph_models)
* django-extentions 라이브러리의 graph_models 패키지를 이용
* accounts 모델은 django.contrib.auth.models로부터 AbstractUser model을 import 받아서 커스텀
![my_api_model](https://github.com/goldbutnew/BANKOOK/assets/149566915/b96b6580-547b-452f-9cd5-822f6319690b)


### 👫 역할분담 (기능으로 분담)
* 이금현: 메인페이지, 근처은행검색, 자유게시판CRUD, CSS 및 UI/UX Design
* 김도훈: 회원커스터마이징, 금융상품비교, 환율계산기, 로그인 기능, 프로필페이지

### 기능