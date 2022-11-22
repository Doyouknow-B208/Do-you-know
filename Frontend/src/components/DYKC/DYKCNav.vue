<template>
  <div class="navbar">
    <a href="https://j7b208.p.ssafy.io/" class="nav-img">
      <img src="@/assets/logo.png" alt="logo" class="nav-logo" />
    </a>
    <div class="nav-menu">
      <a
        href="https://j7b208.p.ssafy.io/"
        class="nav-menu-item"
        style="color: #53d9d1"
        >홈</a
      >
      <router-link to="/game" class="nav-menu-item" style="color: #eb7132"
        >더많이더적게</router-link
      >
    </div>
  </div>
</template>

<script></script>

<style scoped>
@font-face {
  font-family: "TTCrownMychewR";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2205@1.0/TTCrownMychewR.woff2")
    format("woff2");
  font-weight: normal;
  font-style: normal;
}
.nav-img {
  margin: 0;
}
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.nav-logo {
  border: 0;
  width: 5vw;
  height: auto;
  margin: 10px 0 0 10px;
}

.nav-menu {
  display: flex;
  font-size: 2em;
  margin: 0 30px;
}

.nav-menu-item {
  margin: 0 10px;
  text-decoration: none;
  color: white;
  position: relative;
  padding: 6px 12px;
  font-size: 2.5rem;
  font-family: "TTCrownMychewR";
}

.nav-menu-item::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 4px;
  background: #f1c40f;
  transition: all 0.5s ease-out;
}

.nav-menu-item:hover::after {
  width: 80%;
}
</style>
