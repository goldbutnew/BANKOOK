<template>
  <div>
    <div id="carouselExampleIndicators" class="carousel slide">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="@/assets/image/main1.png" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="@/assets/image/main2.png" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="@/assets/image/main3.png" class="d-block w-100" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>

    <div class="high-level-container">
      <div class="img-box">
        <div class="intro-item col-lg-4">
          <img src="@/assets/image/icon1.png" alt="">
          <div>
            <p></p>
            <p id="title">다양한 옵션을 한 곳에서!</p>
            <p>내게 필요한 예금? 적금?<br>
              당신의 재무를 책임지는 곳,<br>
              뱅쿡에서 세우는 금융 계획</p>
          </div>
        </div>

        <div class="intro-item col-lg-4">
          <img src="@/assets/image/icon2.png" alt="">
          <div>
            <p></p>
            <p id="title">금융으로 세계를 연결하다</p>
            <p>우리 집 근처 은행이 궁금해?<br>
              실시간 환율이 궁금해?<br>
              뱅쿡에서 해결하세요!</p>
          </div>
        </div>

        <div class="intro-item col-lg-4">
          <img src="@/assets/image/icon3.png" alt="">
          <div>
            <br>
            <p></p>
            <p id="title">함께 나누는 금융 고민</p>
            <p>혼자 끙끙 앓던 금융 고민?<br>
              더 이상 혼자서는 NO!<br>
              뱅쿡에서 함께하는 신나는 금융토크</p>        
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
</script>

<style scoped>

#title {
  font-weight: bolder;
}

.high-level-container {
  display: block;
  padding: 100px;
}
.img-box {
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top:  50px;
  padding-bottom: 30px;
  text-align: center;
  font-size: small;
}

img {
  width: 130px;
}

.intro-item {
  width: 450px;
  height: 280px;
  padding-left: 50px;
  padding-right: 50px;
}

.high-level-container {
  padding: 50px;
}
/* .news {
  display: block;
  justify-content: center;
  align-items: center;
  width: 100%;
  padding-right: 300px;
  padding-left: 300px;
  padding-bottom: 100px;
} */
</style>