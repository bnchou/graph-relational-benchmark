<template>
  <div id="app">
    <el-container>
      <el-header class="header">
        <navbar></navbar>
      </el-header>
      <router-view></router-view>
    </el-container>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";

export default {
  name: "app",
  components: {
    Navbar
  }
};
</script>

<style>
#app {
  font-family: "GalanoGrotesque", "Avenir", Helvetica, Arial, sans-serif;
  color: #2c3e50;
}

.fa-icon {
  position: relative;
  top: 3px;
  width: 16px;
  height: 16px;
}
</style>
