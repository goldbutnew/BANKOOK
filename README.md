# 내 입맛대로 금융을 요리하다, BANKOOK

## 목차
1. [GOAL](#-goal)
2. [TECH STACK](#-tech-stack)
3. [API](#-api)
4. [Prototype](#-prototype-kakao-oven)
5. [ERD](#-erd-django-extentions-graph_models)
6. [역할분담](#-역할분담-기능으로-분담)
7. [서비스 화면](#-서비스-화면 )

<br>

---

<br>

## 📌 GOAL
- 금융상품 추천 서비스를 포함한 금융 상품 비교 웹 애플리케이션 구현

<br>

## 💻 TECH STACK
- front: JavaScript, Vue, Node.js
- back: Django, SQLite

<br>

## 📚 API
* Kakao Maps API
* 한국수출입은행 환율 API
* 금융감독원 API
* 대한민국 법정동 코드 조회 API (juso.dev)

<br>

## 🎨 Prototype (Kakao Oven)
![목업](https://github.com/goldbutnew/BANKOOK/assets/149566915/b26b22fe-07b7-425e-b8f7-6cef77701015)

<br>

## ⚙ ERD (django-extentions graph_models)
* django-extentions 라이브러리의 graph_models 패키지를 이용
* accounts 모델은 django.contrib.auth.models로부터 AbstractUser model을 import 받아서 커스텀
![my_api_model](https://github.com/goldbutnew/BANKOOK/assets/149566915/b96b6580-547b-452f-9cd5-822f6319690b)

<br>

## 👫 역할분담 (기능으로 분담)
* 이금현: 메인페이지, 근처은행검색, 자유게시판CRUD, CSS 및 UI/UX Design
* 김도훈: 회원커스터마이징, 금융상품비교, 환율계산기, 로그인 기능, 프로필페이지

<br>

## 🎙 서비스 화면
* 메인페이지
  <table>
    <tr>
      <td>
        <img src="img/bankook_main.png" width="100%" />
      </td>
    </tr>
  </table>

* 금융상품비교
  <table>
    <tr>
      <td>
        <img src="img/bankook_compare.png" width="100%" />
      </td>
      <td>
        <img src="img/bankook_compare_deposit.png" width="100%" />
      </td>
    </tr>
    <tr>
      <td>
        <img src="img/bankook_compare_saving.png" width="100%" />
      </td>
      <td>
        <img src="img/bankook_compare_join.png" width="100%" />
      </td>
    </tr>
  </table>

* 환율계산기
  <table>
    <tr>
      <td>
        <img src="img/bankook_exchange.png" width="100%" />
      </td>
    </tr>
  </table>

* 근처은행검색
  <table>
    <tr>
      <td>
        <img src="img/bankook_map.png" width="100%" />
      </td>
    </tr>
  </table>

* 자유게시판
  <table>
    <tr>
      <td>
        <img src="img/bankook_community.png" width="100%" />
      </td>
      <td>
        <img src="img/bankook_community_create.png" width="100%" />
      </td>
    </tr>
    <tr>
      <td>
        <img src="img/bankook_community_detail.png" width="100%" />
      </td>
      <td>
        <img src="img/bankook_community_comment.png" width="100%" />
      </td>
    </tr>
  </table>

* 회원 정보 관련
  <table>
    <tr>
      <td>
        <img src="img/bankook_user.png" width="100%" />
      </td>
    </tr>
    <tr>
      <td>
        <img src="img/bankook_user_join.png" width="100%" />
      </td>
    </tr>
    <tr>
      <td>
        <img src="img/bankook_user_recommend.png" width="100%" />
      </td>
    </tr>
  </table>
