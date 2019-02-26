<template>
  <ve-pie :data="chartData"></ve-pie>
</template>

<script>
import VePie from "v-charts/lib/pie.common";

export default {
  components: { VePie },
  data() {
    return {
      chartData: this.$store.state.data["pie-example"]
    };
  }
};
</script>