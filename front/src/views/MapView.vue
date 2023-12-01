<template>
  <div class="container">
    <div class="link">
      <p class="bread-crumb">
        <a href="http://localhost:5173/">홈</a> > <a href="http://localhost:5173/map">근처은행검색</a>
      </p>
      <h3>🔎 근처은행검색</h3>
    </div>
    <hr>
  

    <form class="inputForm"  @submit.prevent="searchPlace()">
      <div class="input-group mb-3">
        <select v-for="code in sidolist" :key="code.id" class="form-select" v-model="selectedCode1" @change="onSelected2Change" id="sidoselect">
          <option disabled selected value="">시/도를 선택해주세요.</option>
          <option v-for="optionCode in code" :key="optionCode.id" :value="optionCode">
            {{ optionCode.name }}
          </option>
        </select>

        <select v-for="code in sigungulist" :key="code.id" class="form-select" v-model="selectedCode2" @change="onSelected3Change" id="sigunguselect">
          <option disabled selected value="">시/군/구를 선택해주세요.</option>
          <option v-for="optionCode in code" :key="optionCode.id" :value="optionCode">
            {{ optionCode.name }}
          </option>
        </select>

        <select div v-for="code in donglist" :key="code.id" class="form-select" v-model="selectedCode3" id="dongselect">
          <option disabled selected value="null">읍/면/동/리를 선택해주세요.</option>
          <option v-for="optionCode in code" :key="optionCode.id" :value="optionCode">
            {{ optionCode.name }}
          </option>
        </select>
        
        <select v-model="bankselect" id="bankselect" class="form-select">
          <option disabled selected value="">은행을 선택해 주세요...</option>
          <option value="신한은행">신한은행</option>
          <option value="하나은행">하나은행</option>
          <option value="KB국민은행">KB국민은행</option>
          <option value="한국씨티은행">한국씨티은행</option>
          <option value="우리은행">우리은행</option>
          <option value="SC제일은행">SC제일은행</option>
          <option value="NH농협은행">NH농협은행</option>
          <option value="SH수협은행">SH수협은행</option>
          <option value="KDB산업은행">KDB산업은행</option>
          <option value="IBK기업은행">IBK기업은행</option>
          <option value="한국수출입은행">한국수출입은행</option>
          <option value="부산은행">부산은행</option>
          <option value="경남은행">경남은행</option>
          <option value="제주은행">제주은행</option>
          <option value="대구은행">대구은행</option>
          <option value="광주은행">광주은행</option>
          <option value="전북은행">전북은행</option>
        </select>

        <!-- <button type="submit" class="btn btn-outline-secondary" @submit.prevent="searchPlace(selectedCode1+' '+selectedCode2+' '+selectedCode3+' '+bankselect)">찾기</button> -->
        <button type="submit" class="btn btn-outline-secondary">찾기</button>

      </div>
    </form>
  
  
    <div id="map"></div>
  </div>
</template>
  
<style scoped>
.bread-crumb > a {
  text-decoration: none;
  color: black;
  font-size: small;
}

.inputForm {
  margin: 20px;
}

#map {
  height: 600px;
  border: 10px solid whitesmoke;
  margin: 20px;
}
.container {
  padding-top: 20px;
  padding-bottom: 20px;
}

.select-div {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}

/* select {
  margin: 5px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 200px;
} */

</style>
<script setup>
    import { ref,inject } from 'vue'
    import axios from 'axios'
    const language = inject('language',ref(''))
</script>

<script >
  import { ref,inject } from 'vue'
  import { baseCompile } from '@vue/compiler-core'
  const language = inject('language',ref(''))
  console.log(language)

  export default {
  name: "KakaoMap", // 컴포넌트 이름 지정
  data() {
    return {
      sidolist: [],
      sigungulist: [],
      donglist: [],
      selectedCode1: 11,
      selectedCode2: 123,
      selectedCode3: 123,
      bankselect: null,
    };
  },
  
  mounted() {
      // api 스크립트 소스 불러오기 및 지도 출력
    if (window.kakao && window.kakao.maps) {
      this.loadMap();
    } else {
      this.loadScript();
    }
    this.sidoCodes();
    this.sigunguCodes();
    this.dongCodes();
  },
  methods: {
      // api 불러오기

      onSelected2Change() {
      // 이 메서드에서 select가 변경됐을 때 실행할 로직을 추가하세요.
      // 예를 들어, sigunguCodes()를 호출하거나 다른 로직을 추가할 수 있습니다.
      this.sigunguCodes();
      },

      onSelected3Change() {
        // 이 메서드에서 select가 변경됐을 때 실행할 로직을 추가하세요.
        // 예를 들어, sigunguCodes()를 호출하거나 다른 로직을 추가할 수 있습니다.
        this.dongCodes();
      },

      sidoCodes() {
        axios({
          method: 'get',
          url: `https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=*00000000`
        })
        .then((res) => {
          this.sidolist = res.data;
          console.log(res.data)
        })
        .catch((error) => {
          console.error("API 호출 중 에러 발생:", error);
        })
      },
      
      sigunguCodes() {
        if (this.selectedCode1 && this.selectedCode1.code) {
            // Use substring only if selectedCode1 and its code property exist
            var tempcode1 = this.selectedCode1.code.substring(0, 2);

      axios({
        method: 'get',
        url: `https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=${tempcode1}???00000`
        })
        .then((res) => {
        this.sigungulist = res.data;
        console.log(tempcode1)
        console.log(res.data)
        })
        .catch((error) => {
        console.error("API 호출 중 에러 발생:", error);
        }) } else {
        console.error("selectedCode1 is null or undefined");
      }
      },

      dongCodes() {
        if (this.selectedCode1 && this.selectedCode1.code) {
            // Use substring only if selectedCode1 and its code property exist
            var tempcode1 = this.selectedCode2.code.substring(0, 5);

      axios({
      method: 'get',
        url: `https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=${tempcode1}*&is_ignore_zero=true`
        })
        .then((res) => {
        this.donglist = res.data;
        console.log(res.data)
        console.log(tempcode1)
        })
        .catch((error) => {
        console.error("API 호출 중 에러 발생:", error);
      })
    }
    }, 

    
    loadScript() {
      const script = document.createElement("script");
      script.src =
        // "//dapi.kakao.com/v2/maps/sdk.js?appkey=b63dd7cc18d4a3f04b7d7d4d212ffc38&libraries=services&autoload=false"; 
        "//dapi.kakao.com/v2/maps/sdk.js?appkey=446b7caced64ca3ed637bd373f449f42&libraries=services&autoload=false"; 
      script.onload = () => window.kakao.maps.load(this.loadMap); 
      document.head.appendChild(script);
    },
    // 맵 출력하기(현재 설정해둔 위치-역삼역)
    loadMap() {
      const container = document.getElementById("map"); 
      const options = {
        center: new window.kakao.maps.LatLng(37.49982193285956, 127.03690105516682), 
        level: 3
      };
  
      var map = new window.kakao.maps.Map(container, options);
  
      // 초기에 설정해둔 지도의 중심좌표를 마커로 표시할 거임.
      var marker = new window.kakao.maps.Marker({
        position: map.getCenter() // 지도의 중심좌표
      })

      // 일반 지도와 스카이뷰로 지도 타입을 전환할 수 있는 지도타입 컨트롤을 생성합니다
      var mapTypeControl = new kakao.maps.MapTypeControl();

      // 지도에 컨트롤을 추가해야 지도위에 표시됩니다
      // kakao.maps.ControlPosition은 컨트롤이 표시될 위치를 정의하는데 TOPRIGHT는 오른쪽 위를 의미합니다
      map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);

      // 지도 확대 축소를 제어할 수 있는  줌 컨트롤을 생성합니다
      var zoomControl = new kakao.maps.ZoomControl();
      map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);


      marker.setMap(map)
    },
  
// 키워드로 장소 서치할 거임
searchPlace() {
  const mapContainer = document.getElementById("map"); 
  const mapOptions = {
    center: new window.kakao.maps.LatLng(37.49982193285956, 127.03690105516682), 
    level: 3
  };

  var map = new window.kakao.maps.Map(mapContainer, mapOptions);


  const keyword = `${this.selectedCode3.name} ${this.bankselect}`;
  if (keyword.length === 0) {
    return;
  }
  const ps = new window.kakao.maps.services.Places();
  ps.keywordSearch(keyword, placesSearchCB)


  function placesSearchCB (data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {
      // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
      // LatLngBounds 객체에 좌표를 추가합니다
      if (data.length > 0) {
        loadMaker(data);
      } else {
        // No results, display an alert message
        alert('검색 결과가 없습니다.');
      }
    } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
      // No results, display an alert message
      alert('검색 결과가 없습니다.');
    } else if (status === kakao.maps.services.Status.ERROR) {
      // Handle error, display an alert message
      alert('검색 중 오류가 발생했습니다.');
    }
  }

  // 지정한 위치에 마커 불러오기
  function loadMaker(places) {
  
    console.log(places)
    var infowindow = new kakao.maps.InfoWindow({zIndex:1});
    var bounds = new window.kakao.maps.LatLngBounds()
    for (let i = 0; i < places.length; i++) {
      var markerPosition = new window.kakao.maps.LatLng(
        places[i].y,
        places[i].x
      );
      const marker = new window.kakao.maps.Marker({
      position: markerPosition,
      });
      marker.setMap(map);

      bounds.extend(markerPosition);
      // 마커에 클릭이벤트를 등록합니다
      window.kakao.maps.event.addListener(marker, 'click', function() {
      // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
      console.log(places[i])
      infowindow.setContent('<div style="padding:5px;font-size:12px;">' + places[i].place_name + '</div>');

      // console.log(ma rker)
      infowindow.open(map, marker);
      });

      // console.log(infowindow.open(this.map, marker))

      map.setBounds(bounds)
    }


    }
}
  }
  };
  </script>