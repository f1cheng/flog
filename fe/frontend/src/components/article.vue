<template>
  <div id="article">

    <div> 
      <el-button class="btn btn-block btn-success" @click="toArticles">
        Back To Article List
      </el-button>
    </div>

      <div class="article-wrap">
      <div class="article-message">
        <p class="article-title">
          {{ title }}
        </p>
      </div>
        
        <div class="article-info">
          Description: {{description}}
        </div>

    <div class="article-view">
     <!--<div v-highlight v-viewer class="md-body" v-html="article_html"></div>-->
     <div v-highlight v-html="article_html"></div>
    </div>
  </div>
  <div>
  <Comments  :articleId="articleid"/>
  </div> 
  </div>

</template>

<script>
// import axios from "axios";
//ok import {marked} from 'marked';
//nok import marked from 'marked';
import {marked} from 'marked';
import 'mavon-editor/dist/css/index.css'
import Comments from '@/components/comments'
//import Commentss from '@/components/commentss'
export default {
  name: "Article",
  components: {
    Comments,
  },
  data(){
    return {
      title: this.$route.query.title, 
      article_html:'xxx', 
      description:'',
      articleid: null,
    }
  },
  created() {
    //no call here
  },
  mounted() {
    this.getArticleDetail()
  },

  methods:{
    toArticles() {
      this.$router.push({name:'Articles'})
    },
    getArticleDetail() {
      this.$axios({
        url: 'rest/article/',
        method: 'get',
        params: {
          title: this.$route.query.title
        }
      }).then(res => {
        let articles = res.data.data
        this.title = articles[0].title
        this.description = articles[0].description
        this.article_html = marked(articles[0].content) 
        this.articleid = articles[0].id
      })
    },

  }
}
</script>

<style scoped>

.article {
  padding: 30px 10px;
}
.article-wrap {
  position: relative;
  padding: 30px;
  width: 90%;
  background-color: #fff;
  box-shadow: 0 0 5px 0 rgba(38, 42, 48, 0.1);
}
.article-message {
  display: flex;
  -ms-flex-direction: column;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.article-title {
  font-size: 26px;
  font-weight: 700;
  color: #E6A23C;
  margin: 0;
}

.article-info {
  font-size: 14px;
  #margin: 2px 0;
  color: #666;
  display: flex;
  flex-direction: row;
  justify-content: left;
  flex-wrap: wrap;
}

.article-view {
  position: relative;
  width: 100%;
  margin-top: 0px;
  text-align: left;
}

</style>
