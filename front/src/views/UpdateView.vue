<template>
  <div class="outer container">
    <div class="link">
      <p class="bread-crumb">
        <a href="http://localhost:5173/">홈</a> > <a href="http://localhost:5173/community">자유게시판</a> > <a href="http://localhost:5173/update">글수정</a>
      </p>
      <h3>✏ 글수정</h3>
    </div>
    <hr>
    <form @submit.prevent="updateArticle" class="update-form">
      <div class="board-title">
        <input class="form-control" type="text" v-model.trim="title" id="title" placeholder="제목">
      </div>
      <div class="board-content">
        <div class="input-group">
          <textarea class="form-control" aria-label="With textarea" v-model.trim="content" id="content" placeholder="내용"></textarea>
        </div>
      </div>
    </form>
    <input class="btn btn-light float-right" type="submit" @click="updateArticle">
  </div>

  <div class="list-container" style="text-decoration: none;">
    <RouterLink :to="{ name: 'community' }">
      <p class="list-text" style="text-decoration: none; color: black;">목록</p>
    </RouterLink>
  </div>

</template>

<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()

const article = ref(null)
const title = ref(null)
const content = ref(null)


// 게시글 내용 조회
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res.data)
      article.value = res.data
      title.value = article.value.title
      content.value = article.value.content
    })
    .catch((err) => {
      console.log(err)
    })
})

// 업데이트 함수
const updateArticle = function () {
  // Check if title or content is empty
  if (!title.value) {
    // Display a warning for empty title
    alert('제목을 입력해주세요!');
    return; // Stop the function execution
  }
  if (!content.value) {
    // Display a warning for empty content
    alert('내용을 입력해주세요!');
    return; // Stop the function execution
  }
  axios({
    method: 'put',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      router.push({ name: 'detail' })
    })
    .catch((err) => {
      console.log(err)
    })
  }

</script>

<style>
.outer {
  padding-top: 20px;
  padding-bottom: 20px;
}

.bread-crumb > a {
  text-decoration: none;
  color: black;
  font-size: small;
}

.update-form {
  margin-top: 10px;
  margin-bottom: 10px;
  padding: 20px;
  background-color: rgb(240, 240, 240);
  /* border: solid 1px lightgrey  */
}

#title {
  width: 100%;
}

#content {
  width: 100%;
  height: 500px;
}

.list-container {
  display: flex;
  justify-content: center;
  margin-top: 20px; /* Add margin-top for spacing */
}

.list-text {
  margin-top: 10px;
  text-align: center;
  font-size: medium;
}


</style>
