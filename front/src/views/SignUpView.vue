<template>
    <!-- <div>
    <h1>Sign up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model.trim="username"><br>

      <label for="password">password : </label>
      <input type="password" id="password1" v-model.trim="password1"><br>

      <label for="password2">password confirmation : </label>
      <input type="password" id="password2" v-model.trim="password2">

      <input type="submit" value="Signup">
    </form>
  </div> -->
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
        </div>
  
        <v-text-field
          :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
          :type="visible ? 'text' : 'password'"
          density="compact"
          placeholder="Enter your password"
          variant="outlined"
          @click:append-inner="visible = !visible"
          v-model.trim="password1"
        ></v-text-field>

        <v-text-field
          :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
          :type="visible ? 'text' : 'password'"
          density="compact"
          placeholder="password varification"
          variant="outlined"
          @click:append-inner="visible = !visible"
          v-model.trim="password2"
        ></v-text-field>
        
        <v-card class="mb-12" color="white" variant="tonal">
          <v-card-text class="text-medium-emphasis text-caption">
            --------------------------------------------------------------------------------------
          </v-card-text>
        </v-card>

        <v-btn block class="mb-8" color="blue" size="large" variant="tonal" @click="signUp">
          회원가입
        </v-btn>
  
      </v-card>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const store = useCounterStore()

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}

const visible = ref(false)
</script>

<style>
  .outerouter {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 50px;
  }
  
  #title {
    margin-bottom: 20px;
  }
</style>