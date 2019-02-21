<template>
  <div>
    <h4>Cypher</h4>
    <el-tag class="tag">Mean: {{chartData.cypher.mean}} ms</el-tag>
    <el-tag class="tag">Std: {{chartData.cypher.std}} ms</el-tag>

    <h4>SQL</h4>
    <el-tag class="tag">Mean: {{chartData.sql.mean}} ms</el-tag>
    <el-tag class="tag">Std: {{chartData.sql.std}} ms</el-tag>
  </div>
</template>

<script>
import _ from "lodash";

export default {
  props: {
    data: { type: String, required: true }
  },
  computed: {
    chartData() {
      const calc = values => {
        const mean = _.mean(values);
        const pow2 = x => Math.pow(x - mean, 2);
        const std = Math.sqrt(_.sum(_.map(values, pow2)) / values.length);

        return { mean: _.round(mean, 2), std: _.round(std, 2) };
      };

      const chartData = this.$store.state.executionData[this.data];

      if (chartData) return _.mapValues(chartData, calc);
      return { cypher: {}, sql: {} };
    }
  }
};
</script>

<style scoped>
.tag {
  margin-right: 10px;
}
</style>
