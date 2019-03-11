<template>
  <el-tabs type="border-card" @tab-click="handleClick" :stretch="true" style="min-height: 80vh;">
    <el-tab-pane name="advanced_coworkers" v-loading="isLoading">
      <span slot="label">
        <v-icon name="building"/>
        <!-- Companies -->
        Coworkers
      </span>
      <benchmark-pane title="Coworkers" data="advanced_coworkers" :isLoading="isLoading"/>
    </el-tab-pane>
    <el-tab-pane name="advanced_histories" v-loading="isLoading">
      <span slot="label">
        <v-icon name="history"/>
        <!-- Histories -->
        Histories
      </span>
      <benchmark-pane title="Histories" data="advanced_histories" :isLoading="isLoading"/>
    </el-tab-pane>
  </el-tabs>
</template>

<script>
import BenchmarkPane from "@/components/Panes/BenchmarkPane";

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
