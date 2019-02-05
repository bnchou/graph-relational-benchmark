<template>
  <div id="menu">
    <el-menu mode="horizontal">
      <el-menu-item index="/">
        <logo></logo>
      </el-menu-item>
      <el-menu-item class="item" index="/github">Github</el-menu-item>
      <el-menu-item class="item" index="/docs">Docs</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
import Logo from "@/components/Logo";

export default {
  components: {
    Logo
  }
};
</script>

<style scoped>
.item {
  float: right;
}
</style>
