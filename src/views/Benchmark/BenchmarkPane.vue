<template>
  <div>
    <h1>{{title}}</h1>
    <el-row :gutter="20">
      <el-col :sm="8">
        <h2>Table</h2>
      </el-col>
      <el-col :sm="8">
        <h2>Graph</h2>
        <line-graph :data="data"/>
      </el-col>
      <el-col :sm="8">
        <h2>Pie</h2>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import LineGraph from "./LineGraph";

export default {
  props: {
    title: String,
    data: String
  },
  components: { LineGraph }
};
</script>

<style>
</style>
