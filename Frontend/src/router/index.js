import { createRouter, createWebHistory } from "vue-router";
import MainPage from "../views/MainPage.vue";
import GamePage from "../views/GamePage.vue";
import GamePlay from "../views/GamePlay.vue";
import GameEnding from "../views/GameEnding.vue";

// DYKC
import DYKCView from "../views/DYKC/DYKCView.vue";
import AwardIntroView from "../views/DYKC/AwardIntroView.vue";
import AwardView from "../views/DYKC/AwardView.vue";

const routes = [
  {
    path: "/",
    name: "MainPage",
    component: MainPage,
  },
  {
    path: "/game",
    name: "GamePage",
    component: GamePage,
  },
  {
    path: "/game-playing",
    name: "GamePlay",
    component: GamePlay,
  },
  {
    path: "/gameend",
    name: "GameEnding",
    component: GameEnding,
  },

  // DYKC
  {
    path: "/DYKC",
    name: "DYKC",
    component: DYKCView,
  },
  {
    path: "/awardintro",
    name: "awardintro",
    component: AwardIntroView,
  },
  {
    path: "/award",
    name: "award",
    component: AwardView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
