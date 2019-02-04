<template>
  <div id="menu">
    <el-menu mode="horizontal">
      <el-menu-item>
        <logo></logo>
      </el-menu-item>
      <el-menu-item index="/hello">Hello</el-menu-item>
      <el-menu-item index="/projects">Projects</el-menu-item>
      <el-menu-item index="/about">About</el-menu-item>
      <el-menu-item index="/contact">Contact</el-menu-item>
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