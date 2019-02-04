<template>
  <el-menu>
    <el-menu-item-group title="Welcome">
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>Guide</span>
        </template>
        <el-menu-item index="1-1">Introduction</el-menu-item>
        <el-menu-item index="1-2">Quick Start</el-menu-item>
      </el-submenu>
      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span>Components</span>
      </el-menu-item>
    </el-menu-item-group>
  </el-menu>
</template>