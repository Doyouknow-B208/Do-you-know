import BackendAPI from "@/api/BackendAPI";
import axios from "axios";

export const dykc = {
  state: {
    //DYKC
    sport : null,
    drama : null,
    movie : null,
    entertainer : null,
    
    // 트위터
    twitter : null,
    // translate: null,
  },

  getters: {
    //DYKC
    sport : state => state.sport,
    drama : state => state.drama,
    movie : state => state.movie,
    entertainer : state => state.entertainer,
    
    //트위터
    twitter : state => state.twitter,
  },

  mutations: {
    //DYKC
    SET_SPORT: (state, sport) => state.sport = sport,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_DRAMA: (state, drama) => state.drama = drama,
    SET_ENTERTAINER: (state, entertainer) => state.entertainer = entertainer,
    
    // 트위터
    SET_TWITTER: (state, twitter) => state.twitter = twitter,

  },

  actions: {
    //DYKC
    fetchSport({ commit }, keyword) {
      axios({
        url: BackendAPI.dykc.DYKC(keyword),
        method: 'get',
      })
        .then(res => {
          commit('SET_SPORT', res.data)
      })
        .catch(err => {
          console.error(err.response)
        })
    },
    fetchMovie({ commit }, keyword) {
      axios({
        url: BackendAPI.dykc.DYKC(keyword),
        method: 'get',
      })
        .then(res => {
          commit('SET_MOVIE', res.data)
      })
        .catch(err => {
          console.error(err.response)
        })
    },
    fetchDrama({ commit }, keyword) {
      axios({
        url: BackendAPI.dykc.DYKC(keyword),
        method: 'get',
      })
        .then(res => {
          commit('SET_DRAMA', res.data)
      })
        .catch(err => {
          console.error(err.response)
        })
    },
    fetchEntertainer({ commit }, keyword) {
      axios({
        url: BackendAPI.dykc.DYKC(keyword),
        method: 'get',
      })
        .then(res => {
          commit('SET_ENTERTAINER', res.data)
      })
        .catch(err => {
          console.error(err.response)

        })
        .catch((err) => {
          console.error(err.response);
        });
    },

    
    // 트위터
    fetchTwitter({ commit }, name) {
      axios({
        url: BackendAPI.dykc.twitter(name),
        method: 'get',
      })
        .then(res => {
          commit('SET_TWITTER', res.data)
      })
        .catch(err => {
          console.error(err.response)

        })
        .catch((err) => {
          console.error(err.response);
        });
    },
  }
}
