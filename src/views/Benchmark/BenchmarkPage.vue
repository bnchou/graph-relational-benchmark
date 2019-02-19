<template>
  <el-tabs type="border-card" @tab-click="handleClick">
    <el-tab-pane name="companies">
      <span slot="label">
        <v-icon name="building"/>
        <!-- Companies -->
        Companies
      </span>
      Fetching companies...
      {{executionData.companies}}
    </el-tab-pane>
    <el-tab-pane name="persons">
      <span slot="label">
        <v-icon name="users"/>
        <!-- Persons -->
        Persons
      </span>
      Fetching persons...
      {{executionData.persons}}
    </el-tab-pane>
    <el-tab-pane name="deals">
      <span slot="label">
        <v-icon name="handshake"/>
        <!-- Deals -->
        Deals
      </span>
      Fetching deals...
      {{executionData.deals}}
    </el-tab-pane>
    <el-tab-pane name="documents">
      <span slot="label">
        <v-icon name="file"/>
        <!-- Documents -->
        Documents
      </span>
      Fetching documents...
      {{executionData.documents}}
    </el-tab-pane>
    <el-tab-pane name="histories">
      <span slot="label">
        <v-icon name="history"/>
        <!-- Histories -->
        Histories
      </span>
      Fetching histories...
      {{executionData.histories}}
    </el-tab-pane>
  </el-tabs>
</template>

<script>
export default {
  data() {
    return {
      isLoading: false,
      executionData: {}
    };
  },
  methods: {
    handleClick: async function(tab) {
      this.isLoading = true;

      const res = await fetch(`/api/command/${tab.name}`);
      const json = await res.json();
      this.$set(this.executionData, tab.name, json);

      this.isLoading = false;
    }
  }
};
</script>

<style scoped>
</style>
