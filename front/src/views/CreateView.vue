<template>
  <div class="outer container">
    <div class="link">
      <p class="bread-crumb">
        <a href="http://localhost:5173/">홈</a> > <a href="http://localhost:5173/community">자유게시판</a> > <a href="http://localhost:5173/create">글작성</a>
      </p>
      <div style="display: inline">
        <h3>✏ 글작성</h3>
      </div>
    </div>
    <hr>
    <form @submit.prevent="createArticle" class="create-form">
      <div class="board-title">
        <input class="form-control" type="text" v-model.trim="title" id="title" placeholder="제목">
      </div>
      <div class="board-content">
        <div class="input-group">
          <textarea class="form-control" type="text" v-model.trim="content" id="content" placeholder="내용"></textarea>
        </div>
      </div>
    </form>
    <input class="btn btn-light float-right" type="submit" @click="createArticle">
  </div>

  <!-- <input type="button" value="BACK" onClick="history.go(-1)">  -->

  <div class="list-container" style="text-decoration: none;">
    <RouterLink :to="{ name: 'community' }">
      <p class="list-text" style="margin-top: 10px; text-align: center; font-size: medium; text-decoration: none; color: black">목록</p>
    </RouterLink>
  </div>

</template>

<script setup>
// import 'quill/dist/quill.core.css';
// import 'quill/dist/quill.snow.css';
// import { QuillEditor } from 'vue3-quill';

import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useCounterStore()
const router = useRouter()

// const editorOptions = {
//     modules: {
//       toolbar: [
//         ['bold', 'italic', 'underline', 'strike'],      // add the formatting options you want
//         ['link', 'image', 'video'],
//         ['clean'],
//       ],
//     },
//   };


const createArticle = function () {
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
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      router.push({ name: 'community' })
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

.create-form {
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
