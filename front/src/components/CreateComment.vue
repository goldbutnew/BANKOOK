<template>
  <div class="create-comment-form">
    <form class="input-group mb-3">
      <input type="text" class="form-control" placeholder="댓글을 작성하세요" aria-label="Recipient's username" aria-describedby="button-addon2" v-model.trim="content"> 
      <input class="btn btn-light float-right" type="submit" @click="createComment">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'

const content = ref(null)
const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const emit = defineEmits(["create"])

const createComment = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/comments/`,
    data: {
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log('댓글작성완료')
      emit("create", content.value)
      // router.push({ name: 'detail' })
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>
.create-comment-form {
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>