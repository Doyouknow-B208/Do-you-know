import axios from "axios";
import BackendAPI2 from "@/api/BackendAPI2";
// 안녕하세요!!
export const datalab = {
  state: {
    rank: null,
    currentrank: null,
    currentRankTrans: null,
    keywordrank: null,
    // relatedkeword: [],
    isoverlay: false,
    isRate: false,
    isTopFive: false,
    isLineGraph: false,
    iserrormsg: false,
    datalabviewloading: true,
    relatedkeword: [],
    relatedkeywordnews: [],
    relatedkewordloading: false,
    graphkeyword: null,
    TTS: null,
    category: [
      { value: 1, text: "운동선수" },
      { value: 2, text: "드라마" },
      { value: 3, text: "영화" },
      { value: 4, text: "가수" },
      { value: 5, text: "배우" },
    ],
    period: [
      { value: 0, text: "일주일" },
      { value: 1, text: "한달" },
      { value: 3, text: "세달" },
    ],
    nation: [
      { value: 1, text: "미국", lang: "en" },
      { value: 2, text: "영국", lang: "en" },
      { value: 3, text: "일본", lang: "ja" },
      { value: 4, text: "베트남", lang: "vi" },
      { value: 5, text: "인도네시아", lang: "id" },
      { value: 6, text: "브라질", lang: "pt" },
    ],
    nationRate: null,
    condition: {
      nation: null,
      category: null,
      period: null,
    },
  },
  getters: {
    getIsErrormsg(state){
      return state.iserrormsg;
    },
    getCurrentRank(state) {
      return state.currentrank;
    },
    getCurrentTrans(state) {
      return state.currentRankTrans;
    },
    getKeywordRank(state) {
      return state.keywordrank;
    },
    getRelatedKeyword(state) {
      return state.relatedkeword;
    },
    getRelatedKeywordNews(state) {
      return state.relatedkeywordnews;
    },
    getIsOverlay(state) {
      return state.isoverlay;
    },
    getIsRate(state) {
      return state.isRate;
    },
    getIsTopFive(state) {
      return state.isTopFive;
    },
    getIsLineGraph(state) {
      return state.isLineGraph;
    },
    getDatalabViewLoading(state) {
      return state.datalabviewloading;
    },
    getCondition(state) {
      return state.condition;
    },
    getConditionNation(state) {
      return state.condition.nation;
    },
    getConditionCategory(state) {
      return state.condition.category;
    },
    getConditionPeriod(state) {
      return state.condition.period;
    },
    getNation(state) {
      return state.nation;
    },
    getCategory(state) {
      return state.category;
    },
    getPeriod(state) {
      return state.period;
    },
    getNationRate(state) {
      return state.nationRate;
    },
    getGraphKeyword(state) {
      return state.graphkeyword;
    },
    getRelatedKewordLoading(state) {
      return state.relatedkewordloading;
    },
    getTTS(state) {
      return state.TTS;
    },
  },
  mutations: {
    SET_ISERRORMSG: (state, iserrormsg) => (state.iserrormsg = iserrormsg),
    SET_ISOVERLAY: (state, isoverlay) => (state.isoverlay = isoverlay),
    SET_ISRATE: (state, isRate) => (state.isRate = isRate),
    SET_ISTOPFIVE: (state, isTopFive) => (state.isTopFive = isTopFive),
    SET_ISLINEGRAPH: (state, isLineGraph) => (state.isLineGraph = isLineGraph),

    SET_DATALABVIEWLOADING: (state, datalabviewloading) => {
      state.datalabviewloading = datalabviewloading;
    },
    SET_CURRENTRANK: (state, keyword) => (state.currentrank = keyword),
    SET_CURRENTRANKTRANS: (state, keyword) =>
      (state.currentRankTrans = keyword),
    SET_KEYWORDRANK: (state, data) => (state.keywordrank = data),
    RESET_KEYWORDRANK: (state) => (state.keywordrank = null),
    SET_RELATEDKEWORD: (state, keywords) => (state.relatedkeword = keywords),
    SET_RELATEDKEYWORDNEWS: (state, news) => (state.relatedkeywordnews = news),
    SET_NATION: (state, nation) => (state.condition.nation = nation),
    SET_CATEGORY: (state, category) => (state.condition.category = category),
    SET_PERIOD: (state, period) => (state.condition.period = period),
    SET_NATIONRATE: (state, nationRate) => (state.nationRate = nationRate),
    SET_GRAPHKEYWORD: (state, graphkeyword) => {
      state.graphkeyword = [];
      graphkeyword.forEach((keyword) => {
        keyword.date = new Date(keyword.date);
        state.graphkeyword.push(keyword);
      });
      // state.graphkeyword = graphkeyword;
    },
    SET_RELATEDKEYWORDLOADING: (state, relatedkewordloading) => {
      state.relatedkewordloading = relatedkewordloading;
    },
    SET_TTS: (state, TTS) => {
      state.TTS = TTS;
    },
    SET_OVERLAYRESET: (state) => {
      state.condition.nation = null;
      state.condition.category = null;
      state.condition.period = null;
      state.isoverlay = false;
    },
    // (state.graphkeyword = graphkeyword),
  },
  actions: {
    async setIsOverlay({ commit }, { data }) {
      await commit("SET_ISOVERLAY", data);
    },
    async OverlayReset({ commit }) {
      await commit("SET_OVERLAYRESET");
    },
    async getNationRate({ commit }, { nation }) {
      await commit("SET_ISRATE", true);
      await axios
        .get(`https://j7b208.p.ssafy.io/api/keyword/searchcount/${nation}`)
        .then((res) => {
          commit("SET_ISRATE", false);
          commit("SET_NATIONRATE", res.data);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    async currentRank({ commit }, { keyword }) {
      await commit("SET_CURRENTRANK", keyword);
    },
    async setNation({ commit }, { nation }) {
      await commit("SET_NATION", nation);
    },
    async setCategory({ commit }, { category }) {
      await commit("SET_CATEGORY", category);
    },
    async setPeriod({ commit }, { period }) {
      await commit("SET_PERIOD", period);
    },

    async resetKeyword({ commit }) {
      await commit("RESET_KEYWORDRANK");
    },

    async getKeywordData({ commit }, { condition }) {
      await commit("SET_ISTOPFIVE", true);
      
      await axios
        .get(
          `https://j7b208.p.ssafy.io/api/keyword/${condition.nation}/${condition.category}/${condition.period}`
        )
        .then((res) => {
          commit("SET_ISTOPFIVE", false);
          commit("SET_KEYWORDRANK", res.data);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },

    async getGraphKeyword({ commit }, { condition }) {
      await commit("SET_ISLINEGRAPH", true);
      await axios
        .get(
          `https://j7b208.p.ssafy.io/api/keyword/keywordgraph/${condition.keyword}/${condition.nation}/${condition.category}/${condition.period}`
        )
        .then((res) => {
          
          commit("SET_ISLINEGRAPH", false);
          commit("SET_GRAPHKEYWORD", res.data);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },

    async relatedkeyword({ commit }, keyword) {
      commit("SET_RELATEDKEYWORDLOADING", true);
      commit("SET_ISERRORMSG", false);
      await axios({
        url: BackendAPI2.datalab.relatedkeyword(keyword.data),
        method: "get",
      })
        .then((res) => {
          commit("SET_RELATEDKEYWORDLOADING", false);
          commit("SET_RELATEDKEWORD", res.data);
        })
        .catch((err) => {
          commit("SET_RELATEDKEYWORDLOADING", false);
          commit("SET_ISERRORMSG", true);
          console.error(err.response);
        });
    },

    async TTSTranslate({ commit }, condition) {
      
      await axios({
        url: `https://j7b208.p.ssafy.io/api2/pytranslate/detail/${condition.keyword}/${condition.nation}/`,
        method: "get",
      })
        .then((res) => {
          commit("SET_TTS", res.data);
        })
        .catch((err) => {
          console.error(err.response);
        });
    },

    async getTranslateKeyword({ commit, state }, data) {
      
      await axios({
        url: BackendAPI2.datalab.relatedkeywordtranslate(
          data[1],
          state.nation[data[0].nation - 1].lang
        ),
        method: "get",
      })
        .then((res) => {
          commit("SET_CURRENTRANKTRANS", res.data);
        })
        .catch((err) => {
          console.error(err.response);
          // lang = 'ko';
        });
    },


    async relatedkeywordnews({ commit }, data) {
      // console.log(data[0].category, data[0].nation);
      var keyword = data[1];
      console.log("news--------------------------");
      var nation_id =data[0].nation;
      //console.log(data[]);
      
      console.log(nation_id);
      console.log(keyword);

      await axios({
        // &language=${lang}
        url: `https://j7b208.p.ssafy.io/api2/pytranslate/news/${keyword}/${nation_id}/`,
        method: "get",
      })
        .then((res) => {

          // console.log(res.data.articles.length)
          console.log("어디까지 갔니");
          console.log(res);
          console.log(res.data);
          commit("SET_RELATEDKEYWORDNEWS", res.data);
          

          // commit("SET_RELATEDKEYWORDNEWS", res.data.articles);
        })
        .catch((err) => {
          console.error(err.response);
        });
    },
  },
};
