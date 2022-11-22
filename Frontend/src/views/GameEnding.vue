<template>
  <div class="ending-background">
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
          onloadstart="this.volume=0.1"
        >
          <source src="@/assets/higherlower/ending-bgm.mp3" type="audio/mp3" />
        </audio>
      </div>
    </div>
    <div class="ending-container">
      <!-- <img
        class="ending-img"
        :src="require(`@/assets/ending-img${randomint}.jpg`)"
        alt=""
      /> -->
      <div class="ending-info">
        <h2 style="color: white; margin-top: 0">🎯당신의 점수는🎯</h2>
        <transition class="animate__animated animate__bounceInDown">
          <h1 class="score">{{ score }}점 !</h1>
        </transition>
        <h3 style="color: white; margin-top: 0; margin-bottom: 4rem">
          아이쿠 손이 미끄러졌네~~🔨
        </h3>
        <div class="button-container">
          <button class="w-btn-neon2" @click="gamestart">다시할래</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import { reactive } from "vue";
export default {
  setup() {
    const router = useRouter();

    let randomint = Math.ceil(Math.random() * 3).toString();

    // 점수가져오기
    let score = 0;
    let getScore = function () {
      score = window.localStorage.getItem("korea-score");
      window.localStorage.removeItem("korea-score");
      
    };
    getScore();

    const gohome = function () {
      router.push({ name: "MainPage" });
    };
    const gamestart = function () {
      router.push({ name: "GamePage" });
    };
    let data = reactive({
      isSound: true,
    });
    const onOffSound = function () {
      data.isSound = !data.isSound;
      
    };

    return {
      onOffSound,
      data,
      randomint,
      gamestart,
      gohome,
      score,
    };
  },
};
</script>

<style scoped>
.ending-background {
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
.ending-container {
  display: flex;
  justify-content: center;
  margin-top: 8rem;
  z-index: 2;
}
.ending-img {
  width: 100%;
  height: 600px;
  opacity: 70%;
  margin-top: -8rem;
  margin-bottom: 3.1rem;
}
.score {
  color: yellow;
  font-size: 5rem;
  margin-top: 0;
  margin-bottom: 1rem;
}
.ending-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: absolute;
  margin-top: 9rem;
}
.button-container {
  display: flex;
  margin-top: 2.5rem;
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
