<template>
  <ve-line :data="chartData"></ve-line>
</template>

<script>
import _ from "lodash";
import VeLine from "v-charts/lib/line.common";

export default {
  props: {
    data: { type: String, required: true }
  },
  components: { VeLine },
  computed: {
    chartData() {
      const ungrouped = json => {
        const [columns, values] = _.unzip(_.toPairs(json));
        const rows = _.map(_.zip(...values), (a, i) =>
          _.merge(_.zipObject(columns, a), { i })
        );
        columns.unshift("i");

        return { columns, rows };
      };

      const chartData = this.$store.state.executionData[this.data];

      if (chartData) return ungrouped(chartData);
      return null;
    }
  }
};
</script>