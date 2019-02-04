<template>
  <div id="app">
    <el-container>
      <el-header class="header">
        <navbar></navbar>
      </el-header>
      <el-container>
        <el-aside width="200px" class="hidden-sm-and-down aside">
          <sidebar></sidebar>
        </el-aside>
        <el-main class="main">
          <HelloWorld title="Benchmark: Graph vs Relational DB"/>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import HelloWorld from "@/components/HelloWorld.vue";
import Sidebar from "@/components/Sidebar.vue";

export default {
  name: "app",
  components: {
    Navbar,
    HelloWorld,
    Sidebar
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  color: #2c3e50;
}
</style>
