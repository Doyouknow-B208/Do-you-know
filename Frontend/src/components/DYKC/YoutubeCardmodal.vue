<template>
  <div class="APIscene">
    <iframe
      width="100%"
      height="100%"
      :src="`https://www.youtube.com/embed/${urlword}`"
      >
    </iframe>  
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: ["name"],
  data(){
    return{
      keyword: '',
      youtube: [],
      selectedYoutube: null,
      urlword:'',
    }
  },
  mounted(){
    this.setKeyword();
  },
  methods:{
    setKeyword(){
      const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
      
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      this.keyword = this.name + '해외 반응'

      const config = {
        params:{
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          chart : 'mostPopular',
          maxResults : 2,
          q: this.keyword,
        }
      }
      axios.get(API_URL, config)
        .then(response => {
          this.youtube = response.data.items
          this.selectedYoutube = this.youtube[1]      
          this.urlword = this.selectedYoutube.id.videoId
           
        })
    },  
  },
}

</script>

<style scoped>
  .APIscene{
    position: fixed;
    top: 2.5rem;
    background-color: gray;
    width: 85%;
    height: 80%;
    transform: translate(7%, 5%);
  }
</style>