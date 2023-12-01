<template>
  <div class="outerouter">
      <v-card
        class="mx-auto pa-12 pb-8"
        elevation="8"
        max-width="448"
        rounded="lg"
      >
        <div class="text-center mb" id="title">
          <h3>BANKOOK</h3>
        </div>
        <div class="text-subtitle-1 text-medium-emphasis">아이디</div>
  
        <v-text-field
          density="compact"
          placeholder="아이디"
          variant="outlined"
          v-model.trim="username"
        ></v-text-field>
  
        <div
          class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between"
        >
          비밀번호
  
          <a
            class="text-caption text-decoration-none text-grey"
            href="#"
            rel="noopener noreferrer"
            target="_blank"
          >
            비밀번호를 잊으셨나요?</a
          >
        </div>
  
        <v-text-field
          :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
          :type="visible ? 'text' : 'password'"
          density="compact"
          placeholder="Enter your password"
          variant="outlined"
          @click:append-inner="visible = !visible"
          v-model.trim="password"
        ></v-text-field>
  
        <v-card class="mb-12" color="grey" variant="tonal">
          <v-card-text class="text-medium-emphasis text-caption">
            경고: 3회 연속 로그인 시도에 실패하면 3시간 동안 로그인을 시도할 수
            없습니다. 지금 로그인해야 하는 경우, "비밀번호를 잊으셨나요?" 문구를
            클릭하세요. 비밀번호를 재설정할 수 있습니다.
          </v-card-text>
        </v-card>
  
        <v-btn block class="mb-8" color="blue" size="large" variant="tonal" @click="logIn">
          로그인
        </v-btn>
  
        <v-card-text class="text-center">
          <a
            class="text-grey text-decoration-none"
            href="http://localhost:5173/signup"
            rel="noopener noreferrer"
          >
            회원가입 <v-icon icon="mdi-chevron-right"></v-icon>
          </a>
        </v-card-text>
      </v-card>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { useCounterStore } from '@/stores/counter'
  
  const username = ref(null)
  const password = ref(null)
  const router = useRouter()
  const store = useCounterStore()

  const logIn = function () {
    const payload = {
      username: username.value,
      password: password.value
    }
    store.logIn(payload)
    router.push({name:'main'})
  }
  
  const visible = ref(false);
  
  </script>
  
  <style>
  .outerouter {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 150px;
  }
  
  #title {
    margin-bottom: 20px;
  }
  </style>
  