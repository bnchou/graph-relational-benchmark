<template>
  <div id="menu">
    <div id="logo">
      <logo></logo>
    </div>
    <el-menu id="tabs" :default-active="activeIndex" mode="horizontal" :router="true">
      <el-menu-item index="/benchmark">Benchmark</el-menu-item>
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
      return this.$route.path.match("/[^/]*").toString();
    }
  }
};
</script>

<style scoped>
#menu {
  display: flex;
  align-items: flex-end;
}
#logo {
  margin: 0 3px;
}
#tabs {
  flex: 1;
}
#tabs .item {
  float: right;
}
a {
  text-decoration: none;
}
</style>
