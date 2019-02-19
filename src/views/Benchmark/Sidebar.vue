<template>
  <el-menu :default-active="activeIndex" :router="true">
    <el-menu-item index="/benchmark">
      <i class="el-icon-view"></i>
      <span>Analysis</span>
    </el-menu-item>
    <el-menu-item index="/benchmark/settings">
      <i class="el-icon-setting"></i>
      <span>Configuration</span>
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