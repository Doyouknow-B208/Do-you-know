<template>
  <div class="black-bg" v-if="youtube == true" @click="youtubeClose($event)">
    <div class="white-bg">

      <h1 style="text-align : center; font-size: 2.5rem; font-family: 'SDSamliphopangche_Outline';">{{youtubeName}}</h1>
      <YoutubeCardmodal v-bind:name="youtubeName"/>
      <button class="close2">close</button>

    </div>
  </div>

  <div class="black-bg" v-if="twitter == true" @click="twitterClose($event)">
    <div class="white-bg">

      <h1 style="text-align : center; font-size: 2.5rem; margin-bottom:1rem; font-family: 'SDSamliphopangche_Outline';">해외 트위터 반응</h1>
      <TwitterCardmodal v-bind:name="twitterName"/>
      <button class="close2">close</button>
    </div>
  </div>

  <div class="black-bg" v-if="profile == true" @click="profileClose($event)">
    <div class="white-bg">
      <h1 style="text-align : center; font-size: 2.5rem; margin-bottom:1rem; font-family: 'SDSamliphopangche_Outline';">프로필</h1>
      <ProfileCardmodal v-bind:name="profileName"/>
      <button class="close2">close</button>
    </div>
  </div>

  <div class="black-bg" v-if="award == true" @click="awardClose($event)">
    <div class="white-bg">
      <h1 style="text-align : center; font-size: 2.5rem; margin-bottom:1rem; font-family: 'SDSamliphopangche_Outline';">수상 내역</h1>
      <AwardCardmodal v-bind:name="awardName"/>
      <button class="close2">close</button>

    </div>
  </div>

  <video class="videoPlay" muted autoplay loop>
    <source src="../../assets/DYKC/award.mp4" type="video/mp4" />
  </video>

  <div v-if="youtube===false && twitter===false && isShowing===true">
    <audio id="myAudio" autoplay loop onloadstart="this.volume=0.3">
      <source src="../../assets/DYKC/BGM.mp3" type="audio/mp3">
    </audio>
  </div>


  <div v-show="youtube===false && twitter===false && award===false && profile===false">
    <DYKCNav/>

    <div>
      <div v-show="isShowing === true">
        <img
          class="soundbtn"
          src="../../assets/DYKC/soundon.png"
          @click="sound()"
        />
      </div>
      <div v-show="isShowing === false">
        <img
          class="soundbtn"
          src="../../assets/DYKC/soundoff.png"
          @click="sound()"
        />
      </div>
    </div>

    <div class="main">
      <ul class="category">
        <li>

          <button v-if="keyword==='운동선수'" @click="changeKeyword('운동선수'), changecategory(1)">운동선수</button>
          <button v-else @click="changeKeyword('운동선수'), changecategory(1)">운동선수</button>

        </li>
        <li>
          <button v-if="keyword==='드 라 마'" @click="changeKeyword('드 라 마'), changecategory(2)">드 라 마</button>
          <button v-else @click="changeKeyword('드 라 마'), changecategory(2)">드 라 마</button>
        </li>
        <li>
          <button v-if="keyword==='영    화'" @click="changeKeyword('영    화'), changecategory(3)">영      화</button>
          <button v-else @click="changeKeyword('영    화'), changecategory(3)" >영      화</button>
        </li>
        <li>
          <button v-if="keyword==='연 예 인'" @click="changeKeyword('연 예 인'), changecategory(4)">연 예 인</button>
          <button v-else @click="changeKeyword('연 예 인'), changecategory(4)">연 예 인</button>

        </li>
      </ul>

      <div class="content">

        <div>
          <h1 class="title">{{ keyword }}</h1>
        </div>
      
        <div class="scene" v-if="category_id==1">
          <label class="card-wrap" v-for="(item, key) in sport" :key="key">
            <input type="checkbox" class="flipcard">
            <div class="card">
              <div class="front card-face">
                  <img :src="item.imgUrl" alt="" class="card-photo">
              </div>
              <div class="back card-face">
                <h1>{{item.name}}</h1>
                <p class="card__body">
                  {{item.dykClubContentResponses[0]['content']}}
                </p>
              </div>
            </div>
            <footer class="social">
              <button class="btn btn__phone" @click="openYoutubeModal(item.name)"></button>
              <button class="btn btn__email" @click="openTwitterModal(item.name)"></button>
              <button class="btn btn__intro" @click="openProfileModal(item.name)"></button>
              <button class="btn btn__award" @click="openAwardModal(item.name)"></button>
            </footer>
          </label>
        </div>
        <div class="scene" v-if="category_id==2">
          <label class="card-wrap" v-for="(item, key) in drama" :key="key">
            <input type="checkbox" class="flipcard">
            <div class="card">
              <div class="front card-face">
                  <img :src="item.imgUrl" alt="" class="card-photo">
              </div>
              <div class="back card-face">
                <h1>{{item.name}}</h1>
                <p class="card__body">
                  {{item.dykClubContentResponses[0]['content']}}
                </p>
              </div>
            </div>
            <footer class="social">
              <button class="btn btn__phone" @click="openYoutubeModal(item.name)"></button>
              <button class="btn btn__email" @click="openTwitterModal(item.name)"></button>
              <button class="btn btn__intro" @click="openProfileModal(item.name)"></button>
              <button class="btn btn__award" @click="openAwardModal(item.name)"></button>
            </footer>
          </label>
        </div>
        <div class="scene" v-if="category_id==3">
          <label class="card-wrap" v-for="(item, key) in movie" :key="key">
            <input type="checkbox" class="flipcard">
            <div class="card">
              <div class="front card-face">
                  <img :src="item.imgUrl" alt="" class="card-photo">
              </div>
              <div class="back card-face">
                <h1>{{item.name}}</h1>
                <p class="card__body">
                  {{item.dykClubContentResponses[0]['content']}}
                </p>
              </div>
              <div class="bottombox">hi</div>
            </div>
            <footer class="social">
              <button class="btn btn__phone" @click="openYoutubeModal(item.name)"></button>
              <button class="btn btn__email" @click="openTwitterModal(item.name)"></button>
              <button class="btn btn__intro" @click="openProfileModal(item.name)"></button>
              <button class="btn btn__award" @click="openAwardModal(item.name)"></button>
            </footer>
          </label>
        </div>
        <div class="scene" v-if="category_id==4">
          <label class="card-wrap" v-for="(item, key) in entertainer" :key="key">
            <input type="checkbox" class="flipcard">
            <div class="card">
              <div class="front card-face">
                  <img :src="item.imgUrl" alt="" class="card-photo">
              </div>
              <div class="back card-face">
                <h1>{{item.name}}</h1>
                <p class="card__body">
                  {{item.dykClubContentResponses[0]['content']}}
                </p>
              </div>
            </div>
            <footer class="social">
              <button class="btn btn__phone" @click="openYoutubeModal(item.name)"></button>
              <button class="btn btn__email" @click="openTwitterModal(item.name)"></button>
              <button class="btn btn__intro" @click="openProfileModal(item.name)"></button>
              <button class="btn btn__award" @click="openAwardModal(item.name)"></button>
            </footer>
          </label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import DYKCNav from '@/components/DYKC/DYKCNav.vue'
import YoutubeCardmodal from '@/components/DYKC/YoutubeCardmodal.vue'
import TwitterCardmodal from '@/components/DYKC/TwitterCardmodal.vue'
import ProfileCardmodal from '@/components/DYKC/ProfileCardmodal.vue'
import AwardCardmodal from '@/components/DYKC/AwardCardmodal.vue'
import { mapActions, mapGetters } from 'vuex'


export default {
  name: "AwardView",
  components: {
    DYKCNav,
    YoutubeCardmodal,
    TwitterCardmodal,

    ProfileCardmodal,
    AwardCardmodal,
  },
  data(){
    return{
      isShowing : true,
      youtube : false,
      twitter : false,
      profile : false,
      award : false,
      keyword : "운동선수",
      category_id : 1,
      twitterName : "",
      youtubeName : "",
      awardName : "",
      profileName : "",
      twitter_translate : false,
    }
  },
  computed: {
    ...mapGetters(['sport', 'drama', 'movie', 'entertainer'])
  },
  created() {
    this.fetchSport(1);
    this.fetchDrama(2);
    this.fetchMovie(3);
    this.fetchEntertainer(4);
  },
  methods: {
    ...mapActions(['fetchSport', 'fetchMovie', 'fetchDrama', 'fetchEntertainer']),
    

    sound() {
      this.isShowing = !this.isShowing;
    },
    changeKeyword(event) {
      this.keyword = event;
    },
    changecategory(event) {
      this.category_id = event;
      if(this.category_id == 1){
        this.cardfront = this.sport;
      }
      else if (this.category_id == 2){
        this.cardfront = this.drama;
      }
      else if (this.category_id == 3){
        this.cardfront = this.movie;
      }
      else if (this.category_id == 4){
        this.cardfront = this.entertainer;
      }
    },
    openYoutubeModal(event) {
      this.youtube = true;
      this.youtubeName = event;
    },
    openTwitterModal(event) {
      this.twitter = true;
      this.twitterName = event;
    },

    openProfileModal(event){
      this.profile = true;
      this.profileName = event
    },
    openAwardModal(event){
      this.award = true;
      this.awardName = event
    },
    youtubeClose(event){
      if(event.target.classList.contains('black-bg')||event.target.classList.contains('close2')){
        this.youtube = false;
        this.twitter_translate = false;
      } else if (event.target.classList.contains('white-bg')){
        this.youtube = true;
      }
    },
    twitterClose(event){
      if(event.target.classList.contains('black-bg')||event.target.classList.contains('close2')){
        this.twitter = false;
        this.twitter_translate = false;
      } else if (event.target.classList.contains('white-bg')){
        this.twitter = true;
      }
    },
    profileClose(event){
      if(event.target.classList.contains('black-bg')||event.target.classList.contains('close2')){
        this.profile = false;
        this.twitter_translate = false;
      } else if (event.target.classList.contains('white-bg')){
        this.profile = true;
      }
    },
    awardClose(event){
      if(event.target.classList.contains('black-bg')||event.target.classList.contains('close2')){
        this.award = false;
        this.twitter_translate = false;
      } else if (event.target.classList.contains('white-bg')){
        this.award = true;
      }
    },
  },
}  
</script>

<style scoped>
  @font-face {
    font-family: 'BMJUA';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/BMJUA.woff') format('woff');
    font-weight: normal;
    font-style: normal;
  }
  @font-face {
    font-family: 'RixYeoljeongdo_Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2102-01@1.0/RixYeoljeongdo_Regular.woff') format('woff');
    font-weight: normal;
    font-style: normal;
  }
  @font-face {
    font-family: 'KyoboHand';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@1.0/KyoboHand.woff') format('woff');
    font-weight: normal;
    font-style: normal;
  }
  @font-face {
    font-family: 'SDSamliphopangche_Outline';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts-20-12@1.0/SDSamliphopangche_Outline.woff') format('woff');
    font-weight: normal;
    font-style: normal;
  }
@font-face {
  font-family: 'PyeongChangPeace-Bold';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2206-02@1.0/PyeongChangPeace-Bold.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
}

  video {
    position: fixed; right: 0; bottom: 0;
    min-width: 100%; min-height: 100%;
    width: auto; height: auto; z-index: -100;
    background-size: cover;
  }
  .soundbtn{
    width: 3rem;
    height: auto;
    display: flex;
    margin-left: auto;
    margin-right: 5rem;
    float: right;
  }
  .soundbtn:hover{
    transform: scale(1.2);
  }
  .main{
    display: flex;
    margin-top: 3rem;
  }
  ul{
    list-style:none;
    font-weight: bold;
  }
  li > button {
    all: unset;
    display: flex;
    justify-content: center;
    width: 8rem;
    color: white;
    font-size: 2.5rem;
    font-weight: bold;
    border: 0;
    padding: 0;
    margin-bottom: 3rem;
    margin-top: 3rem;
    position: relative;
    font-family: 'BMJUA';
  }
  .category{
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
    margin-left: 2rem;
    margin-top: 3rem;
  }

  li > button:hover {
    transform: scale(1.2);
  } 
  .content{
    flex: 1;
  }
  .title{
    text-align : center;
    font-size: 3.5rem;
    font-family: 'BMJUA';
    letter-spacing: 1rem;
    color: #ffdfaed6;
    text-shadow: 0 0 3px #fff, 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #ffdfaed6,
    0 0 25px #ffdfaed6, 0 0 35px #ffdfaed6, 0 0 55px #ffdfaed6, 0 0 70px #ffdfaed6;
    margin-bottom:3rem;
  }


 * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  .input {
      position: absolute;
  }

  .scene {
      width: 80%;
      max-width: 100%;
      min-height: 80%;
      margin: auto;
      padding: 10px 30px;
  }

  .card-wrap {
      display: block;
      width: 300px;
      max-width: 100%;
      height: 400px;
      margin-right: 2rem;
      margin-bottom: 15px;
  }

  .card, .front, .back, .card-photo{
      width: 100%;
      height: 100%;
  }

  .card-face {
      position: absolute;
      backface-visibility: hidden;
  }

  .card {
    position: relative;
    transform-style: preserve-3d;
    transition: transform 1s, box-shadow .4s;
    box-shadow: 0 1px 2px 0 rgba(60,64,67,0.302), 0 1px 3px 1px rgba(60,64,67,0.149);
    border-radius: 10px;
  }
   .card-photo {
    object-fit: fill;
    border-radius: 10px;
    opacity: 1;
    transition: 0.3s;
  }
  .card-photo:hover{
    transform: scale(1.1);
  }
  .back {
      background-color: white;
      transform: rotateY( 180deg );
      text-align: center;
      color: darkgray;
      border-radius: 10px;
      font-family: 'Raleway', sans-serif;
      font-weight: 600;
  }
  .back h1 {
    margin-top: 2rem;
    font-family: 'RixYeoljeongdo_Regular';
  }
  .back p {
    margin: 0;
    width: 80%;
    position: absolute;
    top: 50%;
    left: 50%;
    font-size: 1.2rem;
    font-family: 'KyoboHand';
    transform: translate(-50%, -50%);
    text-align: left;
  }
  .flipcard {
      opacity: 0;
  }
  input:checked + .card {
      transform: rotateY( 180deg );
  }
  @media screen and (min-width: 960px) {
    .scene {
        display: flex;
        justify-content: space-around;
    }
  }
  a {
    text-decoration: none;
    color: var(--color-link);
  }
  a:hover {
    color: var(--color-link-hover);
  }

  footer.social {
    display: grid;
    justify-items: center;
    grid-column-gap: 1em;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    border-radius: 1em;
    top: 85%;
    position: absolute;
    background-color: rgb(0 0 0 / 35%);
  }
  .btn {
    position: relative;
    width: 4em;
    height: 4em;
    border-radius: 50vh;
    background: #0099ff8a;
    border: 0;
    outline: 0;
    -webkit-transition: all 0.4s ease;
    transition: all 0.4s ease;
    margin : 5px;
  }
  .social .btn::before {
    position: absolute;
    top: 50%;
    left: 50%;
    -webkit-transform: translate(-50%, -45%);
    transform: translate(-50%, -45%);
    color: white;
    font-size: 2em;
    margin-right: 0.5em;
  }
  .icon::before,
  .icon::after,
  .btn::before {
    display: inline-block;
    font-weight: 700;
    font-style: normal;
    font-variant: normal;
    text-rendering: auto;
  }

  .btn:hover {
    -webkit-box-shadow: inset 0 0 10px 0 white, 0 0 10px 0 #0099ff,
      0 0 20px 0 #0099ff, 0 0 30px 0 #0099ff;
    box-shadow: inset 0 0 10px 0 white, 0 0 10px 0 #0099ff, 0 0 20px 0 #0099ff,
      0 0 30px 0 #0099ff;
    border: 1px solid white;
    -webkit-transform: rotate(360deg) scale(1.2);
    transform: rotate(360deg) scale(1.2);
  }
  .btn:hover::before {
    font-family: Raleway, sans-serif;
    font-weight: 900;
    font-size: 1em;
    color: white;
    text-shadow: 0 0 3px #003b62;
  }

  .btn:active {
    background-color: #6dc5ff;
  }

  .btn__phone::before {
    content: url("../../assets/DYKC/youtube.png");
  }
  .btn__phone:hover::before {
    content: "YOUTUBE";
    font-family: 'PyeongChangPeace-Bold';
  }

  .btn__email::before {
    content: url("../../assets/DYKC/twitter.png");
  }
  .btn__email:hover::before {
    content: "TWITTER";
    font-family: 'PyeongChangPeace-Bold';
  }
  .btn__intro::before {
    content: url("../../assets/DYKC/profile.png");
  }
  .btn__intro:hover::before {
    content: "INTRO";
    font-family: 'PyeongChangPeace-Bold';
  }
  .btn__award::before {
    content: url("../../assets/DYKC/award.png");
  }
  .btn__award:hover::before {
    content: "AWARD";
    font-family: 'PyeongChangPeace-Bold';
  }
  .black-bg {
    width: 100%; height:100%;
    background: rgba(0,0,0,0.6);
  }
.white-bg {
  width: 100%; background: rgb(255 255 255 / 20%);
  border-radius: 8px;
  padding: 20px;
  position: relative;
  top: 50%;
  left: 50%;
  width: 70vw;
  height: 90vh;
  transform: translate(-50%, -50%);
}
.close2{
  position: absolute;
  cursor: pointer;
  border:none;
  background: #6667AB;
  color: white;
  font-weight: bold;
  border-radius: 5px;
  padding: 5px 15px;
  bottom: 2vh;
  right: 30vw;
  width: 10rem;
  height: 5vh;
  font-size: x-large;
}
.close2:hover{
  color:white;
  font-weight: bold;
  transform: scale(1.1);
  transition: all 0.5s;
}

</style>

