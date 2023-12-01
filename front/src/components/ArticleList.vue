<template>
  <div>
    <table class="table table-border table-hover container">
      <thead>
        <tr>
          <th style="width: 50px;">번호</th>
          <th>제목</th>
          <th style="width: 100px;">작성자</th>
          <th style="width: 150px;">작성일시</th>
        </tr>
      </thead>
      <tbody>
        <!-- 게시글 역순 출력 해결해야 함-->
        <!-- v-for="article in store.articles.slice().reverse()" -->
        <ArticleListItem 
          v-for="article in store.articles.slice().reverse()"
          :key="article.id"
          :article="article"
        />          
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useCounterStore()

console.log(store.articles)
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
</style>
