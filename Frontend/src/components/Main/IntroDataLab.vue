<template>
  <div class="text-area">
    <h1>DYK DataLab</h1>
    <div class="datalab-content">
      <p>주요 6개국의 데이터를 한 눈에!</p>
      <p>한국에 대한 키워드를 나라별로 확인할 수 있습니다.</p>
      <div class="datalab-router" @click="goToDatalab">데이터 확인하러 가기 >></div>
    </div>
  </div>
  <img class="photo" src="@/assets/wordcloud.png" alt="">
  <img class="data-img" src="@/assets/data-img.gif" >
</template>

<script>
import { useRouter } from "vue-router";
export default {
  setup(){
    const router = useRouter();
    const goToDatalab = () => {
      router.push({name: 'DatalabPage'})
    }
    return {
      goToDatalab
    }
  }
  
}
</script>

<style scoped>
.photo {
  position: absolute;
  top: 200px;
  left: 200px;
  width: 700px;
  height: 600px;
  z-index: 0;
}

.data-img {
  width: 60%;
  height: 100%;
  position: absolute;
  left: 0%;
  z-index: -1;
}

.text-area {
  position: absolute;
  top: 200px;
  right: 100px;
  width: 500px;
  height: 500px;
  text-align: start;
}

h1 {
  font-size: 4em;
  width: 500px;
  color: black;
  font-family: sans-serif;
  text-align: start;
}

.datalab-content p {
  margin: 0;
  color: black;
  font-size: 1.2em;
}

.datalab-router {
  margin-top: 10px;
  background: -webkit-linear-gradient(white, rgb(18, 201, 222));
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  cursor: pointer;
  font-weight: bold;
}
</style>
