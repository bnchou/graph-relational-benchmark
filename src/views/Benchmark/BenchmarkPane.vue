<template>
  <div>
    <h1>{{title}}</h1>
    <el-row :gutter="20">
      <el-col :sm="8">
        <h2>Information</h2>
        <info-pane :data="data"/>
      </el-col>
      <el-col :sm="8">
        <h2>Graph</h2>
        <line-chart v-if="!isLoading" :data="data"/>
      </el-col>
      <el-col :sm="8">
        <h2>Pie</h2>
        <pie-chart v-if="!isLoading" :data="data"/>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import InfoPane from "./InfoPane";
import LineChart from "./LineChart";
import PieChart from "./PieChart";

export default {
  props: {
    title: String,
    data: String,
    isLoading: Boolean
  },
  components: { InfoPane, LineChart, PieChart }
};
</script>

<style>
</style>
