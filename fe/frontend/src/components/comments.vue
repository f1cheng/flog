<template>
  <div>

  <br /><br />
  <hr />
  <h3>Your comments is welcome!</h3>
  <textarea
    v-model="comment.message"
    :placeholder="placeholder"
    name="commentname"
    id="comment-area"
    cols="60"
    rows="10"></textarea>
  <div>
    <el-button @click="submitComment" class="submitBtn">Submit</el-button>
  </div>

    <hr>
    <div v-for="commentt in comments" :key="commentt.id">
     <div class='ccomments'>
            <span class='cheader'>
               comment: 
            </span>
             <div class='ccontent'>
                {{ commentt.message }}
             </div>
     </div>
     </div>
     <hr>


  </div>
</template>

<script>
export default {
  name: "Comments",
  props: ['articleId'], 
  watch: {
    articleId(newvalue, oldvalue) {
      console.log('show comments once article id changed')
      this.getArticleComments(newvalue)
    }
  },
  data(){
    return {
      comments: [],
      message: 'msg',
      comment: {},
      articleId: null,
    }
  },

  create() {
  },

  mounted() {
    //'this prefix is must'
    this.getArticleComments(this.articleId)
  },

  methods:{
    submitComment() {
      if (this.articleId == null) {
        this.$message({
            type: 'error',
            message: 'articleId is empty!'
          })
        return
      }

      this.comment.article_id = this.articleId
      let comm = {article_id: this.articleId, message:this.comment.message}
      this.comments.unshift(comm)
      this.$axios({
        url: 'rest/comment/',
        method: 'post',
        data: {
          article_id: this.articleId,
          message: this.comment.message,
        }
      }).then(res => {
        let article_comments = res.data.data
        let mss = article_comments[0].message
        let idd = article_comments[0].article_id
      })

    },

    getArticleComments(aid) {
      if (this.articleId == null) {
        return
      }
      alert(aid)
      this.$axios({
        url: 'rest/comment/',
        method: 'get',
        params: {
          article_id: aid,
        }
      }).then(res => {
        this.comments = res.data.data
      })
    },

  }
}
</script>

<style scoped>

.comment-area {
  padding: 30px 10px;
}

.ccontent {
   font-size: large;
   padding: 10px;
 }

.ccomments {
  padding-top: 10px;
  line-height: 90%;
 }

.cheader {
  font-weight: bold;
  color: darkorange;
}

</style>
