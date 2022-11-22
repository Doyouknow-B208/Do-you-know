<template>
  <div class="APIscene" style="overflow:auto;">
    <div class="twitter_box" v-for="(item, index) in twitter" :key="index">
      <TwitterTranslate :twitter="item" :index="index" :name="name"/>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  
  import TwitterTranslate from '@/components/DYKC/TwitterTranslate.vue'

  export default {
    props: ["name", "status"],
    components:{
      TwitterTranslate,
    },
    computed: {
      ...mapGetters(['twitter'])
    },
    methods: {
      ...mapActions(['fetchTwitter']),

    },
    created() {
      this.fetchTwitter(this.name);
    },
  }
</script>

<style scoped>
  .APIscene{
    position: fixed;
    top: 2.5rem;
    border-radius: 8px;
    background-color: #cac9cd;
    width: 90%;
    height: 80%;
    transform: translate(5%, 5%);
  } 
  .APIscene::-webkit-scrollbar {
    width: 10px;
  }
  .APIscene::-webkit-scrollbar-track {
    background-color: transparent;
  }
  .APIscene::-webkit-scrollbar-thumb {
    border-radius: 20px;
    background-color: rgb(219, 214, 214);
  }
  .APIscene::-webkit-scrollbar-button {
    width: 0;
    height: 0;
  }
  .twitter_box{
    display: flex;
    height: auto;
    width: 100%;
    justify-content: space-around;
    align-items: center;
    margin-top: 1rem;
    margin-bottom: 2rem;
  }
</style>