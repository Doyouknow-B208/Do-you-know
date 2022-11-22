<template>
  <!-- <div class="navbar">
    <router-link to="/" class="nav-img">
      <img class="nav-logo" src="../../assets/logo.png" />
    </router-link>
    <div class="nav-menu">
      <router-link to="/datalab" class="nav-menu-item">데이터랩</router-link>
      <router-link to="/game" class="nav-menu-item">더많이더적게</router-link>
      <router-link to="/DYKC" class="nav-menu-item">명예의전당</router-link>
    </div>
  </div> -->
  <div class="navbar-container">
    <img src="@/assets/logo.png" class="logo" @click.prevent="moveSlide(0)" />
    <div class="menu-container">
      <div class="background-one">
        <div class="link-container">
          <a class="link-one" @click.prevent="moveSlide(0)">DataLab</a>
        </div>
      </div>
      <div class="background-two link-container">
        <a class="link-two" @click.prevent="moveSlide(1)">DYKClub</a>
      </div>
      <div class="background-three link-container">
        <a class="link-three" @click.prevent="moveSlide(2)">Game</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    swiper: Object, // swiper 인스턴스 받기
  },

  setup(props) {
    const moveSlide = (index) => {
      props.swiper.slideTo(index, 1000, false);
    };

    return {
      moveSlide,
    };
  },
};
</script>

<style scoped>
.logo {
  border: 0;
  width: 5vw;
  height: auto;
  margin: 10px 0 0 10px;
  cursor: pointer;
}

body {
  margin: 0;
  height: 100vh;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 1fr;
}
.navbar-container {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
  z-index: 3;
  position: fixed;
}
.menu-container {
  display: flex;
  margin: 0 3% 0 0;
}

.background-one {
  /* background-color: #151515; */
  background-color: transparent;
}

.background-two {
  /* background-color: #151515; */
  background-color: transparent;
}

.background-three {
  background-color: transparent;
}

.link-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
  position: relative;
  z-index: 0;
  margin: 0 30px;
}

a {
  font-family: "Bungee", cursive;
  font-size: 2.5em;
  cursor: pointer;
}

.link-one {
  color: #53d9d1;
  transition: color 1s cubic-bezier(0.32, 0, 0.67, 0);
  line-height: 1em;
}

.link-one:hover {
  color: #111;
  transition: color 1s cubic-bezier(0.33, 1, 0.68, 1);
}

.link-one::before {
  content: "";
  position: absolute;
  z-index: -1;
  width: 100%;
  height: 100%;
  top: 0;
  right: 0;
  background-color: #53d9d1;

  clip-path: circle(0% at 50% calc(50%));
  transition: clip-path 1s cubic-bezier(0.65, 0, 0.35, 1);
}

.link-one:hover::before {
  clip-path: circle(100% at 50% 50%);
}

.link-two {
  color: #f1c56c;
  transition: color 1s cubic-bezier(0.32, 0, 0.67, 0);
  line-height: 1em;
}

.link-two:hover {
  color: #111;
  transition: color 1s cubic-bezier(0.33, 1, 0.68, 1);
}

.link-two::before {
  content: "";
  position: absolute;
  z-index: -1;
  width: 100%;
  height: 100%;
  top: 0;
  right: 0;
  background-color: #f1c56c;

  clip-path: circle(0% at 50% calc(50%));
  transition: clip-path 1s cubic-bezier(0.65, 0, 0.35, 1);
}

.link-two:hover::before {
  clip-path: circle(100% at 50% 50%);
}

.link-three {
  color: #899cff;
  transition: color 1s cubic-bezier(0.32, 0, 0.67, 0);
  line-height: 1em;
}

.link-three:hover {
  color: #111;
  transition: color 1s cubic-bezier(0.33, 1, 0.68, 1);
}

.link-three::before {
  content: "";
  position: absolute;
  z-index: -1;
  width: 100%;
  height: 100%;
  top: 0;
  right: 0;
  background-color: #899cff;

  clip-path: circle(0% at 50% calc(50%));
  transition: clip-path 1s cubic-bezier(0.65, 0, 0.35, 1);
}

.link-three:hover::before {
  clip-path: circle(100% at 50% 50%);
}

.link-one-active {
  text-decoration: underline;
  text-decoration-style: wavy;
}

.link-two-active {
  text-decoration: underline;
  text-decoration-style: wavy;
}

.link-three-active {
  text-decoration: underline;
  text-decoration-style: wavy;
}
</style>
