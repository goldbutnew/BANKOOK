import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

import { useRoute, useRouter } from "vue-router";

export const useCounterStore = defineStore(
  "counter",
  () => {
    const API_URL = "http://127.0.0.1:8000";
    const articles = ref([]);
    const comments = ref([]);

    const route = useRoute();
    const router = useRouter();

    const getArticles = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          articles.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const getComments = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/comments/all/${route.params.id}`,
        // url: `${API_URL}/api/v1/articles/${route.params.id}/comments/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          comments.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const getCompareData = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/deposit/`,
      })
        .then((res) => {
          console.log("deposit data download");
        })
        .catch((err) => console.log(err));

      axios({
        method: "get",
        url: `${API_URL}/api/v1/saving/`,
      })
        .then((res) => {
          console.log("saving data download");
        })
        .catch((err) => console.log(err));
    };

    const deposit = ref([]);
    const getDeposit = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/deposit/data/`,
      })
        .then((res) => {
          deposit.value = res.data;
        })
        .catch((err) => console.log(err));
    };

    const saving = ref([]);

    const getSaving = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/saving/data/`,
      })
        .then((res) => {
          saving.value = res.data;
        })
        .catch((err) => console.log(err));
    };

    const exchange = ref([]);
    const getExchange = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/exchanges/`,
      })
        .then((res) => {
          exchange.value = res.data;
        })
        .catch((err) => console.log(err));
    };

    const signUp = function (payload) {
      const username = payload.username;
      const password1 = payload.password1;
      const password2 = payload.password2;

      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
        },
      })
        .then((res) => {
          console.log("회원가입이 완료되었습니다.");
          const password = password1;
          logIn({ username, password });
          router.push({ name: "profile" });
        })
        .catch((err) => console.log(err));
    };

    const token = ref(null);

    const logIn = function (payload) {
      const username = payload.username;
      const password = payload.password;
      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          token.value = res.data.key;
          getUserInfo();
        })
        .catch((err) => console.log(err));
    };

    const userInfo = ref(null);
    const getUserInfo = function () {
      axios({
        method: "get",
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          console.log(res.data);
          userInfo.value = res.data;
        })
        .catch((err) => console.log(err));
    };

    const isLogin = computed(() => {
      if (token.value === null) {
        return false;
      } else {
        return true;
      }
    });

    const dOption = ref([]);
    const sOption = ref([]);

    const getdOption = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/deposit/option/`,
      })
        .then((res) => {
          dOption.value = res.data;
        })
        .catch((err) => console.log(err));
    };
    const getsOption = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/saving/option/`,
      })
        .then((res) => {
          sOption.value = res.data;
        })
        .catch((err) => console.log(err));
    };

    return {
      API_URL,
      articles,
      getArticles,
      comments,
      getComments,
      getCompareData,
      deposit,
      getDeposit,
      saving,
      getSaving,
      exchange,
      getExchange,
      signUp,
      token,
      logIn,
      getUserInfo,
      userInfo,
      isLogin,
      getdOption,
      getsOption,
      dOption,
      sOption,
    };
  },
  { persist: true }
);
