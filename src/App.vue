<template>
  <div id="app">
    <el-container>
      <el-header class="header">
        <navbar></navbar>
      </el-header>
      <docs></docs>
    </el-container>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import Docs from "@/views/Docs";

export default {
  name: "app",
  components: {
    Navbar,
    Docs
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  color: #2c3e50;
}
</style>
