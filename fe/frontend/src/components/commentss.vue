<template>
  <div>

  <br />testing22222<br />
  <hr />
  <h3>Provide 2comments</h3>
  <div>
  </div>


  </div>
</template>

<script>
export default {
  name: "Commentss",
  data(){
    return {
      todo: 0,
    }
  },

  create() {
    //no here this.getArticleComments()
    this.getArticleComments2()
  },

  mounted() {
    //'this prefix is must'
    this.getArticleComments2()
  },

  methods:{
    getArticleComments2() {
      alert('22222')
      this.$axios({
        url: 'rest/comment/',
        method: 'get',
        params: {
          article_id: this.todo,
        }
      }).then(res => {
        alert('get responsed comments')
        //this.comments = article_comments
        alert('two sssssssssssssssssssss')
      })
    },

  }
}
</script>

<style scoped>

.comment-area {
  padding: 30px 10px;
}

</style>
