<template>
  <el-container>
    <el-aside width="200px" class="hidden-sm-and-down aside">
      <sidebar></sidebar>
    </el-aside>
    <el-main class="main">
      <welcome-page title="Benchmark: Graph vs Relational DB"/>
    </el-main>
  </el-container>
</template>

<script>
import WelcomePage from "./WelcomePage";
import Sidebar from "./Sidebar";

export default {
  name: "app",
  components: {
    WelcomePage,
    Sidebar
  }
};
</script>

<style>
</style>
