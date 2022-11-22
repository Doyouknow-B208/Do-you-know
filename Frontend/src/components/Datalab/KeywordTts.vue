<template>
  <div class="tts-container">
    <div class="wrapper">
      <div class="slide-group">
        <div @click="Speak()" class="bubble">
          <em></em>
          <template v-if="this.getTTS">
            <p>
              <span>
                {{ this.getTTS.replace("?", "") }}?
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="30"
                  height="30"
                  fill="currentColor"
                  class="bi bi-volume-up sound"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M11.536 14.01A8.473 8.473 0 0 0 14.026 8a8.473 8.473 0 0 0-2.49-6.01l-.708.707A7.476 7.476 0 0 1 13.025 8c0 2.071-.84 3.946-2.197 5.303l.708.707z"
                  />
                  <path
                    d="M10.121 12.596A6.48 6.48 0 0 0 12.025 8a6.48 6.48 0 0 0-1.904-4.596l-.707.707A5.483 5.483 0 0 1 11.025 8a5.483 5.483 0 0 1-1.61 3.89l.706.706z"
                  />
                  <path
                    d="M10.025 8a4.486 4.486 0 0 1-1.318 3.182L8 10.475A3.489 3.489 0 0 0 9.025 8c0-.966-.392-1.841-1.025-2.475l.707-.707A4.486 4.486 0 0 1 10.025 8zM7 4a.5.5 0 0 0-.812-.39L3.825 5.5H1.5A.5.5 0 0 0 1 6v4a.5.5 0 0 0 .5.5h2.325l2.363 1.89A.5.5 0 0 0 7 12V4zM4.312 6.39 6 5.04v5.92L4.312 9.61A.5.5 0 0 0 4 9.5H2v-3h2a.5.5 0 0 0 .312-.11z"
                  />
                </svg>
              </span>
            </p>
          </template>
          <!-- <template v-else><p><span>bubble left text </span></p></template> -->
          <em></em>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { mapGetters, mapActions } from "vuex";
export default {
  setup() {
    const store = useStore();

    let utterThis = new SpeechSynthesisUtterance();
    utterThis.voice = speechSynthesis.getVoices()[8];
    speechSynthesis.speak(utterThis);

    const Speak = function Speak() {
      let lang = null;
      if (store.getters.getConditionNation == 1) {
        lang = "en-US";
      }
      if (store.getters.getConditionNation == 2) {
        lang = "en-UK";
      }
      if (store.getters.getConditionNation == 3) {
        lang = "ja-JP";
      }
      if (store.getters.getConditionNation == 4) {
        lang = "vi-VN";
      }
      if (store.getters.getConditionNation == 5) {
        lang = "id-ID";
      }
      if (store.getters.getConditionNation == 6) {
        lang = "pt-BR";
      }

      // let utterThis = new SpeechSynthesisUtterance(store.getters.getTTS+"?");
      utterThis.text = store.getters.getTTS + "?";
      utterThis.voice = speechSynthesis.getVoices()[8];
      utterThis.lang = lang;
      window.speechSynthesis.speak(utterThis);
    };
    return { store, Speak, utterThis };
  },
  computed: {
    ...mapGetters([
      "getCurrentRank",
      "getConditionNation",
      "getGraphKeyword",
      "getCurrentTrans",
      "getTTS",
    ]),
  },
  methods: {
    ...mapActions(["getTranslateKeyword", "TTSTranslate"]),
  },
  watch: {
    getCurrentRank: function (keyword) {
      let nation = null;
      //   let lang = null;
      if (this.store.getters.getConditionNation == 1) {
        nation = "en";
      }
      if (this.store.getters.getConditionNation == 2) {
        nation = "en";
      }
      if (this.store.getters.getConditionNation == 3) {
        nation = "ja";
      }
      if (this.store.getters.getConditionNation == 4) {
        nation = "vi";
      }
      if (this.store.getters.getConditionNation == 5) {
        nation = "id";
      }
      if (this.store.getters.getConditionNation == 6) {
        nation = "pt";
      }

      const condition = {
        keyword: keyword + "를 아십니까",
        nation: nation,
      };
      this.store.dispatch("TTSTranslate", condition);

      //   let utterThis = new SpeechSynthesisUtterance(this.store.getters.getTTS+"?");
      //   utterThis.voice = speechSynthesis.getVoices()[8];
      //   utterThis.lang = lang;
      //   window.speechSynthesis.speak(utterThis);
    },
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

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  top: 65px;
}
.sound {
  margin-bottom: -8px;
  cursor: pointer;
}
.wrapper {
  width: 100%;
}
.slide-group {
  height: 100%; /*animation:slideup 5s infinite linear;*/
}

@keyframes slideup {
  0% {
    transform: translateY(0%);
  }
  100% {
    transform: translateY(-100%);
  }
}
.bubble {
  position: relative;
}
.bubble.right {
  text-align: right;
}
.bubble.center {
  text-align: center;
}

.bubble p {
  display: inline-block;
  position: relative;
}
.bubble p span {
  display: inline-block;
  background: #fbfcff;
  padding: 10px 30px 15px;
  border-radius: 400px;
  box-shadow: inset -3px -3px 8px rgba(0, 0, 0, 0.3);
  filter: drop-shadow(3px 3px 5px rgba(0, 0, 0, 20%));
  z-index: 2;
  /* font-family: "KOTRA_BOLD-Bold"; */
  opacity: 75%;
  font-size: 20px;
}
.bubble p::before {
  content: "";
  width: 49px;
  height: 19px;
  position: absolute;
  bottom: -18px;
  left: 75%;
  transform: translateX(-50%);
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='49px' height='19px'%3E%3Cimage x='0px' y='0px' width='49px' height='19px' xlink:href='data:img;base64,iVBORw0KGgoAAAANSUhEUgAAADEAAAATCAQAAACT8S2qAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAHdElNRQfmCRUQDB21ixdGAAACU0lEQVQ4y62VO2sWQRSGn7ls0BBjEIOoTSBeQEkwIaaSeGuMKGJjKzYWlvkb4g+QoIWIFhaiCNqIl0bFCF5A01kpYmEaNTuzM3Msdve75UI+Ps9hYXaZnWfO+56dVe9QKBQajRKFbtzVaaqrTIUCFHUIkYjHkeMpiCQltIbFyhYgSwOyVZ1Uw2mn2qV2qz16nx5SGDQJg2CqhetNqAZCIehy7OWq3GETeRtCgloSQH4291cuoXboQ3FKT+sZM2SwGGyFauJAGgDgCjegvQZQC/Wg+agFpFFooyfMGXPejlvqNA3RhEiBY5nl5DZ7H9dGdEYTpFFoDGbMXMou2m0ZGRZbeQORgGOZPOb9hQ9IB0SvQUAQEolEIBDwuE9uLh/J5/IfOQ5PIJKQqlqLMWa/XmVBc5mNhNTp0+t0XaJMk7XPSCTS9/RSVry7plCrSaeqJrZke7P5vqMZGQaNqsTKv+Wj3gVim1gbrKJZDSQE+SW35I8cE9NaJ4OyJK86veiiis5aMuzhvrvZaGk9RAr8bzfuvxaVS7K+3eu5EollA7zNJ/PbDkdBRNCYAXvTaotuOQO6FKodJSSX7suHdCQNSiUjI2h5JtUc1QuiXFBIyKLMS79MiS6xzMhHWWwgu/ei05fyHLOYA+aaOaWBRPwbToQ3dWd17UWnWKn6MP1nP+tm/UJBJPXziLH6qOwJUTsSy27CP/HT/lzxPpK285SDJaRHRLOWRCRQSPEwTIbT8XkclhcyJf8HUWJqSCRIeByOp4l0Tx5wtke7V4ai9U/CgFzgyz+FYyTNc6r0WAAAAABJRU5ErkJggg=='/%3E%3C/svg%3E");
  /* no-repeat top center; */
  filter: drop-shadow(3px 3px 5px rgba(0, 0, 0, 20%));
}
.bubble.right p::before {
  transform: translateX(-50%) rotateY(180deg);
}
.bubble.center p::before {
}
.bubble em {
  display: inline-block;
  font-size: 30px;
  color: #fff;
  position: relative;
}
.bubble p::after {
  position: absolute;
  /* filter: drop-shadow(5px 7px 3px rgba(0, 0, 0, 30%)); */
  transform-origin: center;
}
.bubble p::after {
  /* content:url("https://dyk.s3.ap-northeast-2.amazonaws.com/gookbon1.png"); */
  content: "";
  background-image: url("https://dyk.s3.ap-northeast-2.amazonaws.com/gookbon1.png");
  background-size: 80px 80px;
  width: 80px;
  height: 80px;
  left: 60%;
  top: 80%;
  font-size: 80px;
  transform: rotate(-30deg);
  z-index: 2;
  animation: rotate 20s linear infinite;
  margin: 35px;
}
@keyframes rotate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
@keyframes rotate2 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(-360deg);
  }
}

.bubble:nth-child(1) {
  margin-left: -10%;
  margin-top: -24%;
}

@media (min-width: 1920px){
  .bubble:nth-child(1) {
    margin-left: -10%;
    margin-top: -15%;
  }
}
</style>
