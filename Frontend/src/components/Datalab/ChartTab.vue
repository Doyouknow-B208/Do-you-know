<template>
  <div class="chart-container">
    <vue3-chart-js
      :id="lineChart.id"
      ref="chartRef"
      :type="lineChart.type"
      :data="lineChart.data"
      :options="lineChart.options"
    ></vue3-chart-js>

    <button @click="updateChart">Update Chart</button>
  </div>
  <div></div>
</template>

<script>
import { ref } from "vue";
import { mapGetters, mapActions } from "vuex";
import Vue3ChartJs from "@j-t-mcc/vue3-chartjs";
import { useStore } from "vuex";

export default {
  components: {
    Vue3ChartJs,
  },
  setup() {
    const keywordlist = ref([]);
    const chartRef = ref(null);

    const lineChart = {
      id: "line",
      type: "line",
      data: {
        label: [],
        datasets: [
          {
            backgroundColor: "#f87979",
            data: [],
          },
        ],
      },
      options: {
        labels: false,
        legend: {
          display: false,
        },
        tooltips: {
          callbacks: {
            label: function (tooltipItem) {
              return tooltipItem.yLabel;
            },
          },
        },
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          datalabels: {
            display: false,
            backgroundColor: "#404040",
          },
          title: {
            text: "검색량 추이",
            display: true,
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
          backgroundColor: "#f87979",
          data: [],
        },
      ];

      for (let i = 0; i < res.length; i++) {
        
        lineChart.data.labels[i] = res[i].date.toLocaleDateString();
        lineChart.data.datasets[0].data[i] = res[i].count;
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
    ...mapGetters([
      "getCurrentRank",
      "getConditionNation",
      "getConditionCategory",
      "getConditionPeriod",
      "getGraphKeyword",
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
.chart-container {
  width: 33rem;
  height: 16rem;
  background: #ffffff;
  border-radius: 15px;
  margin-left: 1.5rem;
  margin-top: 1rem;
}
</style>
