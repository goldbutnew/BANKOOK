<template>
  <div class="outer container">
    <div class="link">
      <p class="bread-crumb">
        <a href="http://localhost:5173/">홈</a> >
        <a href="http://localhost:5173/compare">금융상품비교</a> >
        <a href="http://localhost:5173/compare/savings">정기적금</a> >
        <a :href="`http://localhost:5173/compare/savings/${route.params.id}`">{{
          product.fin_prdt_nm
        }}</a>
      </p>
      <h3>{{ product.fin_prdt_nm }}</h3>
    </div>
    <hr />

    <div>
      <table class="table table-bordered">
        <tbody>
          <tr>
            <td class="col-md-2">
              <strong>공시 제출월</strong>
            </td>
            <td class="col-md-8">
              <span>{{ product.dcls_month }}</span>
            </td>
          </tr>
          <tr>
            <td class="col-md-2">
              <strong>금융회사명</strong>
            </td>
            <td class="col-md-8">
              <span>{{ product.kor_co_nm }}</span>
            </td>
          </tr>
          <tr>
            <td class="col-md-2">
              <strong>상품명</strong>
            </td>
            <td class="col-md-8">
              <span>{{ product.fin_prdt_nm }}</span>
            </td>
          </tr>
          <tr>
            <td class="col-md-2">
              <strong>가입 제한</strong>
            </td>
            <td class="col-md-8">
              <span>{{ product.join_deny }}</span>
            </td>
          </tr>
          <tr>
            <td class="col-md-2">
              <strong>가입 방법</strong>
            </td>
            <td class="col-md-8">
              <span>{{ product.join_way }}</span>
            </td>
          </tr>
          <tr>
            <td class="col-md-2">
              <strong>우대 조건</strong>
            </td>
            <td class="col-md-8">
              <span style="white-space: pre-line">{{ product.spcl_cnd }}</span>
            </td>
          </tr>
          <tr>
            <td class="col-md-2">
              <strong>옵션</strong>
            </td>
            <td class="col-md-8">
              <table class="inner-table">
                <thead>
                  <tr>
                    <th>저축 금리 유형</th>
                    <th>저축 금리</th>
                    <th>최고 우대금리</th>
                    <th>적립 유형</th>
                    <th>저축기간</th>
                    <th v-if="store.isLogin">가입</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="option in product.options" :key="option.id">
                    <td>{{ option.intr_rate_type_nm }}</td>
                    <td>{{ option.intr_rate }}%</td>
                    <td>{{ option.intr_rate2 }}%</td>
                    <td>{{ option.rsrv_type_nm }}</td>
                    <td>{{ option.save_trm }}개월</td>
                    <td v-if="store.isLogin">
                      <input
                        type="checkbox"
                        :checked="isOptionSelected(option.id)"
                        @change="toggleOption(option.id)"
                      />
                    </td>
                  </tr>
                </tbody>
              </table>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div>
      <button
        v-if="store.isLogin"
        class="btn btn-sm btn-primary float-right"
        @click="submitRegistration"
      >
        가입하기
      </button>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();

const store = useCounterStore();
const product = ref({});
const saving_optionlist = ref([]);
const editInfo = ref({});

const get_optionList = () => {
  const optionListString = store.userInfo.saving_option_list;

  if (optionListString !== null) {
    saving_optionlist.value = optionListString.split(",").map(Number);
  } else {
    saving_optionlist.value = [];
  }
};

const isOptionSelected = (optionId) => {
  return saving_optionlist.value.includes(optionId);
};

onMounted(() => {
  product.value = store.saving[route.params.id - 1];
  if (store.isLogin){
    get_optionList();
  }
});

const toggleOption = (optionId) => {
  const index = saving_optionlist.value.indexOf(optionId);
  if (index === -1) {
    // 배열에 없는 경우 추가
    saving_optionlist.value.push(optionId);
  } else {
    // 배열에 있는 경우 제거
    saving_optionlist.value.splice(index, 1);
  }
};


const registrationCompleted = ref(false);

const submitRegistration = () => {
  let selectedOptionStr = null;
  if (saving_optionlist.value.length > 0) {
    selectedOptionStr = saving_optionlist.value.join(",");
  }
  editInfo.value = store.userInfo;
  editInfo.value.saving_option_list = selectedOptionStr;

  console.log(editInfo);
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
      // Set registrationCompleted to true when registration is successful
      registrationCompleted.value = true;

      // Show alert when registration is completed
      window.alert("가입이 완료되었습니다!");
    })
    .catch((err) => console.log(err));
};
</script>

<style  scoped>
.outer {
  padding-top: 20px;
  padding-bottom: 20px;
}

.bread-crumb > a {
  text-decoration: none;
  color: black;
  font-size: small;
}

.inner-table {
  width: 100%;
  border-collapse: collapse; /* 인접 셀의 경계를 병합 */
}

.inner-table th,
.inner-table td {
  border: 1px solid #ddd; /* 가로, 세로선 설정 */
  padding: 8px; /* 내부 여백 설정 */
  text-align: left;
}

.inner-table th {
  background-color: #f2f2f2; /* 헤더 배경색 설정 */
}

table {
  font-size: small;
}
</style>
