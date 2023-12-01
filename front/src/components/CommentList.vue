<template>
  <div>
    <table class="container">
      <div v-for="comment in comments"
        :key="comment.article"
        :comment="comment"
      >
        {{ comments }}
      </div>
      <tbody class="get-comment ">
        <CommentListItem 
          v-for="comment in store.comments.slice().reverse()"
          :key="comment.article"
          :comment="comment"
        />      
      </tbody>
    </table>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'
import CommentListItem from '@/components/CommentListItem.vue'

const store = useCounterStore()
const route = useRoute()
const comments = ref(null)

onMounted(() => {
  store.getComments()
})

// onMounted((articleId) => {
//   axios({
//     method: 'get',
//     url: `${store.API_URL}/api/v1/comments/all/${articleId}`
//   })
//     .then((res) => {
//       comments.value = res.data
//     })
//     .catch((err) => {
//       console.log(err)
//     })
// })

console.log(store.comments)

</script>

<style>
  .container {
    padding-top: 20px;
    padding-bottom: 20px;
  }

  table {
    border-collapse: collapse;
    border: 0;
  }

  .get-comment {
    margin-top: 10px;
    margin-bottom: 10px;
    padding: 20px;
  }
</style>
