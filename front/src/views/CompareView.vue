<template>
  <div class="outer container">
    <div class="link">
      <p class="bread-crumb">
        <a href="http://localhost:5173/">홈</a> > <a href="http://localhost:5173/compare">금융상품비교</a>
      </p>
      <h3>🎁 금융상품비교</h3>
    </div>
    <hr>
    <div class="img-area">
      <a href="http://localhost:5173/compare/deposit">
        <img src="@/assets/image/deposit-icon.png" alt="" class="deposit-icon">        
      </a>
      <a href="http://localhost:5173/compare/savings">
        <img src="@/assets/image/savings-icon.png" alt="" class="savings-icon">        
      </a>
    </div>
    <button class="btn btn-light float-right mt-15 btn-sm" @click="store.getCompareData()">데이터 다운로드</button>
  </div>

    <!-- <button>예금/적금 선택 버튼</button> -->
    <!-- <li v-for="product in store.deposit"
    :key="product.id">
    공시제출월: {{ product.dcls_month }} | 
    금융회사명: {{ product.kor_co_nm }} | 
    상품명: {{ product.fin_prdt_nm }} | 
    금리: {{ product.options[0].intr_rate }}
    </li> -->

    
  
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

// import SavingsView from '@/views/SavingsView.vue';
// import DepositView from '@/views/DepositView.vue';

const store = useCounterStore()

// onMounted(() => {
//   store.getDeposit()
//   store.getSaving()
// })


</script>

<style scoped>
.outer {
  padding-top: 20px;
  padding-bottom: 20px;
}

.bread-crumb > a {
  text-decoration: none;
  color: black;
  font-size: small;
}

.img-area {
  display: flex;
  justify-content: center;
}

.savings-icon {
  margin-top: 50px;
  margin-left: 30px;
}

.deposit-icon {
  margin-top: 50px;
  margin-right: 30px;
}

</style>