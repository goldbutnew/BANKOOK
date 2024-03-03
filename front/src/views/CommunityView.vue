<template>
  <div class="outer container">
    <div class="link">
      <p class="bread-crumb">
        <a href="http://localhost:5173/">홈</a> > <a href="http://localhost:5173/community">자유게시판</a>
      </p>
      <h3>😁 자유게시판</h3>
    </div>
    <hr>
    <div class="article-list">
      <ArticleList />
    </div>
    
    <div class="create-article">
      <RouterLink :to="{ name: 'create' }">
        <button class="btn btn-light float-right">글작성</button>
      </RouterLink>
    </div>

  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import ArticleList from '@/components/ArticleList.vue'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})
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

button {
  display: flex;
  justify-content: end;
  text-align: right;
}

.article-list {
  width: 100%;
  margin-top: 10px;
  margin-bottom: 10px;
  padding: 20px;
  border: solid 1px lightgrey 
}

.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.create-article {
  margin-top: 10px;
}

</style>