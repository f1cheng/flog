<template>
  <div class="row">
    <div class="col-md-4">
      <div class="form-group">
        <input type="hidden" v-model="toedit" />
      </div>

     <h3> Article List</h3>

     <div>
      <el-form>
          <el-row>
           <el-col :span="4">
          <el-form-item>
            <el-input v-model="SearchKey"></el-input>
          </el-form-item>
          </el-col>

           <el-col :span="2">
          <el-form-item>
            <el-button type="primary" icon="el-icon-search" @click="onSearch">Search</el-button>
          </el-form-item>
          </el-col>

           <el-col :span="4">
          <el-form-item>
            <el-button type="primary" icon="el-icon-edit" @click="toPost">Post</el-button>
          </el-form-item>
          </el-col>

          </el-row>
       </el-form>

     </div>
    </div>

    <div>

    <el-table
      v-loading="listLoading"
      :data="blogs"
      border
      fit
      highlight-current-row
      style="width: 100%;"
      :header-cell-style="{'background': '#e0e0e0'}"
    >

      <el-table-column label="Title" min-width="auto">
        <template v-slot="{ row }">
          <span class="link-type" @click="getArticle(row.title)">{{ row.title }}</span>
        </template>
      </el-table-column>
	  
      <el-table-column label="Description" min-width="auto">
        <template v-slot="{ row }">
          <span class="link-type">{{ row.description }}</span>
        </template>
      </el-table-column>
	  
      <el-table-column
        label="Operation"
        align="center"
        width="auto"
        class-name="small-padding fixed-width"
      >
        <template v-slot="scope">
          <el-button type="primary" size="mini" @click="editBlogRow(scope.row.title)">Edit</el-button>
          <el-button
            size="mini"
            type="danger"
            @click.native.prevent="deleteBlogRow(scope.$index, blogs, scope.row.title)"
            >Delete</el-button
          >
        </template>
      </el-table-column>


    </el-table>
    </div>
  </div>
 </div>
</template>

<script>
import {mavonEditor} from "mavon-editor";
import {marked} from "marked";
import 'mavon-editor/dist/css/index.css';
import Qs from "qs";
export default {
  name: 'Articles',
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
      SearchKey: '',
    }
  },
  methods: {

    rowStyle({row, rowIndex}) {
      if (rowIndex === 0) {
        return {'background': '#e0e0e0'};
      }
      else {
        return {};
      }
    },

    toPost() {
      this.$router.push({name: 'Post', params:{title: ''}})
    },
    getArticle(title) {
      this.$router.push({name:'Article', query:{title: title}})
    },
    getAll () {
      this.$axios({
        url: 'rest/article/',
        method: 'get',
        params: {}
      }).then(res => {
        this.blogs = res.data.data
        for (var x in this.blogs)
        {
            this.blogs[x].hh = marked(this.blogs[x].content)
        }
        this.title = ''
        this.description = ''
        this.content = ''
        this.toedit = ''
      })
        .catch(error => {
          console.log(error)
        })
    },
    onSearch () {
      this.$axios({
        url: 'rest/article/',
        method: 'GET',
        params: {title: this.SearchKey, }, 
      }).then(res => {
        this.$message({
            type: 'success',
            message: 'Success!'
          })

        this.blogs = res.data.data
        for (var x in this.blogs)
        {
            this.blogs[x].hh = marked(this.blogs[x].content)
        }
        this.title = ''
        this.description = ''
        this.content = ''
        this.toedit = ''
      }).catch(error => {
          console.log(error)
        })
    },

    editBlogRow (title) {
      this.toedit = 'edit_mode'
      this.title = title
      this.$router.push({name:'Post', params:{title: this.title}})
    },
 

    editBlog (blog) {
      this.toedit = 'edit_mode'
      this.title = blog.title
      this.description = blog.description
      this.content = blog.content
      this.$router.push({name:'Post', params:{title: this.title}})
    },


    deleteBlogRow (index, rows, title) {
      this.$confirm('Article to be deleted, to continue?', 'Prompt', {
        confirmButtonText: 'Confirm',
        cancelButtonText: 'Cancel',
        type: 'warning'
      }).then(() => {
        this.deleteArticle(title).then(response => {
          this.$message({
            type: 'success',
            message: 'Deleted successful!'
          })
        })
        rows.splice(index, 1)
      })
    },

    deleteArticle (title) {
      return this.$axios({
        url: 'rest/article/',
        method: 'delete',
        data: {
          title: title,
        }
      })
    },

    deleteBlog (blog) {
      this.$axios({
        url: 'rest/article/',
        method: 'delete',
        data: {
          title: blog.title,
          content: blog.content
        }}).then(() => {
        this.getAll()
      })
    },

  },
  mounted () {
  },
  created () {
    this.getAll()
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .article-title {
        font-size: large;
        font-weight: bolder;
        color: black;
        text-decoration: none;
        padding: 5px 0 5px 0;
    }
</style>
