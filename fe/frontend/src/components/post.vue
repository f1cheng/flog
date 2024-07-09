<template>
  <div class="row">
    <h3>Blog</h3>
     <div>
        <el-form label-width="100px">

          <el-form-item>
            <el-button type="primary" @click="saveBlog">Summit</el-button>
            <el-button type="primary" @click="toArticles">Return to Article List</el-button>
          </el-form-item>

          <el-form-item label="Title">
            <el-input v-model="title"></el-input>
          </el-form-item>

          <el-form-item label="Description">
          <el-input
            type="textarea"
            class="form-control"
            v-model="description"
            :rows="2"
            placeholder="description">
          </el-input>
          </el-form-item>

          <el-form-item label="Text">
            <mavon-editor ref="md" v-model="content" @imgAdd="$imgAdd"> </mavon-editor>
          </el-form-item>          

        </el-form>
     </div>
  </div>
</template>

<script>
import {mavonEditor} from "mavon-editor";
import marked from "marked";
import 'mavon-editor/dist/css/index.css';
import Qs from "qs";
export default {
  name: 'Post',
  props: {},
  components: {mavonEditor},
  data () {
    return {
      blogs: null,
      toedit: '',
      title: '',
      description: '',
      content: 'md content',
      article_value: 'I am fei',
      dooc: '',
      ruleForm: {
        id: '',
        title: '',
        description: '',
        content: ''
      },

    }
  },
  created() {
    this.getArticleEdit()
  },
  methods: {
    toArticles() {
      this.$router.push({name:'Articles'})
    },
    getArticleEdit() {
      let t = this.$route.params.title
      if (!t) {
        this.toedit = ''
        return
      }
      this.toedit = 'edit_mode'
      this.$axios({
        url: 'rest/article/',
        method: 'get',
        params: {
          title: this.$route.params.title
        }
      }).then(res => {
        let articles = res.data.data
        this.title = articles[0].title
        this.description = articles[0].description
        //this.article_html = marked(articles[0].content)
        this.content = articles[0].content
      })
    },
    $imgAdd(pos, file) {
        this.$axios({
          url: 'rest/article/',
          method: 'post',
          data: {
            //img: JSON.stringify({url: file['miniurl'], name: file['name'] })
            //img: {'url': file['miniurl'], 'name': file['name'] }
            img: {url: file['miniurl'], name: file['name'] }
          }
          }).then((res) => {
            this.$refs.md.$img2Url(pos, res.data.data)
          })
    },
    saveBlog () {
      if (!this.title) {
        this.$message({
            type: 'success',
            message: 'Please input title!'
        })
        return
      }

      if (this.toedit === '') {
        this.$axios({
          url: 'rest/article/',
          method: 'post',
          data:{
            'title': this.title,
            'description': this.description,
            'content': this.content
          }
          })
          .then(() => {
            this.$message({
            type: 'success',
            message: 'Success!'
            })
            //this.getAll()
          })
      } else {
        this.$axios({
          url: 'rest/article/',
          method: 'put',
          data: {
            title: this.title,
            description: this.description,
            content: this.content,
          }})
          .then(() => {
            this.$message({
            type: 'success',
            message: 'Success!'
            })
            //this.getAll()
          })
      }
      this.toArticles()
    },
    deleteBlog (blog) {
      this.$axios({
        url: 'rest/article/',
        method: 'delete',
        data: {
          title: blog.title,
          content: blog.content
        }}).then(() => {
        //this.getAll()
      })
    }
  },
  mounted () {
    //this.getAll()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
