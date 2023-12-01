<template>
  <div class="outer container">

    <p class="bread-crumb">
      <a href="http://localhost:5173/">홈</a> > <a href="http://localhost:5173/community">자유게시판</a>
    </p>

    <div v-if="article" class="article-deatil">
      <h3>{{ article.title }}</h3>
      <p class="date">작성일 : {{ formatDate(article.created_at) }}</p>
      <hr>
      <p>{{ article.content }}</p>
    </div>

    <div class="button-area">
      <button @click="deleteArticle" type="submit" class="btn btn-danger float-right m-1"
          style="--bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem; color: white;">
        삭제
      </button>
      <button @click="goUpdate" type="button" class="btn btn-success float-right m-1"
          style="--bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem; color: white;">
        수정
      </button>

      <br>
    </div>
    
    <hr>

    <div class="comment-list">
      <h5>댓글창</h5>
      <CreateComment @create=""/>
      <CommentList />
    </div>
    <div style="text-decoration: none;">
      <RouterLink :to="{ name: 'community' }">
        <p style="margin-top: 10px; text-align: center; font-size: medium; text-decoration: none; color: black">목록</p>
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

import CommentList from '@/components/CommentList.vue'
import CreateComment from '@/components/CreateComment.vue'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)

// 날짜 포멧
// 날짜 포멧
const formatDate = (dateTimeString) => {
  const dateObject = new Date(dateTimeString);
  const options = {
    year: '2-digit',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    hourCycle: 'h23', // Use 24-hour format
  };
  const formattedDate = new Intl.DateTimeFormat('en-US', options).format(dateObject);
  return formattedDate.replace(/,/g, '');}


// 게시글 내용 조회
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
    .then((res) => {
      article.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

// 게시글 삭제
const deleteArticle = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
  })
    .then((res) => {
      router.push({ name: 'community' })
      console.log('삭제 완료')
    })
    .catch((err) => {
      console.log(err)
    })
  }

// 수정 페이지로 가기
const goUpdate = function () {
  router.push({name: 'update'})
}

</script>

<style  scoped>
.outer {
  padding-top: 20px;
  padding-bottom: 20px;
}

.bread-crumb > a, .back {
  text-decoration: none;
  color: black;
  font-size: small;
}

.date {
  font-size: small;
}

button {
  display: flex;
  justify-content: end;
  text-align: right;
}

.article-detail {
  border: 1px solid lightgray;
}

.comment-list {
  margin-left: 10px;
  margin-right: 10px;
}
</style>