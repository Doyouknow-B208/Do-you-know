<template>
  <div class="game-background">
    <a href="https://j7b208.p.ssafy.io/">
      <img src="@/assets/logo.png" alt="logo" class="logo" />
    </a>
    <div>
      <div>
        <img
          v-show="data.isSound === true"
          class="soundbtn"
          src="@/assets/DYKC/soundon.png"
          @click="onOffSound"
        />
        <img
          v-show="data.isSound === false"
          class="soundbtn"
          src="@/assets/DYKC/soundoff.png"
          @click="onOffSound"
        />
      </div>
      <div v-if="data.isSound === true">
        <audio
          id="myAudio"
          autoplay="autoplay"
          loop
          onloadstart="this.volume=0.4"
        >
          <source src="@/assets/higherlower/bg-music.mp3" type="audio/mp3" />
        </audio>
      </div>
    </div>
    <div class="game-container">
      <transition class="animate__animated animate__heartBeat">
        <img class="game-logo" src="@/assets/hilow.png" alt="game-logo" />
      </transition>
      <div class="intro-container">
        <div class="sub-intro">
          <h3>(그런데 국뽕을 곁들인)</h3>
        </div>
        <div class="main-intro">
          <h1>어떤 키워드들이 더 많이 검색됐을까?</h1>
          <h2 class="intro-h2">
            세계 6개국 Google News 한국관련 키워드 수집량
          </h2>
          <h3 class="intro-h2">(2022년 10월기준 3개월)</h3>
        </div>
      </div>
      <div class="button-container">
        <button class="w-btn-neon2" @click="gamestart">시이작 !</button>
      </div>
    </div>
  </div>
</template>

<script>
import { reactive } from "@vue/reactivity";
import { useRouter } from "vue-router";

export default {
  setup() {
    const router = useRouter();
    const gamestart = function () {
      router.push({ name: "GamePlay" });
    };
    const gohome = function () {
      router.go(-1);
    };
    let data = reactive({
      isSound: true,
    });
    const onOffSound = function () {
      data.isSound = !data.isSound;
    };

    return {
      data,
      onOffSound,
      gamestart,
      gohome,
    };
  },
};
</script>

<style scoped>
.game-background {
  overflow: hidden;
  background-color: rgba(137, 156, 255, 75%);
  background: url("@/assets/bg-2.png") no-repeat center center fixed;
  background-size: cover;
  height: 100%;
  width: 100%;
}
.logo {
  border: 0;
  width: 5vw;
  height: auto;
  margin: 10px 0 0 10px;
}

.game-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: -3rem;
}
.game-logo {
  height: 700px;
  width: 700px;
}
.game-logo:hover {
  transform: scale(1.05);
  filter: drop-shadow(0 0px 10px rgba(0, 0, 0, 0.5));
}
.intro-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: -15rem;
}
.sub-intro {
  color: white;
  margin-left: 20rem;
  margin-top: -2rem;
}
.main-intro {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.intro-h2 {
  color: #909090;
  margin-top: -1rem;
}
.button-container {
  height: 6.3rem;
  margin-top: 2rem;
  margin-bottom: 4rem;
  z-index: 1;
}
button {
  padding: 13px;
  width: 200px;
  background: none;
  border: 3px solid white;
  border-radius: 200px;
  font-weight: bold;
  color: white;
  font-size: 16pt;
  cursor: pointer;
  transition: color 0.2s, background-color 0.2s;
}
button:hover {
  color: black;
  text-shadow: 1px 2px grey;
  background-color: white;
}
.soundbtn {
  width: 3rem;
  height: auto;
  position: absolute;
  right: 0%;
  margin-left: auto;
  margin-right: 5rem;
  cursor: pointer;
}
</style>
