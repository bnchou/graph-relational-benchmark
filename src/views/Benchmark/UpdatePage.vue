<template>
  <el-tabs type="border-card" @tab-click="handleClick" :stretch="true" style="min-height: 80vh;">
    <el-tab-pane name="deals" v-loading="isLoading">
      <span slot="label">
        <v-icon name="handshake"/>
        <!-- Deals -->
        Deals
      </span>
      <benchmark-pane title="Deals" data="update_deals" :isLoading="isLoading"/>
    </el-tab-pane>
  </el-tabs>
</template>

<script>
import BenchmarkPane from "./BenchmarkPane";

export default {
  components: { BenchmarkPane },
  data() {
    return {
      isLoading: false
    };
  },
  methods: {
    handleClick: async function(tab) {
      this.isLoading = true;

      const res = await fetch(`/api/command/${tab.name}`);
      const json = await res.json();

      this.$set(this.$store.state.executionData, tab.name, json);

      this.isLoading = false;
    }
  }
};
</script>

<style scoped>
</style>
