<template>
  <div id="app">
    <div class="container">
      <div class="row">
        <div class="col-md-3" v-for="(mbti, index) in mbtiTypes" :key="index">
          <button id="trigger" class="btn btn-outline-primary" @click="openModal(mbti)">{{ mbti }}</button>

          <!-- 모달 창 시작 -->
          <div class="modal" :id="mbti + 'Modal'" tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title">{{ mbti }} Modal</h5>
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close" @click="closeModal(mbti)">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
                <div class="modal-body">
                  <!-- 각 MBTI에 대한 다른 내용 -->
                  <p>{{ getModalContent(mbti) }}</p>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" style="color: white;" data-dismiss="modal" @click="closeModal(mbti)">Close</button>
                </div>
              </div>
            </div>
          </div>
          <!-- 모달 창 끝 -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mbtiTypes: [
        'ISTJ', 'ISFJ', 'INFJ', 'INTJ',
        'ISTP', 'ISFP', 'INFP', 'INTP',
        'ESTP', 'ESFP', 'ENFP', 'ENTP',
        'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ',
      ],
    };
  },
  methods: {
    openModal(mbti) {
      // 해당 MBTI 모달 열기
      $('#' + mbti + 'Modal').modal('show');
    },
    closeModal(mbti) {
      // 해당 MBTI 모달 닫기
      $('#' + mbti + 'Modal').modal('hide');
    },
    getModalContent(mbti) {
      // 각 MBTI에 대한 다른 내용 반환
      return `이것은 ${mbti}에 대한 모달의 내용입니다.`;
    },
  },
};
</script>

<style>
/* 추가적인 스타일링이 필요한 경우 여기에 추가 */
#trigger {
  width: 200px;
  margin: 10px;
}
</style>