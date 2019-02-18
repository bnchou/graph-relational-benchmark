<template>
  <el-container>
    <el-aside width="200px" class="hidden-sm-and-down aside">
      <sidebar></sidebar>
    </el-aside>
    <el-main class="main">
      <router-view/>
    </el-main>
  </el-container>
</template>

<script>
import Sidebar from "./Sidebar";

export default {
  name: "benchmark",
  components: {
    Sidebar
  }
};
</script>

<style>
</style>
