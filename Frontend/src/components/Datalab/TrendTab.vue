<template>
  <div>
    <!-- <div class="trend-container">여기는 연관검색어</div>
    <div class="news-container">여기는 뉴스링크</div> -->
    <RelatedKeyword></RelatedKeyword>
    <NewsArticle></NewsArticle>
  </div>
</template>

<script>
import NewsArticle from './NewsArticle.vue';
import RelatedKeyword from './RelatedKeyword.vue';
export default { components: { NewsArticle, RelatedKeyword } };
</script>

<style scoped>
/* .trend-container {
  height: 15rem;
  width: 20rem;
  background: white;
  margin-left: 1rem;
  margin-right: 1.5rem;
  border-radius: 15px;
}
.news-container {
  width: 20rem;
  height: 16rem;
  background: white;
  margin-left: 1rem;
  margin-top: 1rem;
  margin-right: 1.5rem;
  border-radius: 15px;
} */
</style>
