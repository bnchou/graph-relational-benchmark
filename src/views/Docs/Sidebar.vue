<template>
  <el-menu :default-active="activeIndex" :router="true">
    <el-submenu index="1">
      <template slot="title">
        <i class="el-icon-location"></i>
        <span>Guide</span>
      </template>
      <el-menu-item index="/docs/intro">Introduction</el-menu-item>
    </el-submenu>
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