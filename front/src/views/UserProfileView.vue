<template>
  <div class="outer container">
    <div class="link">
      <p class="bread-crumb">
        <a href="http://localhost:5173/">홈</a> >
        <a href="http://localhost:5173/community">유저 프로필</a>
      </p>
      <h3>유저 프로필</h3>
    </div>
    <hr />
    <div class="container mt-5">
      <div class="row">
        <div class="col-md-2">
          <!-- 세로 선택바 -->
          <ul class="nav flex-column">
            <li class="nav-item">
              <a
                class="nav-link active"
                href="#"
                @click="
                  (infoShow = true),
                    (chartShow = false),
                    (recommendShow = false)
                "
                >유저 정보</a
              >
            </li>
            <li class="nav-item">
              <a
                class="nav-link active"
                href="#"
                @click="
                  (infoShow = false),
                    (chartShow = true),
                    (recommendShow = false)
                "
                >가입한 상품 정보</a
              >
            </li>
            <li class="nav-item">
              <a
                class="nav-link active"
                href="#"
                @click="
                  (infoShow = false),
                    (chartShow = false),
                    (recommendShow = true)
                "
                >상품 추천받기</a
              >
            </li>
          </ul>
        </div>
        <div class="col-md-10">
          <!-- 유저 정보 -->
          <div class="card" v-show="infoShow">
            <div
              class="card-header d-flex justify-content-between align-items-center"
              style="min-height: 50px"
            >
              <span>유저 정보</span>
              <button
                v-if="!isEditMode"
                class="btn btn-sm btn-primary"
                @click="editStart"
              >
                수정하기
              </button>
            </div>
            <div class="card-body">
              <!-- 값 표시 -->
              <table class="table table-borderless">
                <tbody>
                  <tr>
                    <td class="col-md-2 border-right">
                      <strong>ID</strong>
                    </td>
                    <td class="col-md-8">
                      <span>{{ store.userInfo.username }}</span>
                    </td>
                  </tr>
                  <tr>
                    <td class="col-md-2 border-right">
                      <strong>닉네임</strong>
                    </td>
                    <td class="col-md-8">
                      <span v-if="!isEditMode">{{
                        store.userInfo.nick_name
                      }}</span>
                      <input
                        v-else
                        v-model="editInfo.nick_name"
                        type="text"
                        class="border-input"
                      />
                    </td>
                  </tr>
                  <tr>
                    <td class="col-md-2 border-right">
                      <strong>Email</strong>
                    </td>
                    <td class="col-md-8">
                      <span v-if="!isEditMode">{{ store.userInfo.email }}</span>
                      <input
                        v-else
                        v-model="editInfo.email"
                        type="text"
                        class="border-input"
                      />
                    </td>
                  </tr>
                  <tr>
                    <td class="col-md-2 border-right">
                      <strong>나이</strong>
                    </td>
                    <td class="col-md-8">
                      <span v-if="!isEditMode">{{ store.userInfo.age }}</span>
                      <input
                        v-else
                        v-model="editInfo.age"
                        type="number"
                        class="border-input"
                      />
                    </td>
                  </tr>
                  <tr>
                    <td class="col-md-2 border-right">
                      <strong>현재 가진 금액</strong>
                    </td>
                    <td class="col-md-8">
                      <span v-if="!isEditMode">{{ store.userInfo.money }}</span>
                      <input
                        v-else
                        v-model="editInfo.money"
                        type="number"
                        class="border-input"
                      />
                    </td>
                  </tr>
                  <tr>
                    <td class="col-md-2 border-right">
                      <strong>연봉</strong>
                    </td>
                    <td class="col-md-8">
                      <span v-if="!isEditMode">{{
                        store.userInfo.salary
                      }}</span>
                      <input
                        v-else
                        v-model="editInfo.salary"
                        type="number"
                        class="border-input"
                      />
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            <!-- edit mode에서만 나타남 -->
            <div v-if="isEditMode" class="card-footer">
              <button
                class="btn btn-sm btn-success float-right"
                @click="editComplete"
              >
                수정 완료
              </button>
            </div>
          </div>

          <!-- ############ -->
          <!-- 가입상품 차트 -->
          <div class="card" v-show="chartShow">
            <div
              class="card-header d-flex justify-content-between align-items-center"
              style="min-height: 50px"
            >
              <span>가입한 상품 정보</span>
            </div>
            <div class="card-body">
              <!-- 값 표시 -->
              <table class="table table-borderless" style="margin-bottom: 10px;">
                <tbody>
                  <tr>
                    <td class="col-md-2 border-right">
                      <strong>가입한 상품들</strong>
                    </td>
                    <td class="col-md-8">
                      <ul v-if="deposit_optionlist" class="chart_ul">
                        <li v-for="(id, index) in deposit_cdlist" class="chart_li">
                          {{ index + 1 }}: (정기예금)
                          {{ store.deposit[id].kor_co_nm }} - 
                          <RouterLink :to="{ name: 'deposit_detail', params: { id: id+1 }}">
                            {{ store.deposit[id].fin_prdt_nm }}
                          </RouterLink>
                        </li>
                      </ul>
                      
                      <ul v-if="saving_optionlist" class="chart_ul">
                        <li v-for="(id, index) in saving_cdlist" class="chart_li">
                          {{ index + 1 + dOptionLen }}: (정기적금)
                          {{ store.saving[id].kor_co_nm }} - 
                          <RouterLink :to="{ name: 'savings_detail', params: { id: id+1 }}">
                            {{ store.saving[id].fin_prdt_nm }}
                          </RouterLink>
                        </li>
                      </ul>
                    </td>
                  </tr>
                  <tr style="height: 500px;">
                    <td class="col-md-2 border-right">
                      <strong>가입한 상품 금리</strong>
                    </td>
                    <td class="col-md-8">
                      <canvas id="myChart" width="1500" height="1500"></canvas>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- ############ -->
          <!-- 상품 추천받기 -->
          <div class="card" v-show="recommendShow">
            <div
              class="card-header d-flex justify-content-between align-items-center"
              style="min-height: 50px"
            >
              <span>상품 추천받기</span>
            </div>
            <div class="card-body">
              <div class="row">
                <!-- 예금상품 -->
                <div class="col-md-6">
                  <p style="font-weight: bold; text-align: center;">예금 추천</p>
                  <hr>
                  <ol>
                    <li v-for="op in recommend_dlist">
                      <p>{{ store.deposit[store.deposit.findIndex(Item => Item.fin_prdt_cd === store.dOption[op-1].fin_prdt_cd)].fin_prdt_nm }}
                      ({{ store.dOption[op-1].save_trm }}개월)
                      - 금리: {{ store.dOption[op-1].intr_rate }}</p>
                    </li>
                  </ol>
                </div>

                <!-- 적금상품 -->
                <div class="col-md-6">
                  <p style="font-weight: bold; text-align: center; background-color: ;">적금 추천</p>
                  <hr>
                  <ol>
                    <li v-for="op in recommend_slist">
                      <p>{{ store.saving[store.saving.findIndex(Item => Item.fin_prdt_cd === store.sOption[op-1].fin_prdt_cd)].fin_prdt_nm }}
                      ({{ store.sOption[op-1].save_trm }}개월)
                      - 금리: {{ store.sOption[op-1].intr_rate }}</p>
                    </li>
                  </ol>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import axios from "axios";
import Chart from 'chart.js/auto'

const store = useCounterStore();
const isEditMode = ref(false);
const editInfo = ref({});

const infoShow = ref(true);
const chartShow = ref(false);
const recommendShow = ref(false);

const editStart = () => {
  editInfo.value = store.userInfo;
  isEditMode.value = true;
};

const editComplete = () => {
  isEditMode.value = false;
  axios({
    method: "put",
    url: `${store.API_URL}/accounts/user/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
    data: editInfo.value,
  })
    .then((res) => {
      console.log(res);
      store.getUserInfo();
    })
    .catch((err) => console.log(err));
};

const deposit_optionlist = ref([]);
const deposit_cdlist = ref([]);
const saving_optionlist = ref([]);
const saving_cdlist = ref([]);
const dOptionLen = ref(0);
const xlabel_list = ref([]);
const intr1_list = ref([]);
const intr2_list = ref([]);


const chartData = ref({
  labels: xlabel_list, // 가로 축 레이블
  datasets: [
    {
      label: '금리', // 차트 레이블
      backgroundColor: 'rgba(75, 192, 192, 0.2)', // 막대 색상
      borderColor: 'rgba(75, 192, 192, 1)', // 막대 테두리 색상
      borderWidth: 1, // 테두리 너비
      data: intr1_list, // 세로 축 데이터 (금리)
    },
    {
      label: '최고우대 금리', // 차트 레이블
      backgroundColor: 'rgba(192, 75, 75, 0.2)', // 막대 색상
      borderColor: 'rgba(192, 75, 75, 1)', // 막대 테두리 색상
      borderWidth: 1, // 테두리 너비
      data: intr2_list, // 세로 축 데이터 (금리)
    },
  ],
});

const chartOptions = ref({
  responsive: true,
  scales: {
    y: {
      beginAtZero: true,
      title: {
        display: true,
        text: '금리',
      },
    },
    x: {
      title: {
        display: false,
        text: '가입한 옵션',
      },
    },
  },
});


onMounted(() => {
  store.getdOption();
  store.getsOption();

  const d_optionListString = store.userInfo.deposit_option_list;
  if (d_optionListString !== null) {
    deposit_optionlist.value = d_optionListString.split(",").map(Number);
  } else {
    deposit_optionlist.value = [];
  }
  deposit_optionlist.value.sort();

  deposit_optionlist.value.forEach(option_id => {
    intr1_list.value.push(store.dOption[option_id-1].intr_rate)
    intr2_list.value.push(store.dOption[option_id-1].intr_rate2)

    const prdt_cd = store.dOption[option_id-1].fin_prdt_cd
    
    const prdt_id = store.deposit.findIndex(depositItem => depositItem.fin_prdt_cd === prdt_cd)
    xlabel_list.value.push(store.deposit[prdt_id].fin_prdt_nm + "(" +store.dOption[option_id-1].save_trm + "개월)")

    if (deposit_cdlist.value.indexOf(prdt_id) === -1) {
      deposit_cdlist.value.push(prdt_id)
    }
  })

  const s_optionListString = store.userInfo.saving_option_list;
  if (s_optionListString !== null) {
    saving_optionlist.value = s_optionListString.split(",").map(Number);
  } else {
    saving_optionlist.value = [];
  }
  saving_optionlist.value.sort();

  saving_optionlist.value.forEach(option_id => {
    intr1_list.value.push(store.sOption[option_id-1].intr_rate)
    intr2_list.value.push(store.sOption[option_id-1].intr_rate2)

    const prdt_cd = store.sOption[option_id-1].fin_prdt_cd

    const prdt_id = store.saving.findIndex(savingItem => savingItem.fin_prdt_cd === prdt_cd)
    xlabel_list.value.push(store.saving[prdt_id].fin_prdt_nm + "(" +store.sOption[option_id-1].save_trm + "개월)")

    if (saving_cdlist.value.indexOf(prdt_id) === -1) {
      saving_cdlist.value.push(prdt_id)
    }
  })

  dOptionLen.value = deposit_cdlist.value.length;

  const ctx = document.getElementById('myChart');
  if (ctx){
    new Chart(ctx, {
      type: 'bar',
      data: chartData.value,
      options: chartOptions.value,
    });
  }

  recommend_dlist.value = getTopNOptions(store.dOption, 'intr_rate', 3)
  recommend_slist.value = getTopNOptions(store.sOption, 'intr_rate', 3)
  console.log(recommend_dlist)
});

const recommend_dlist = ref([])
const recommend_slist = ref([])
const getTopNOptions = (arr, property, n) => {
  // 속성(property)에 따라 내림차순으로 정렬
  arr.sort((a, b) => b[property] - a[property]);

  // 상위 N개 요소 반환
  return arr.slice(0, n).map(option => option.id);
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

table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  padding: 10px;
  text-align: left;
}

.border-right {
  border-right: 1px solid #dee2e6;
}

/* .border-input {
  border: 0.5px solid #ccc;
} */
.chart_ul{
  list-style-type: none;
  padding: 0;
}
.chart_li{
  margin-bottom: 8px;
}
</style>
