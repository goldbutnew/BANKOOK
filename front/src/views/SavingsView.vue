<template>
  <div class="outer container">
    <div class="link">
      <p class="bread-crumb">
        <a href="http://localhost:5173/">홈</a> >
        <a href="http://localhost:5173/compare">금융상품비교</a> >
        <a href="http://localhost:5173/compare/savings">정기적금</a>
      </p>
      <div style="white-space: nowrap">
        <h3>
          <span><a href="http://localhost:5173/compare/deposit" style="text-decoration: none; color: black;">정기예금 </a></span>
          <span style="font-weight: bold;">정기적금</span>
        </h3>        
      </div>
    </div>
    <hr />
    <div class="container mt-5">
      <table class="table table-bordered table-striped">
        <thead>
          <tr class="align-middle">
            <th rowspan="2">공시 제출월</th>
            <th rowspan="2">금융회사명</th>
            <th rowspan="2">상품명</th>
            <th colspan="2">6개월</th>
            <th colspan="2">12개월</th>
            <th colspan="2">24개월</th>
            <th colspan="2">36개월</th>
          </tr>
          <tr class="align-middle" style="font-size: small">
            <th>저축 금리</th>
            <th>최고 우대금리</th>
            <th>저축 금리</th>
            <th>최고 우대금리</th>
            <th>저축 금리</th>
            <th>최고 우대금리</th>
            <th>저축 금리</th>
            <th>최고 우대금리</th>
          </tr>
        </thead>
        <tbody style="font-size: small">
          <tr v-for="product in store.saving">
            <td>{{ product.dcls_month }}</td>
            <td>{{ product.kor_co_nm }}</td>
            <td>
              <RouterLink
                :to="{ name: 'savings_detail', params: { id: product.id } }"
                style="text-decoration: none; color: black"
              >
                {{ product.fin_prdt_nm }}
              </RouterLink>
            </td>
            <td>{{ getOptionIntr1(product, 6) }}</td>
            <td>{{ getOptionIntr2(product, 6) }}</td>
            <td>{{ getOptionIntr1(product, 12) }}</td>
            <td>{{ getOptionIntr2(product, 12) }}</td>
            <td>{{ getOptionIntr1(product, 24) }}</td>
            <td>{{ getOptionIntr2(product, 24) }}</td>
            <td>{{ getOptionIntr1(product, 36) }}</td>
            <td>{{ getOptionIntr2(product, 36) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useCounterStore } from "@/stores/counter";

// import SavingsView from '@/views/SavingsView.vue';
// import DepositView from '@/views/DepositView.vue';

const store = useCounterStore();

onMounted(() => {
  store.getDeposit();
  store.getSaving();
});

const getOptionIntr1 = (product, savetrm) => {
  const option = product.options.find((opt) => opt.save_trm === savetrm);
  return option ? (option.intr_rate ? `${option.intr_rate} %` : "-") : "-";
};

const getOptionIntr2 = (product, savetrm) => {
  const option = product.options.find((opt) => opt.save_trm === savetrm);
  return option ? (option.intr_rate2 ? `${option.intr_rate2} %` : "-") : "-";
};
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

table {
  font-size: small;
}

</style>
