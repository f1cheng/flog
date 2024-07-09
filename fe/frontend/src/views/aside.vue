<template>

<el-menu router=true background-color="#D3DCE6" mode="horizontal" class="menuAlign">
        <el-menu-item-group>
          <template slot="title">
            <i class="el-icon-menu"></i>
            <span style="font-size:15px">House</span>
          </template>
          <el-menu-item index="/decoration">
          <span style="margin-left:10px">House Decoration</span>
          </el-menu-item>
        </el-menu-item-group>

        <el-menu-item-group>
          <template slot="title">
          <i class="el-icon-menu"></i>
            <span style="font-size:15px">Blogs</span>
          </template>
          <el-menu-item index="/post">
          <span style="margin-left:10px">Post</span>
          </el-menu-item>
          <el-menu-item index="/articles">
          <span style="margin-left:10px">Blog Posts</span>
          </el-menu-item>
        </el-menu-item-group>
</el-menu>

</template>

<script>
export default {
  name: 'Aside',

  data() {
    return {
    }
  },

  methods: {

  handleOpen(key, keyPath) 
  {
    this.$refs.menus.open(keyPath);
  },
  handleClose(key, keyPath) 
  {
    this.$refs.menus.open(keyPath);
  },


  }
} 

</script>

<style>

  .menuAlign{
    text-align:left;
    margin: 0;
    color: #303133;
  }

</style>
