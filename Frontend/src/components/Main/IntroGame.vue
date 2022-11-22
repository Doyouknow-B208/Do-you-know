<template>
  <div class="text-area">
    <div class="game-title">
      <p>Do You Know</p>
      <span class="more">더 많이 </span>
      <span class="less">더 적게</span><span>?</span>
    </div>
    <div class="game-content">
      <p>총 검색량으로 K-culture의 힘을 알아봅시다!</p>
      <p>어떤 것이 최고의 DoYouKnow 지수를 갖고 있을지 궁금하다면?</p>
      <div class="game-router" @click="goToGamePage">플레이 하러 가기 >></div>
    </div>
  </div>
  <img class="photo" src="@/assets/highlow.jpg" />
</template>

<script>
import { useRouter } from "vue-router";
export default {
  setup() {
    const router = useRouter();
    const goToGamePage = () => {
      router.push({ name: "GamePage" });
    };
    return {
      goToGamePage,
    };
  },
};
</script>

<style scoped>
@font-face {
  font-family: "KOTRA_BOLD-Bold";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-10-21@1.1/KOTRA_BOLD-Bold.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
.photo {
  position: absolute;
  top: 200px;
  left: 200px;
  width: 40vw;
  height: auto;
}

.text-area {
  width: auto;
  height: 500px;
  position: absolute;
  top: 200px;
  right: 100px;
  text-align: start;
}

.game-title {
  color: black;
  font-size: 4em;
}

.game-title p {
  margin: 0;
  font-weight: bold;
}

.more {
  font-family: "KOTRA_BOLD-Bold";
  color: red;
}

.less {
  font-family: "KOTRA_BOLD-Bold";
  color: blue;
}

.game-content {
  font-family: "KOTRA_BOLD-Bold";
  color: black;
  font-size: 1.2em;
  margin-top: 30px;
}

.game-content p {
  margin: 0;
}

.game-router {
  margin-top: 10px;
  background: -webkit-linear-gradient(red, blue);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  cursor: pointer;
  font-weight: bold;
}
</style>
