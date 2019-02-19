<template>
  <div>
    <el-tabs 
      type="border-card"
      @tab-click="handleClick"
    >
      <el-tab-pane name="update_companies">
        <span slot="label">
          <v-icon name="building"/>
          <!-- Companies -->
          Companies
        </span>
        Fetching companies...
      </el-tab-pane>
      <el-tab-pane name="persons">
        <span slot="label">
          <v-icon name="users"/>
          <!-- Peoples -->
          Peoples
        </span>
        Fetching peoples...
      </el-tab-pane>
      <el-tab-pane name="deal">
        <span slot="label">
          <v-icon name="handshake"/>
          <!-- Deals -->
          Deals
        </span>
        Fetching deals...
      </el-tab-pane>
      <el-tab-pane name="update_deals">
        <span slot="label">
          <v-icon name="file"/>
          <!-- Documents -->
          Documents
        </span>
        Fetching documents...
      </el-tab-pane>
      <el-tab-pane name="history">
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
    return {   
    };
  },
methods: { 
    handleClick: async (tab, event) => {
      const res = await fetch(`/api/command/${tab.name}`);
      const json = await res.json();
      console.log(json)
    }
  }
};
</script>

<style scoped>
</style>
