<template>
  <div>
    <div class="keyword-container">
      <template v-for="nation in this.getNation" :key="nation.value">
        <button @click="setNation(nation.value)" :class="{'btn-common': true, 'btn-nation-active' : ActiveNation[nation.value-1] === true}">
          {{ nation.text }}
        </button>
      </template>
      <br />
      <template v-for="category in this.getCategory" :key="category.value">
        <!-- <input id="tab1" type="radio" name="tabs" checked />
        <label for="tab1">{{ category.text }}</label> -->
        <button @click="setCategory(category.value)" :class="{'btn-common': true, 'btn-category-active' : CategoryNo === category.value}">
          {{ category.text }}
        </button>
      </template>
      <br />
      <template v-for="period in this.getPeriod" :key="period.value">
        <button @click="setPeriod(period.value)" :class="{'btn-common': true, 'btn-period-active' : PeriodNo === period.value}">{{ period.text }}</button>
      </template>

      <!-- <section id="content1"> -->
      <template v-for="(keyword, index) in this.getKeywordRank" :key="keyword">
        <template v-if="index < 5">
          <div @click="setOneKeyword(keyword.name)">{{ keyword.name }}</div>
        </template>
      </template>
      <!-- </section> -->
    </div>
  </div>
</template>

<script>
import { useStore, mapGetters } from "vuex";
import { onMounted } from "vue";
// import { useRoute } from "vue-router";
export default {
  setup() {
    let ActiveNation = [false, false, false, false, false, false]
    // let ActiveCategory = [false, false, false, false, false, false]
    // let ActivePeriod = [false, false, false, false, false, false]

    const store = useStore();
    onMounted(() => {});

    const setNation = function setNation(nation) {
      if (ActiveNation[nation-1] === false){
        ActiveNation[nation-1] = true
      } else {
        ActiveNation[nation-1] = false
      }
      store.dispatch("setNation", { nation });
    };
    const setCategory = function setCategory(category) {
      store.dispatch("setCategory", { category });
    };
    const setPeriod = function setPeriod(period) {
      store.dispatch("setPeriod", { period });
    };
    const setOneKeyword = function setOneKeyword(keyword) {
      store.dispatch("currentRank", { keyword });
    };

    
    // const rank1 = function (e) {
    //   e = rankDrama[0].title;
    
    //   const keyword = e;
    //   store.dispatch("currentRank", { keyword });
    // };
  
    return {
      // rank1,
      setNation,
      setCategory,
      setPeriod,
      setOneKeyword,
      store,
      // data,
      ActiveNation,
    };
  },
  computed: {
    ...mapGetters([
      "getConditionNation",
      "getConditionCategory",
      "getConditionPeriod",
      "getNation",
      "getCategory",
      "getPeriod",
      "getKeywordRank",
    ]),
  },
  watch: {
    getConditionNation: function () {
      if (this.getConditionCategory && this.getConditionPeriod) {
        const condition = {
          nation: this.getConditionNation,
          category: this.getConditionCategory,
          period: this.getConditionPeriod,
        };
        this.store.dispatch("getKeywordData", { condition });
      }
    },
    getConditionCategory: function () {
      if (this.getConditionNation && this.getConditionPeriod) {
        const condition = {
          nation: this.getConditionNation,
          category: this.getConditionCategory,
          period: this.getConditionPeriod,
        };
        this.store.dispatch("getKeywordData", { condition });
      }
    },
    getConditionPeriod: function () {
      if (this.getConditionCategory && this.getConditionNation) {
        const condition = {
          nation: this.getConditionNation,
          category: this.getConditionCategory,
          period: this.getConditionPeriod,
        };
        this.store.dispatch("getKeywordData", { condition });
      }
    },
  },
  // methods: {
  //   ...mapActions(["setNation", "setCategory", "setPeriod"]),
  // },
};
</script>

<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
.keyword-container {
  width: 27.75rem;
  height: 15rem;
  background-color: #e4e8ef;
  margin-left: 1.5rem;
  /* min-width: 320px;
  max-width: 800px; */
  padding: 0;
  background: #ffffff;
  border-radius: 15px;
}
p {
  margin: 0;
}
section {
  display: none;
  padding: 20px 0 0;
  /* border-top: 1px solid #ddd; */
}

/*라디오버튼 숨김*/
input {
  display: none;
}

label {
  display: inline-block;
  margin: 0 0 -1px;
  padding: 15px 25px;
  font-weight: 600;
  text-align: center;
  color: #bbb;
  border: 1px solid transparent;
  /* width: 35px; */
}

label:hover {
  color: #2e9cdf;
  cursor: pointer;
}

/*input 클릭시, label 스타일*/
input:checked + label {
  color: #555;
  border: 1px solid #ddd;
  border-top: 2px solid #2e9cdf;
  border-top-right-radius: 10px;
  border-top-left-radius: 10px;
  border-bottom: 1px solid #ffffff;
}
#tab1:checked ~ #content1,
#tab2:checked ~ #content2,
#tab3:checked ~ #content3,
#tab4:checked ~ #content4,
#tab5:checked ~ #content5 {
  display: block;
}
#content1,
#content2,
#content3,
#content4,
#content5 {
  margin-left: 3rem;
  padding: 0;
  padding-top: 0;
  padding-bottom: 0;
}

.btn-common {
  display: inline-block;
  padding: 5px 10px;
  border-radius: 15px;
  font-family: 'Jeju Gothic', sans-serif;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
  text-decoration: none;
  font-weight: 600;
  transition: 0.25s;
  margin: 5px 2px;
  background-color: aliceblue;
  color: #1e6b7b;
}

.btn-common:hover {
  transform: scale(1.2);
  cursor: pointer;
}

.btn-nation-active {
  /* background: linear-gradient(-45deg, #33ccff 0%, #ff99cc 100%);
  color: white; */
  background-color: #77af9c;
  color: #d7fff1;
}

.btn-category-active {
  background-color: #77af9c;
  color: #d7fff1;
}

.btn-period-active {
  background-color: #77af9c;
  color: #d7fff1;
}
</style>
