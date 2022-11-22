<template>
  <div class="word-container">
    <div v-if="!this.getRelatedKewordLoading && this.getCurrentRank" class="wordcloud-title">연관검색어</div>
    <template v-if="this.getIsErrormsg && !this.getRelatedKewordLoading">
        <p class="ptag">다시 한 번 선택해 주세요.</p>
    </template>
    <loading-spinner v-if="this.getRelatedKewordLoading" />
    <div v-if="this.getRelatedKewordLoading">로딩 중...</div>
    <div class="canvas-container">
      <canvas id="canvas" style="width: 600px; height: 500px"></canvas>
    </div>
  </div>
</template>

<script>
import { mapGetters, useStore } from "vuex";
import { Chart } from "chart.js";
import { WordCloudController, WordElement } from "chartjs-chart-wordcloud";
import { ref } from "vue";
import LoadingSpinner from "@/components/Datalab/LoadingSpinner.vue";
export default {
  components: { LoadingSpinner },
  setup() {
    Chart.register(WordCloudController, WordElement);
    //const keywordlist = ref([]);
    const chartRef = ref(null);
    const store = useStore();
    const barChart = {
      id: "bar",
      type: "bar",
      data: {
        labels: [],
        datasets: [
          {
            backgroundColor: "#f87979",
            data: [],
          },
        ],
      },
      options: {
        responsive: false,
        maintainAspectRatio: false,
        plugins: {
          labels: false,
          legend: {
            display: false,
          },
          datalabels: {
            display: false,
          },
        },
      },
    };

    const updatewordcloud = (data) => {
      
      const color = [
        // "#004B6B",
        // '#255D7E',
        // "#3C6F8E",
        // '#5483A1',
        // "#6996B3",
        // '#7EAAC7',
        // "#94BDD9",
        // '#ABD3EC',
        // "#C1E6FF",
        // "#EBF2F7",

        "#88BCEE",
        "#90ED7D",
        "#8085E9",
        "#F7A35C",
        "#2B908F",
        "#F15C80",
        "#E4D354",
        "#FD0541",
        "#9EEAE4",
        "#4247C0",
        "#6D8DFF",

        "#CAFDC0",
        "#D1D3FC",
        "#FCD8BA",
        "#BEEEEE",
        "#CFE4F9",
        "#FCD6DF",
        "#E4F5CF",
        "#8160C6",
        "#794C57",
      ];

      

      var arr = [];
      for (let i = 0; i < data.length; i++) {
        if (data[i][0].length < 9) {
          arr.push(data[i]);
        }
      }
      let max = arr[0][1];
      let min = arr[arr.length - 1][1];
      const data1 = {
        labels: arr.map((d) => d[0]),
        datasets: [
          {
            label: "",
            // data: data.map((d, index) => 30 - index * 2),
            data: arr.map((d) => ((d[1] - min) / (max - min)) * 13 + 17),
            // data: arr.map((d) => ((d[1] - min)/ (max-min ))*10+20),
            color: arr.map((d, index) => color[index % 20]),
            family: "KOTRA_BOLD-Bold",
            pointHoverBackgroundColor: "#FD943C",
          },
        ],
      };
      

      {
        let chartStatus = Chart.getChart("canvas"); // <canvas> id
        if (chartStatus != undefined) {
          chartStatus.destroy();
        }
        const ctx = document.getElementById("canvas").getContext("2d");

        window.myBar = new Chart(ctx, {
          type: WordCloudController.id,
          data: data1,
          options: {
            plugins: {
              // title: {
              //   text: "연관검색어",
              //   display: true,
              //   font: {
              //     size: '36',
              //     family: 'KOTRA_BOLD-Bold',
              //     weight: "bold",
              //     color: "#ff6384",
                  
              //   },
                
              // },
              labels: false,
              legend: {
                display: false,
              },
              datalabels: {
                display: false,
              },
            },
          },
        });
      }
    };
    return {
      //keywordlist,
      updatewordcloud,
      barChart,
      chartRef,
      store,
    };
  },

  computed: {
    ...mapGetters([
      "getCurrentRank",
      "getRelatedKeyword",
      "getRelatedKewordLoading",
      "getIsErrormsg",
    ]),
  },
  // methods: {
  //   ...mapActions(["relatedkeyword"]),
  // },
  watch: {
    getCurrentRank: function (data) {
      let chartStatus = Chart.getChart("canvas"); // <canvas> id
      if (chartStatus != undefined) {
        chartStatus.destroy();
      }
      this.store.dispatch("relatedkeyword", { data });
    },
    getRelatedKeyword: function (data) {
      const data1 = data.splice(0, 25);
      this.updatewordcloud(data1);
    },
  },
};
</script>

<style scoped>
/* .word-container {
  height: 220px;
  width: 400px;
  background: white;
  opacity: 81%;
  border-radius: 30px;
} */
@font-face {
  font-family: "KOTRA_BOLD-Bold";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-10-21@1.1/KOTRA_BOLD-Bold.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
@font-face {
    font-family: 'GyeonggiTitleM';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/GyeonggiTitleM.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
.cha .chartvue {
  visibility: hidden;
}
.canvas-container {
  height: 185px;
  width: 394px;
  /* position: absolute;
  top: 3rem;
  right: -3rem; */
  margin-right: 4rem;
  /* background: white;
  opacity: 81%;
  border-radius: 30px; */
}
#canvas {
  height: 100%;
  width: 100%;
}
@font-face {
  font-family: "KOTRA_BOLD-Bold";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-10-21@1.1/KOTRA_BOLD-Bold.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}


.ptag {
  /* font-size: 2rem; */
  font-family: "KOTRA_BOLD-Bold";
   opacity: 71%;
}

.wordcloud-title {
  text-align: start;
  font-size: 35px;
  font-weight: bolder;
  font-family: 'GyeonggiTitleM';
}
</style>
