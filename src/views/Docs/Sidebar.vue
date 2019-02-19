<template>
  <el-menu :default-active="activeIndex" :router="true">
    <el-submenu index="1">
      <template slot="title">
        <i class="el-icon-location"></i>
        <span>Guide</span>
      </template>
      <el-menu-item index="/docs/intro">Introduction</el-menu-item>
      <el-menu-item index="/docs/quick-start">Quick Start</el-menu-item>
    </el-submenu>
    <el-menu-item index="/docs/components">
      <i class="el-icon-menu"></i>
      <span>Components</span>
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  computed: {
    activeIndex() {
      return this.$route.path;
    }
  }
};
</script>