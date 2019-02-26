<template>
  <ve-pie :data="chartData"></ve-pie>
</template>

<script>
import _ from "lodash";
import VePie from "v-charts/lib/pie.common";

export default {
  props: {
    data: { type: String, required: true }
  },
  components: { VePie },
  computed: {
    chartData() {
      const chartData = this.$store.state.executionData[this.data];
      const result = _.mapValues(chartData, _.mean);
      const rows = _.map(result, (mean, key) => ({ name: key, mean }));

      if (chartData) return { columns: ["name", "mean"], rows };
      return null;
    }
  }
};
</script>