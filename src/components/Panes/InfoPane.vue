<template>
  <div>
    <h4>Cypher</h4>
    <el-tag type="info" class="tag">Mean: {{chartData.cypher.mean}} ms</el-tag>
    <el-tag type="info" class="tag">Std: {{chartData.cypher.std}} ms</el-tag>
    <el-tag type="info" class="tag">Worst: {{chartData.cypher.worst}} ms</el-tag>

    <h4>SQL</h4>
    <el-tag type="info" class="tag">Mean: {{chartData.sql.mean}} ms</el-tag>
    <el-tag type="info" class="tag">Std: {{chartData.sql.std}} ms</el-tag>
    <el-tag type="info" class="tag">Worst: {{chartData.sql.worst}} ms</el-tag>

    <h5>Note:</h5>
    <p>Worst-case is with 99.7% confidence level.</p>
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
        const worst = mean + 3 * std;

        const data = { mean, std, worst };
        return _.mapValues(data, i => _.round(i, 2));
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
