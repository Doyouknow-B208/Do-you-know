<template>
  <div class="bg">
    <video muted autoplay loop>
      <source src="../../assets/DYKC/intro.mp4" type="video/mp4">
    </video>

    <div>
      <img class="img" src="../../assets/DYKC/leftleaf.png" style="transform: rotate(330deg);">
    </div>
    <div class="main">
        <transition class="animate__animated animate__zoomIn">
          <div class="title">
              <h1 style="margin:0;">DoYouKnow</h1>
              <h1 style="margin:0;">Club</h1>
          </div>
        </transition>
      <button class="button" @click="Award()">
        <img class="btn_img" src="../../assets/DYKC/trophy.png"/>
      </button>
    </div>
    <div>
      <img class="img" src="../../assets/DYKC/rightleaf.png" style="transform: rotate(30deg);">
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return{
      show:true,
    }
  },
  methods: {
    Award() {
      this.$router.push('/awardintro');
    }
  },
}
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Bungee+Spice&family=Lobster&family=Rowdies&family=Supermercado+One&display=swap');
  @import "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css";
 
 video {
    position: fixed; right: 0; bottom: 0;
    min-width: 100%; min-height: 100%;
    width: auto; height: auto; z-index: -100;
    background-size: cover;
  }
  .bg {
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
  }
  .main{
    display: flex;
    flex-direction: column;
  }
  .title {
    color: bisque;
    font-size: xxx-large;
    text-align : center;
    font-family: 'Lobster', cursive;
  }
  .button{
    background-color: unset;
    border: 0;
    outline: 0;
    margin: 3rem;
  }
  .img{
    width: 15rem;
    height: auto;
  }
  .btn_img:hover{
    transform: scale(1.2);
  }
</style>