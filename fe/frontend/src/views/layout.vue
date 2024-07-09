<template>
  <el-container>
    <!-- el-container inside, if there is el-header, then it up down layout. or it will be left right layout -->
    <el-header>
      <Header />
    </el-header>
    <el-container style="height: 500px: boarder: 1px solid #eee">
      <el-aside width="200px">
        <Aside />
.     </el-aside>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import Aside from '@/views/aside'
import Header from '@/views/header'
export default {
  name: 'Layout',
  components: {
    Header,
    Aside
  },
}
</script>

<style>
.el-header {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
  padding: 0;
  z-index: 1000;
}

.el-aside, el-main {
  padding-top: 60px;
}
.el-aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  line-height: 200px;
}
.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: left;
  padding-top: 60px;
  line-height: 50px;
}
.el-container {
  position: absolute;
  width: 100%;
  top: 0px;
  left: 0;
  bottom: 0;
}
</style>
