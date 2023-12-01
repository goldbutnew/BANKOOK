<template>
  <tr class="align-middle">
    <td>{{ article.id }}</td>
    <!-- 디버깅 필요 -->
    <td>
      <RouterLink :to="{ name: 'detail', params: { id: article.id }}" style="font-size: medium; text-decoration: none; color: black">
        {{ article.title }}
      </RouterLink>      
    </td>
    <!-- <td>{{ article.title }}</td> -->
    <td>익쿡{{ article.id }}</td>
    <td class="article-date-time">{{ formatDate(article.created_at) }}</td>
    <!-- <td>{{ article.created_at.slice(0, 10) }}</td> -->
  </tr>
</template>

<script setup>
import { RouterLink, useRoute } from 'vue-router'

const route = useRoute()

defineProps({
  article: Object
})

const router = useRoute

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


</script>

<style>
</style>
