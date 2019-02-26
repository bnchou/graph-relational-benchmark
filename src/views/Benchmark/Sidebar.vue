<template>
  <el-menu :default-active="activeIndex" :router="true">
    <el-menu-item index="/benchmark/retrieval">
      <i class="el-icon-view"></i>
      <span>Data retrieval</span>
    </el-menu-item>
    <el-menu-item index="/benchmark/insertion">
      <i class="el-icon-view"></i>
      <span>Data insertion</span>
    </el-menu-item>
    <el-menu-item index="/benchmark/update">
      <i class="el-icon-view"></i>
      <span>Data update</span>
    </el-menu-item>
    <el-menu-item index="/benchmark/complexity">
      <i class="el-icon-view"></i>
      <span>Query complexity</span>
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