<template>
  <ve-gauge :data="chartData" :settings="chartSettings"></ve-gauge>
</template>

<script>
import VeGauge from "v-charts/lib/gauge.common";

export default {
  components: { VeGauge },
  data() {
    this.chartSettings = {
      labelMap: {
        speed: "speed"
      },
      dataName: {
        speed: "km/h"
      }
    };
    return {
      chartData: {
        columns: ["type", "value"],
        rows: [{ type: "speed", value: 60 }]
      }
    };
  }
};
</script>