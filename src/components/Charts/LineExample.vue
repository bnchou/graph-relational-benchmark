<template>
  <ve-line :data="chartData"></ve-line>
</template>

<script>
import VeLine from "v-charts/lib/line.common";

export default {
  components: { VeLine },
  data() {
    return {
      chartData: this.$store.state.data["line-example"]
    };
  }
};
</script>