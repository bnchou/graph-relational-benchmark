<template>
  <div>
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
    {{query}}
  </div>
</template>

<script>
import InfoPane from "@/components/Panes/InfoPane";
import LineChart from "@/components/Charts/LineChart";
import PieChart from "@/components/Charts/PieChart";

export default {
  props: {
    data: String,
    query: Object,
    isLoading: Boolean
  },
  components: { InfoPane, LineChart, PieChart }
};
</script>

<style>
</style>
