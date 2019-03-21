<template>
  <div>
    <el-row :gutter="20">
      <el-col :sm="8">
        <h2>Information</h2>
        <info-pane :data="data"/>
      </el-col>
      <el-col :sm="8">
        <h2>Graph</h2>
        <line-chart v-if="!reset" :data="data"/>
      </el-col>
      <el-col :sm="8">
        <h2>Pie</h2>
        <pie-chart v-if="!reset" :data="data"/>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :sm="12">
        <h3>Cypher Query</h3>
        <pre v-highlightjs="$_.trim(query.cypher).replace(/  /g, '')"><code class="prolog"></code></pre>
      </el-col>
      <el-col :sm="12">
        <h3>SQL Query</h3>
        <pre v-highlightjs="$_.trim(query.sql).replace(/  /g, '')"><code class="prolog"></code></pre>
      </el-col>
    </el-row>
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
    reset: Boolean
  },
  components: { InfoPane, LineChart, PieChart }
};
</script>

<style>
</style>
