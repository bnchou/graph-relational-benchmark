<template>
  <el-tabs type="border-card" @tab-click="handleClick" :stretch="true" style="min-height: 80vh;">
    <el-tab-pane name="companies" v-loading="isLoading">
      <span slot="label">
        <v-icon name="building"/>
        <!-- Companies -->
        Companies
      </span>
      <benchmark-pane title="Companies" data="companies" :isLoading="isLoading"/>
    </el-tab-pane>
    <el-tab-pane name="persons" v-loading="isLoading">
      <span slot="label">
        <v-icon name="users"/>
        <!-- Persons -->
        Persons
      </span>
      <benchmark-pane title="Persons" data="persons" :isLoading="isLoading"/>
    </el-tab-pane>
    <el-tab-pane name="deals" v-loading="isLoading">
      <span slot="label">
        <v-icon name="handshake"/>
        <!-- Deals -->
        Deals
      </span>
      <benchmark-pane title="Deals" data="deals" :isLoading="isLoading"/>
    </el-tab-pane>
    <el-tab-pane name="documents" v-loading="isLoading">
      <span slot="label">
        <v-icon name="file"/>
        <!-- Documents -->
        Documents
      </span>
      <benchmark-pane title="Documents" data="documents" :isLoading="isLoading"/>
    </el-tab-pane>
    <el-tab-pane name="histories" v-loading="isLoading">
      <span slot="label">
        <v-icon name="history"/>
        <!-- Histories -->
        Histories
      </span>
      <benchmark-pane title="Histories" data="histories" :isLoading="isLoading"/>
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
