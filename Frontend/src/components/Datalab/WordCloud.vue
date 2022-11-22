<template>
  <div class="cloud-container">
    <vue3-chart-js
      :id="lineChart.id"
      ref="chartRef"
      :type="lineChart.type"
      :data="lineChart.data"
      :options="lineChart.options"
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
      "#4dc9f6",
      "#f67019",
      "#f53794",
      "#537bc4",
      "#acc236",
      "#166a8f",
      "#00a950",
      "#58595b",
      "#8549ba",
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
        // responsive: true,
        // maintainAspectRatio: false,
        plugins: {
          labels: false,
          legend: {
            display: false,
          },
          datalabels: {
            display: true,
            formatter: (val, ctx) => {
              // Grab the label for this value
              const label = ctx.chart.data.labels[ctx.dataIndex];

              // Format the number with 2 decimal places
              const formattedVal = Intl.NumberFormat("en-US", {
                // minimumFractionDigits: 2,
              }).format(val);

              // Put them together
              return `${label} : ${formattedVal}`;
            },
            color: "#fff",
            // backgroundColor: '#404040',
          },
        },
      },
    };

    const updateChart = (res) => {
      lineChart.options.plugins.title = {
        text: "검색량 추이",
        display: true,
      };

      lineChart.data.labels = [];
      lineChart.data.datasets = [
        {
          label: res[0].name,
          data: [],
          backgroundColor: [],
        },
      ];

      for (let i = 0; i < 10; i++) {
        
        lineChart.data.labels[i] = res[i].name;
        lineChart.data.datasets[0].data[i] = res[i].count;
        lineChart.data.datasets[0].backgroundColor[i] = COLORS[i % 5];
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
.cloud-container {
  width: 30rem;
  height: 30rem;
  background: #e4e8ef;
  margin-left: 1rem;
  margin-bottom: 1.5rem;
}
</style>
