<template>
  <section>
    <div class="text-area">
      <h1 class="awards-title">DYK Club</h1>
      <div class="awards-content">
        <p>우리 나라를 빛낸 수많은 K-culture 중 최고는?</p>
        <p>영광의 순간을 맛보러 GO GO~</p>
        <p class="awards-router" @click="goToAwardsPage">
          두유노클럽 입장하기 >>
        </p>
      </div>
    </div>
    <img src="../../assets/DYKClub.png" class="photo" @click="goToAwardsPage" />
    <img src="@/assets/podium.jpg" class="podium" />
  </section>
</template>

<script>
import { useRouter } from "vue-router";
export default {
  setup() {
    const router = useRouter();
    const goToAwardsPage = () => {
      router.push({ name: "DYKC" });
    };
    return {
      goToAwardsPage,
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
  width: 30vw;
  height: auto;
  position: absolute;
  bottom: 30vh;
  right: 15vw;
}

.podium {
  position: absolute;
  top: 0%;
  right: 0%;
  width: 60%;
  z-index: -1;
}

.photo:hover {
  outline: none;
  border-color: #9ecaed;
  box-shadow: 0 0 10px #9ecaed;
  border-radius: 10px;
}

.text-area {
  width: 700px;
  height: 500px;
  position: absolute;
  top: 200px;
  left: 75px;
  text-align: start;
}

.awards-title {
  color: black;
  font-size: 4em;
}

.awards-content {
  font-family: "KOTRA_BOLD-Bold";
  color: black;
  font-size: 1.2em;
}

.awards-content p {
  margin: 0;
}

.awards-router {
  margin-top: 10px;
  background: -webkit-linear-gradient(red, purple);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  cursor: pointer;
  font-weight: bold;
}
</style>
