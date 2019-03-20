<template>
  <el-menu :default-active="activeIndex" :router="true">
    <el-menu-item index="/benchmark/retrieval">
      <el-tag class="tag">GET</el-tag>
      <span>Retrieval</span>
    </el-menu-item>
    <el-menu-item index="/benchmark/insertion">
      <el-tag class="tag" type="success">POST</el-tag>
      <span>Insertion</span>
    </el-menu-item>
    <el-menu-item index="/benchmark/updating">
      <el-tag class="tag" type="warning">PUT</el-tag>
      <span>Updating</span>
    </el-menu-item>
    <el-menu-item index="/benchmark/settings">
      <el-tag class="tag" color="white">
        <i class="el-icon-setting"></i>
      </el-tag>
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

<style scoped>
.tag {
  width: 60px;
  text-align: center;
  margin-right: 10px;
}
</style>
