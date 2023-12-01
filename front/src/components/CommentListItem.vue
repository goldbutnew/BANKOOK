<template>
  <div class="comment-item justify-content-between">
    <td class="comment-content">{{ comment.content }}</td>
    <div class="comment-btn">
      <td class="comment-date">{{ formatDate(comment.created_at) }}</td>
      <button @click="openUpdateModal()" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal">수정</button> /
      <button @click="() => deleteComment(comment.id)">삭제</button>
    </div>

    <!-- 수정 모달 창 -->
    <div v-if="isUpdateModalOpen" class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">댓글수정</h5>
            <button @click="closeUpdateModal" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <textarea v-model="updatedComment" class="form-control"></textarea>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-outline-secondary" @click="closeUpdateModal" data-bs-dismiss="modal">삭제</button>
            <button type="button" class="btn btn-outline-primary" @click="saveUpdatedComment(comment.id)">수정</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <hr>
</template>


<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()

const props = defineProps({
  comment: Object
})

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


// 코멘트 삭제
const deleteComment = function (commentId) {
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/v1/comments/${commentId}`,
    headers: {
      Authorization: `Token ${store.token}`
    },
  })
    .then((res) => {
      // router.push({ naem: "detail"})
      location.reload()
      // store.commit('deleteComment', commentId);
      console.log('삭제 완료')
    })
    .catch((err) => {
      console.log(err)
    })
  }


// 코멘트 수정
const updatedComment = ref(null);
const isUpdateModalOpen = ref(true);
const emit = defineEmits(["update"])

const openUpdateModal = () => {
  console.log(props.comment)
  updatedComment.value = props.comment.content;
  isUpdateModalOpen.value = true;
  console.log(isUpdateModalOpen.value)
};

const closeUpdateModal = () => {
  isUpdateModalOpen.value = false;
};

const saveUpdatedComment = (commentId) => {
  axios({
    method: 'put',
    url: `${store.API_URL}/api/v1/comments/${commentId}/`,
    data: {
      content: updatedComment.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log('댓글 수정 완료', res.data);
      closeUpdateModal();
      // emit("update", content.value)
      location.reload()
    })
    .catch((err) => {
      console.error('댓글 수정 실패', err);
    });
};
</script>

<style>
.comment-item {
  display: flex;
  align-items: center;
}

.comment-content {
  font-size: small;  
}

.comment-date {
  font-size: small;
}

.comment-btn {
  font-size: x-small;
  text-align: right;
}
</style>
