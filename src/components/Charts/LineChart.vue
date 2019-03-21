<template>
  <ve-line :data="chartData" :settings="chartSettings"></ve-line>
</template>

<script>
import _ from "lodash";
import VeLine from "v-charts/lib/line.common";

export default {
  props: {
    data: { type: String, required: true }
  },
  components: { VeLine },
  data() {
    return {
      chartSettings: {
        yAxisName: ["time [ms]"]
      }
    };
  },
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
      return { columns: ["x", "no data"], rows: [{ x: 0, "no data": 0 }] };
    }
  }
};
</script>