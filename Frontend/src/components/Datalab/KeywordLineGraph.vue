<template>
  <!-- <loading-spinner v-if="this.getIsLineGraph" /> -->
  <div class="chart-container">
    <div v-show="this.test.getGraphKeyword != null">
      <vue3-chart-js
        :id="lineChart.id"
        ref="chartRef"
        :type="lineChart.type"
        :data="lineChart.data"
        :options="lineChart.options"
        width="400"
        height="280"
      ></vue3-chart-js>
    </div>

    <!-- {{lineChart.data.datasets[0].data.length}} -->

    <!-- <button @click="updateChart">Update Chart</button> -->
  </div>
</template>

<script>
import { ref, computed } from "vue";
import { mapGetters, mapActions } from "vuex";
import Vue3ChartJs from "@j-t-mcc/vue3-chartjs";
import { useStore } from "vuex";
// import LoadingSpinner from "@/components/Datalab/LoadingSpinner.vue";
export default {
  components: {
    Vue3ChartJs,
    // LoadingSpinner,
  },
  setup() {
    const keywordlist = ref([]);
    const chartRef = ref(null);

    const lineChart = {
      display: false,
      type: "line",
      data: {
        labels: [],
        datasets: [
          {
            data: [],
          },
        ],
      },
      options: {
        display: false,
        animations: {
          display: false,
          y: {
            easing: "easeInOutElastic",
            from: (ctx) => {
              if (ctx.type === "data") {
                if (ctx.mode === "default" && !ctx.dropped) {
                  ctx.dropped = true;
                  return 0;
                }
              }
            },
          },
        },
        responsive: false,
        maintainAspectRatio: false,
        plugins: {
          display: false,
          labels: false,
          legend: {
            display: false,
          },
          // title: {
          //   text: "검색량 추이",
          //   display: true,
          // },
          datalabels: {
            display: false,
          },
        },
        borderColor: "rgb(0, 75, 107)",
        borderJoinStyle: "round",
        // spanGaps: true,
        // borderwidth: 30,
        // lineTension: 0,

        scales: {
          x: {
            grid: {
              display: false,
              drawBorder: false,
              drawOnChartArea: false,
              drawTicks: false,
            },
          },
        },
      },
    };

    const updateChart = (res) => {
      
      lineChart.options.plugins.title = {
        text: "날짜별 검색량",
        display: true,
        font: {
          size: 14,
          family: "KOTRA_BOLD-Bold",
          weight: "bold",
          color: "rgb(255, 255, 255)",
        },
      };
      lineChart.labels = res[0].name;
      lineChart.data.labels = [];
      lineChart.data.datasets = [
        {
          label: res[0].name,
          backgroundColor: "rgb(75, 192, 192)",
          data: [],
        },
      ];

      for (let i = 0; i < res.length; i++) {
        lineChart.data.labels[i] =
          res[i].date.toLocaleDateString().split(".")[1] +
          "/" +
          res[i].date.toLocaleDateString().split(".")[2];
        lineChart.data.datasets[0].data[i] = res[i].count;
      }
      chartRef.value.update(250);
    };
    const store = useStore();
    const test = computed(() => store.getters);
    return {
      keywordlist,
      lineChart,
      updateChart,
      chartRef,
      store,
      test,
    };
  },
  computed: {
    ...mapGetters([
      "getCurrentRank",
      "getConditionNation",
      "getConditionCategory",
      "getConditionPeriod",
      "getGraphKeyword",
      "getIsLineGraph",
    ]),
  },
  methods: {
    ...mapActions(["getGraphKeyword"]),
  },
  watch: {
    
    getCurrentRank: function () {
      if (this.getConditionCategory && this.getConditionPeriod) {
        const condition = {
          keyword: this.getCurrentRank,
          nation: this.getConditionNation,
          category: this.getConditionCategory,
          period: this.getConditionPeriod,
        };
        this.store.dispatch("getGraphKeyword", { condition });
      }
    },
    getGraphKeyword: function (data) {
      this.keywordlist = data;
      this.updateChart(data);
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
.chart-container {
  background: rgb(255, 255, 255, 0.4);
  height: 300px;
  /* opacity: 60%; */
  border-radius: 15px;
  margin-left: -20.5rem;
  margin-top: -6.8rem;
}
</style>
