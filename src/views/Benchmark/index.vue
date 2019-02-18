<template>
  <el-container>
    <el-aside width="200px" class="hidden-sm-and-down aside">
      <sidebar></sidebar>
    </el-aside>
    <el-main class="main">
      <benchmark-page/>
    </el-main>
  </el-container>
</template>

<script>
import BenchmarkPage from "./BenchmarkPage";
import Sidebar from "./Sidebar";

export default {
  name: "app",
  components: {
    BenchmarkPage,
    Sidebar
  }
};
</script>

<style>
</style>
