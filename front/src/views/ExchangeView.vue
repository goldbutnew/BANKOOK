<template>
  <div class="outer container">
    <div class="link">
      <p class="bread-crumb">
        <a href="http://localhost:5173/">홈</a> > <a href="http://localhost:5173/exchange">환율계산기</a>
      </p>
      <h3>📈 환율계산기</h3>
    </div>
    <hr>

    <div class="calc">
      <p class="date">기준일시: {{ dateString }} {{ timeString }}</p>
      <div action="#" class="input-group">
        <select v-model="exc.selectedExchangeId" @change="resetFCurrency" class="form-select" id="inputGroupSelect01">
          <!-- <label class="input-group-text">뭐지</label> -->
          <option selected :value="null" style="display: none;">통화 단위를 선택해 주세요...</option>
          <option v-for="(exchange, index) in store.exchange"
          :key="exchange.id"
          :value="index">
            {{ exchange.cur_nm }}
          </option>
        </select>
        <input type="number" v-model="exc.fCurrency" @input="updateWon" class="form-control" style="width: 200px;"/>
        <span class="input-group-text">
          <span v-if="exc.selectedExchangeId !== null">{{ store.exchange[exc.selectedExchangeId].cur_unit }}</span>
          <span v-else="exc.selectedExchangeId == null">통화단위</span>
        </span>
      </div>

      <p></p>
      <div class="input-group">
        <input type="number" v-model="exc.won" @input="updateFCurrency" class="form-control" aria-label="Dollar amount (with dot and two decimal places)">
        <span class="input-group-text">WON</span>
      </div>
      <p class="info">* 엔화, 인도네시아 루피아는 100단위, 나머지는 모두 1단위</p>
    </div>
    <!-- <div class="exchange-table">
      <iframe src="https://kr.widgets.investing.com/live-currency-cross-rates?theme=lightTheme&hideTitle=true&roundedCorners=true&pairs=13926,13925,13927,1915,13923,13924,1918,1919,1031410,1920,1921,1922,14486,1925,1926,13922,1928,1089823" width="100%" height="100%" frameborder="0" allowtransparency="true" marginwidth="0" marginheight="0"></iframe><div class="poweredBy" style="font-family: Arial, Helvetica, sans-serif;"></div>
    </div> -->
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore  } from '@/stores/counter'

const today = new Date()

var year = today.getFullYear();
var month = ('0' + (today.getMonth() + 1)).slice(-2);
var day = ('0' + today.getDate()).slice(-2);

var dateString = year + '-' + month  + '-' + day;

var hours = ('0' + today.getHours()).slice(-2); 
var minutes = ('0' + today.getMinutes()).slice(-2);
var seconds = ('0' + today.getSeconds()).slice(-2); 

var timeString = hours + ':' + minutes  + ':' + seconds;

const store = useCounterStore()
const exc = ref({
  selectedExchangeId: null,
  fCurrency: 1,
  won: 1,
  bkpr: 1
})

onMounted(() => {
  store.getExchange()
})

const resetFCurrency = () => {
  exc.value.fCurrency = 1
  exc.bkpr = (store.exchange[exc.value.selectedExchangeId].bkpr).split(',').join("")
  updateWon()
}

const updateWon = () => {
  exc.value.won = exc.value.fCurrency * exc.bkpr
}

const updateFCurrency = () => {
  exc.value.fCurrency = (exc.value.won / exc.bkpr).toFixed(2)
}

</script>

<style scoped>
input::-webkit-inner-spin-button {
  appearance: none;
  -moz-appearance: none;
  -webkit-appearance: none;
}

.outer {
  padding-top: 20px;
  padding-bottom: 20px;
}

.bread-crumb > a {
  text-decoration: none;
  color: black;
  font-size: small;
}
.calc {
  margin: 50px;
  padding: 50px;
  background-color:#c5d5ee;
  border-radius: 10px;
}

.date {
  font-size: small;
}

.info {
  font-size: x-small;
  margin-top: 15px;
  color: gray;
}

.exchange-table {
  padding-left: 50px;
  padding-right: 50px;
  height: 700px;
}
</style>