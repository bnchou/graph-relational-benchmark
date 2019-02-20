<template>
  <div>
    <el-tabs type="border-card" @tab-click="handleClick" :stretch="true">
      <el-tab-pane name="companies">
        <span slot="label">
          <v-icon name="building"/>
          <!-- Companies -->
          Companies
        </span>
        <benchmark-pane title="Companies" data="companies"/>
      </el-tab-pane>
      <el-tab-pane name="persons">
        <span slot="label">
          <v-icon name="users"/>
          <!-- Persons -->
          Persons
        </span>
        <benchmark-pane title="Persons" data="persons"/>
      </el-tab-pane>
      <el-tab-pane name="deals">
        <span slot="label">
          <v-icon name="handshake"/>
          <!-- Deals -->
          Deals
        </span>
        <benchmark-pane title="Deals" data="deals"/>
      </el-tab-pane>
      <el-tab-pane name="documents">
        <span slot="label">
          <v-icon name="file"/>
          <!-- Documents -->
          Documents
        </span>
        <benchmark-pane title="Documents" data="documents"/>
      </el-tab-pane>
      <el-tab-pane name="histories">
        <span slot="label">
          <v-icon name="history"/>
          <!-- Histories -->
          Histories
        </span>
        <benchmark-pane title="Histories" data="histories"/>
      </el-tab-pane>
    </el-tabs>
  </div>
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
