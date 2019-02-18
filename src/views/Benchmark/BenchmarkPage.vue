<template>
  <div>
    <el-tabs type="border-card">
      <el-tab-pane>
        <span slot="label">
          <v-icon name="building"/>
          <!-- Companies -->
          Companies
        </span>
        Fetching companies...
      </el-tab-pane>
      <el-tab-pane>
        <span slot="label">
          <v-icon name="users"/>
          <!-- Peoples -->
          Peoples
        </span>
        Fetching peoples...
      </el-tab-pane>
      <el-tab-pane>
        <span slot="label">
          <v-icon name="handshake"/>
          <!-- Deals -->
          Deals
        </span>
        Fetching deals...
      </el-tab-pane>
      <el-tab-pane>
        <span slot="label">
          <v-icon name="file"/>
          <!-- Documents -->
          Documents
        </span>
        Fetching documents...
      </el-tab-pane>
      <el-tab-pane>
        <span slot="label">
          <v-icon name="history"/>
          <!-- Histories -->
          Histories
        </span>
        Fetching histories...
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  }
};
</script>

<style scoped>
</style>
