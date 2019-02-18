<template>
  <el-menu :default-active="activeIndex" :router="true">
    <el-submenu index="1">
      <template slot="title">
        <i class="el-icon-location"></i>
        <span>Guide</span>
      </template>
      <el-menu-item index="#intro">Introduction</el-menu-item>
      <el-menu-item index="#start">Quick Start</el-menu-item>
    </el-submenu>
    <el-menu-item index="#components">
      <i class="el-icon-menu"></i>
      <span>Components</span>
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: this.$route.path
    };
  }
};
</script>