<template>
  <loading-spinner v-if="this.getIsRate" class="data-info-spinner"/>
  <template v-else>
    <div class="total-container" v-if="this.getNationRate">
      <div class="sub1-box">
        <div class="first_box">총 데이터</div>
        <div class="second_box">
          전체 데이터의 {{ this.getNationRate.nationRate }}%
        </div>
      </div>
      <div class="sub2-box">
        <span class="half-highlight"
          >{{ this.getNationRate.nationCount.toLocaleString("ko-KR") }}개</span
        >
      </div>
    </div>
  </template>
</template>

<script>
import { mapGetters, useStore } from "vuex";
import LoadingSpinner from "@/components/Datalab/LoadingSpinner.vue";
export default {
  components: { LoadingSpinner },
  setup() {
    const store = useStore();
    return {
      store,
    };
  },
  computed: {
    ...mapGetters([
      "getConditionNation",
      "getNation",
      "getNationRate",
      "getIsRate",
    ]),
  },
  watch: {
    getConditionNation: function (nation) {
      this.store.dispatch("getNationRate", { nation });
    },
  },
};
</script>

<style>
@font-face {
  font-family: "SF_IceLemon";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2106@1.1/SF_IceLemon.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "HS-Regular";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2201-2@1.0/HS-Regular.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "establishRoomNo703OTF";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2112@1.0/establishRoomNo703OTF.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
.total-container {
  display: flex;
  flex-direction: column;
  margin-left: 1rem;
  margin-right: 1rem;
  background: white;
  border-radius: 30px;
  opacity: 71%;
  padding: 0.75rem;
  margin-top: -1.5rem;
  width: 110%;
}
.sub1-box {
  display: flex;
  justify-content: space-around;
  align-items: flex-end;
  margin-bottom: 1rem;
}
.sub2-box {
  font-size: 2rem;
  font-family: "KOTRA_BOLD-Bold";
}
.half-highlight {
  background: linear-gradient(180deg, rgba(255, 255, 255, 0) 80%, #6495ed 50%);
}
.first_box {
  font-size: 1.5rem;
  font-family: "KOTRA_BOLD-Bold";
}
.second_box {
  background-color: white;
  border-radius: 15px;
  font-family: "establishRoomNo703OTF";
}
.data-info-spinner {
  width: 110%;
}
@media (min-width: 1920px){
  .data-info-spinner {
    width: 125%;
  }
}
</style>
