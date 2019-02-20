<template>
  <div>
    <h1>{{title}}</h1>
    <el-row :gutter="20">
      <el-col :sm="8">
        <h2>Table</h2>
      </el-col>
      <el-col :sm="8">
        <h2>Graph</h2>
        <line-chart :data="data"/>
      </el-col>
      <el-col :sm="8">
        <h2>Pie</h2>
        <pie-chart :data="data"/>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import LineChart from "./LineChart";
import PieChart from "./PieChart";

export default {
  props: {
    title: String,
    data: String
  },
  components: { LineChart, PieChart }
};
</script>

<style>
</style>
