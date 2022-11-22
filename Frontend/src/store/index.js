import { createStore } from "vuex";
import { datalab } from "@/store/modules/datalab";
import { dykc } from "@/store/modules/dykc";
import { game } from "@/store/modules/game";
import createPersistedState from "vuex-persistedstate";

export default createStore({
  modules: { datalab, dykc, game },
  plugins: [
    createPersistedState({
      storage: window.sessionStorage,
      paths: ["dykc"],
    }),
  ],
});
