<template>
  <img src="../../assets/DYKC/twitter_mark.png" alt="">
  <div class="pull">
    <p class="content" v-show="trans==false">
      {{twitter.content}}
    </p>
    <p class="content" v-show="trans==true">
      {{ment}}
    </p>
  </div>
  <div @click="twittertranslate()">
    <img src="../../assets/DYKC/translateicon.png" class="translatebtn">
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    props: ["twitter", "index", "name"],
    data(){
      return {
        trans : false,
        ment : [],
        keyword: this.name,
        num: this.index,
      }
    },
    mounted(){
      this.setKeyword();
    },
    methods:{
      setKeyword(){
        const API_URL = `https://j7b208.p.ssafy.io/api2/pytranslate/usually/${this.keyword}/${this.num}/`
        axios.get(API_URL)
          .then(res => {
            this.ment = res.data
          })
      },  
      twittertranslate(){
        if (this.trans == true){
          this.trans = false;
        } else {
          this.trans = true;
        }
      },
    },
  }
</script>

<style scoped>
  @font-face {
    font-family: 'TTCrownMychewR';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2205@1.0/TTCrownMychewR.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
  }

  img{
    margin: 1rem;
    width: auto;
    height: 3rem;
  }
  .translatebtn{
    width: 2rem;
    height: auto;
    margin-left: 0;
  }
  .translatebtn:hover{
    transform: scale(1.2);
  }
  .pull {
    position:relative;
    padding: 1rem; 
    width:80%;
    height:auto; 
    color: black; 
    border-radius: 10px; 
    background-color: #ffdfae5c;
  }
  .pull:after {
    content:""; 
    position: absolute;
    top: 40%;
    right: 100%;
    border-right: 30px solid #ffdfae5c;
    border-top: 10px solid transparent;
    border-bottom: 10px solid transparent;
  }
  .content{
    font-size: 1.5rem;
    text-align : left;
    margin-top: 0;
    font-family: 'TTCrownMychewR';
  }
</style>