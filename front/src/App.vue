<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid my-auto">
        <!-- <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-piggy-bank my-auto" viewBox="0 0 16 16">
          <path d="M5 6.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0m1.138-1.496A6.613 6.613 0 0 1 7.964 4.5c.666 0 1.303.097 1.893.273a.5.5 0 0 0 .286-.958A7.602 7.602 0 0 0 7.964 3.5c-.734 0-1.441.103-2.102.292a.5.5 0 1 0 .276.962"/>
          <path fill-rule="evenodd" d="M7.964 1.527c-2.977 0-5.571 1.704-6.32 4.125h-.55A1 1 0 0 0 .11 6.824l.254 1.46a1.5 1.5 0 0 0 1.478 1.243h.263c.3.513.688.978 1.145 1.382l-.729 2.477a.5.5 0 0 0 .48.641h2a.5.5 0 0 0 .471-.332l.482-1.351c.635.173 1.31.267 2.011.267.707 0 1.388-.095 2.028-.272l.543 1.372a.5.5 0 0 0 .465.316h2a.5.5 0 0 0 .478-.645l-.761-2.506C13.81 9.895 14.5 8.559 14.5 7.069c0-.145-.007-.29-.02-.431.261-.11.508-.266.705-.444.315.306.815.306.815-.417 0 .223-.5.223-.461-.026a.95.95 0 0 0 .09-.255.7.7 0 0 0-.202-.645.58.58 0 0 0-.707-.098.735.735 0 0 0-.375.562c-.024.243.082.48.32.654a2.112 2.112 0 0 1-.259.153c-.534-2.664-3.284-4.595-6.442-4.595zM2.516 6.26c.455-2.066 2.667-3.733 5.448-3.733 3.146 0 5.536 2.114 5.536 4.542 0 1.254-.624 2.41-1.67 3.248a.5.5 0 0 0-.165.535l.66 2.175h-.985l-.59-1.487a.5.5 0 0 0-.629-.288c-.661.23-1.39.359-2.157.359a6.558 6.558 0 0 1-2.157-.359.5.5 0 0 0-.635.304l-.525 1.471h-.979l.633-2.15a.5.5 0 0 0-.17-.534 4.649 4.649 0 0 1-1.284-1.541.5.5 0 0 0-.446-.275h-.56a.5.5 0 0 1-.492-.414l-.254-1.46h.933a.5.5 0 0 0 .488-.393zm12.621-.857a.565.565 0 0 1-.098.21.704.704 0 0 1-.044-.025c-.146-.09-.157-.175-.152-.223a.236.236 0 0 1 .117-.173c.049-.027.08-.021.113.012a.202.202 0 0 1 .064.199z"/>
        </svg> -->
        <RouterLink to="/" class="nav-link active fs-4 fw-bold my-auto" aria-current="page" href="#">
          BANKOOK
        </RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-between" id="navbarNavAltMarkup">
          <ul class="navbar-nav">
            <p class="my-auto">　　</p>
            <RouterLink :to="{name: 'compare'}" class="nav-link my-auto">금융상품비교</RouterLink> 
            <RouterLink :to="{name: 'exchange'}" class="nav-link my-auto">환율계산기</RouterLink> 
            <RouterLink :to="{name: 'map'}" class="nav-link my-auto">근처은행검색</RouterLink> 
            <RouterLink :to="{name: 'community'}" class="nav-link my-auto">자유게시판</RouterLink>
          </ul>
          <hr>
          <ul class="navbar-nav">
            <RouterLink v-if="!store.isLogin" :to="{name: 'signup'}" class="nav-link my-auto">회원가입</RouterLink>
            <RouterLink v-if="!store.isLogin" :to="{name: 'login'}" class="nav-link my-auto">로그인</RouterLink>
            <RouterLink v-if="store.isLogin" :to="{name: 'main'}" class="nav-link my-auto" @click="logout">로그아웃</RouterLink>
            <RouterLink v-if="store.isLogin" :to="{name: 'profile'}" class="nav-link my-auto">유저프로필</RouterLink>
          </ul>
        </div>
      </div>
    </nav>

    
    <div class="main-view">
      <RouterView />
    </div>
    <footer>
      <div class="container">
        <p style="font-weight: bold;">(주)BANKOOK</p>
        대표: 이금현, 김도훈 | 사업자등록번호: 202-31-12411 | 통신판매업신고: 2023-서울강남-1124<br>
        E-mail: hello@bankook.com | 주소: 서울특별시 강남구 역삼동 테헤란로 212 멀티캠퍼스<br>
        내 입맛대로 금융을 요리하다, BANKOOK!<br>
      </div>
    </footer>
  </div>
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const logout = () => {
  store.token = null
  store.userInfo = null
}


</script>

<style scoped>
/* Google Fonts 링크 추가 */
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700&display=swap');

body {
  font-family: 'Nanum Gothic', sans-serif;
}

.container {
  padding-top: 20px;
  padding-bottom: 20px;
}

#wrap{
	min-height: 100%;
	position: relative;
}

.main-view{    
  display: flex;
  justify-content: center;
  /* align-items: center; */
  /* max-width: 80%; */
  /* margin: 0 auto; */
  /* height: 100vh; */
}

footer{
  /* margin-top: 50px; */
  /* padding-top: 20px; */
  padding-bottom: 20px;
	bottom: 0px;
	position: relative;
  font-size: small;
  width: 100%;
	height: 100%;
	background-color:rgb(238, 238, 238);
}

html {
  scroll-behavior: smooth;
}

a {
  text-decoration: none;
  color: black 
}

</style>