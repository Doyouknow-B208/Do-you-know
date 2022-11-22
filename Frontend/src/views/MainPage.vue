<template>
  <NavBar v-if="this.getIsOverlay == false" :swiper="swiper" />

  <swiper
    class="mySwiper"
    :modules="modules"
    :direction="'vertical'"
    :speed="1000"
    mousewheel
    :allowTouchMove="false"
    :lazy="{ loadPrevNext: true }"
    :pagination="!this.getIsOverlay"
  >
    <swiper-slide class="first"><IntroTop /></swiper-slide>
    <swiper-slide class="third"><IntroAwards /></swiper-slide>
    <swiper-slide class="forth"><IntroGame /></swiper-slide>
  </swiper>
</template>

<script>
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from "swiper/vue";

// Import Swiper styles
import "swiper/css";
import "swiper/css/bundle";

// import required modules
import { Navigation, Pagination, Mousewheel, Scrollbar } from "swiper";

import IntroTop from "@/components/Main/IntroTop.vue";
// import IntroDataLab from "@/components/Main/IntroDataLab.vue";
import IntroAwards from "@/components/Main/IntroAwards.vue";
import IntroGame from "@/components/Main/IntroGame.vue";
import NavBar from "@/components/Main/NavBar.vue";
import { mapGetters, useStore } from "vuex";

export default {
  components: {
    Swiper,
    SwiperSlide,
    IntroTop,
    // IntroDataLab,
    IntroAwards,
    IntroGame,
    NavBar,
  },
  data() {
    return {
      swiper: null,
    };
  },

  mounted() {
    const swiper = document.querySelector(".swiper").swiper; //swiper 인스턴스
    this.swiper = swiper;
  },

  setup() {
    const store = useStore();
    store.dispatch("OverlayReset");

    return {
      modules: [Navigation, Pagination, Mousewheel, Scrollbar],
    };
  },
  computed: {
    ...mapGetters(["getIsOverlay", "getNation", "getConditionNation"]),
  },

  watch: {
    getIsOverlay: function(){
      if (this.getIsOverlay){
        this.swiper.mousewheel.disable()
      } else{
        this.swiper.mousewheel.enable()
      }
    },
  }
};
</script>
<style>
#app {
  height: 100%;
}
html,
body {
  position: relative;
  height: 100%;
}

body {
  background: #eee;
  font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
  font-size: 14px;
  color: #000;
  margin: 0;
  padding: 0;
}

.swiper {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #fff;

  /* Center slide text vertically */
  display: -webkit-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  -webkit-justify-content: center;
  justify-content: center;
  -webkit-box-align: center;
  -ms-flex-align: center;
  -webkit-align-items: center;
  align-items: center;
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.first {
  /* background-color: #ffdfae; */
  background: linear-gradient(#fff0fddf, #fae3c2, #ffdfae);
}
.second {
  background: linear-gradient(#f5f7fa, #b8c6db);
}
.third {
  background: linear-gradient(#f1c56c, #dab097);
}
.forth {
  background: linear-gradient(#9d7eb8, #ddbdfc, #96c8fb);
}

/* .swiper-container { width: 100%; height: 100%; }
.swiper-slide { text-align: center; font-size: 18px; background: #fff; display: flex; justify-content: center; align-items: center; } */
.swiper-pagination-vertical {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.swiper-pagination-bullet {
  width: 12px;
  height: 12px;
  background: transparent;
  border: 1px solid #007aff;
  opacity: 1;
}

.swiper-pagination-bullet-active {
  width: 20px;
  height: 20px;
  transition: width 0.5s height 0.5s;
  border-radius: 100%s;
  background: #007aff;
  border: 1px solid transparent;
  outline: none;
  border-color: #9ecaed;
  box-shadow: 0 0 10px #9ecaed;
}
</style>
