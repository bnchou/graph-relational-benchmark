<template>
  <div id="menu">
    <el-menu :default-active="activeIndex" mode="horizontal" :router="true">
      <el-menu-item index="/benchmark">
        <logo></logo>
      </el-menu-item>
      <el-menu-item class="item" index="@github" :route="{}">
        <a href="https://github.com/VictorWinberg/graph-relational-benchmark" target="_blank">Github</a>
      </el-menu-item>
      <el-menu-item class="item" index="/docs">Docs</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
import Logo from "./Logo";

export default {
  components: {
    Logo
  },
  computed: {
    activeIndex() {
      return this.$route.path;
    }
  }
};
</script>

<style scoped>
.item {
  float: right;
}
a {
  text-decoration: none;
}
</style>
