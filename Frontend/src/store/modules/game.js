import axios from "axios";

export const game = {
  state: {
    gamedata: [],
  },
  getters: {
    getGameData(state) {
      
      return state.gamedata;
    },
  },
  mutations: {
    // SET_GAMEDATA: (state) => (state.gamedata = state),
    SET_GAMEDATA(state, data) {
      
      state.gamedata = data;
      
    },
  },
  actions: {
    setGameData({ commit }) {
      axios
        .get(`https://j7b208.p.ssafy.io/api/higherlower`)
        .then((res) => {
          commit("SET_GAMEDATA", res.data);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    setGameData1() {
      return axios.get(`https://j7b208.p.ssafy.io/api/higherlower`);
    },
  },
};
