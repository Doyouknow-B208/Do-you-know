<template>
  <div class="doughnut-container">
    <vue3-chart-js
      :id="lineChart.id"
      ref="chartRef"
      :type="lineChart.type"
      :data="lineChart.data"
      :options="lineChart.options"
      :width="300"
    ></vue3-chart-js>
  </div>
</template>

<script>
import { ref } from "vue";
import { mapGetters } from "vuex";
import Vue3ChartJs from "@j-t-mcc/vue3-chartjs";
import { useStore } from "vuex";
import { Chart } from "chart.js";
import ChartDataLabels from "chartjs-plugin-datalabels";
export default {
  components: {
    Vue3ChartJs,
  },
  setup() {
    Chart.register(ChartDataLabels);
    var COLORS = [
      "#004B6B",
      "#255D7E",
      "#3C6F8E",
      "#5483A1",
      "#6996B3",
      "#7EAAC7",
      "#94BDD9",
      "#ABD3EC",
      "#C1E6FF",
      "#EBF2F7",
      // '#B3CBF5',
      // '#BAD0F6',
      // '#C0D4F5',
      // '#C7D8F6',
      // '#CDDCF5',
      // '#D4E1F6',
      // '#DBE4F5',
      // '#E2E9F6',
      // '#E8EDF5',
      // '#EFF1F6'
    ];

    const keywordlist = ref([]);
    const chartRef = ref(null);

    const lineChart = {
      type: "doughnut",
      data: {
        labels: [],
        datasets: [
          {
            data: [],
          },
        ],
      },
      options: {
        responsive: false,
        // maintainAspectRatio: false,
        plugins: {
          labels: false,
          legend: {
            display: false,
          },
          datalabels: {
            display: true,
            font: {
              size: 11,
              family: "KOTRA_BOLD-Bold",
            },
            formatter: (val, ctx) => {
              // Grab the label for this value
              const label = ctx.chart.data.labels[ctx.dataIndex];

              // Format the number with 2 decimal places
              const formattedVal = Intl.NumberFormat("en-US", {
                // minimumFractionDigits: 2,
              }).format(val);

              // Put them together
              if (ctx.dataIndex >= 8) {
                return "";
              } else {
                return `${label} \n ${formattedVal}`;
              }
            },
            color: "#fff",
            // backgroundColor: '#404040',
          },
        },
      },
    };
    const updateChart = (res) => {
      lineChart.options.plugins.title = {
        text: "탑10 검색어",
        display: true,
        font: {
          size: 14,
          family: "KOTRA_BOLD-Bold",
          weight: "bold",
          color: "rgb(255, 255, 255)",
        },
      };
      lineChart.data.labels = [];
      lineChart.data.datasets = [
        {
          label: res[0].name,
          data: [],
          backgroundColor: [],
        },
      ];

      // console.log(lineChart.data.datasets[0].data.font);
      for (let i = 0; i < 10; i++) {
        lineChart.data.labels[i] = res[i].name;
        lineChart.data.datasets[0].data[i] = res[i].count;
        lineChart.data.datasets[0].backgroundColor[i] = COLORS[i];
      }
      chartRef.value.update(250);
    };
    const store = useStore();
    return {
      keywordlist,
      lineChart,
      updateChart,
      chartRef,
      store,
    };
  },
  computed: {
    ...mapGetters(["getCurrentRank", "getKeywordRank"]),
  },
  watch: {
    getKeywordRank: function (data) {
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
.doughnut-container {
  /* background: rgb(255, 255, 255, 0.1); */
  width: 100%;
  height: 478px;
  margin-left: 5%;
  margin-top: 4rem;
  /* background: rgba(255, 255, 255, 0.70);
  box-shadow: 0px 4px 10px rgba(81, 77, 77, 0.25);
  border-radius: 20px; */
}

/* .cloud-container {
  width: 30rem;
  height: 30rem;
  background: #e4e8ef;
  margin-left: 1rem;
  margin-bottom: 1.5rem;
} */
@media (min-width: 1920px) {
  .doughnut-container {

    width: 100%;
    height: 360px;
    margin-left: 5%;
    margin-top: 12rem;
    
  }
}
</style>
