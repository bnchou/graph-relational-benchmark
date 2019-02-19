<template>
  <div>
    <el-tabs type="border-card" @tab-click="handleClick">
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
      <el-tab-pane name="deals">
        <span slot="label">
          <v-icon name="handshake"/>
          <!-- Deals -->
          Deals
        </span>
        Fetching deals...
      </el-tab-pane>
      <el-tab-pane name="documents">
        <span slot="label">
          <v-icon name="file"/>
          <!-- Documents -->
          Documents
        </span>
        Fetching documents...
      </el-tab-pane>
      <el-tab-pane name="histories">
        <span slot="label">
          <v-icon name="history"/>
          <!-- Histories -->
          Histories
        </span>
        Fetching histories...
      </el-tab-pane>
    </el-tabs>
    <el-row :gutter="20">
      <el-col>
        <h3>Large data insert</h3>
        <el-table :data="tableData">
          <el-table-column prop="query" label="Query"></el-table-column>
          <el-table-column label="Neo4j" width="140">
            <template slot-scope="scope">
              <el-tag size="medium">{{ scope.row.cypher }} ms</el-tag>
              <el-button
                circle
                type="text"
                icon="el-icon-refresh"
                @click="handle('cypher', scope.row.id, scope.row.stmt)"
                :loading="cypher.loading[scope.row.id]"
                :disabled="isDisabled"
              ></el-button>
            </template>
          </el-table-column>
          <el-table-column label="MS SQL" width="140">
            <template slot-scope="scope">
              <el-tag size="medium">{{ scope.row.sql }} ms</el-tag>
              <el-button
                circle
                type="text"
                icon="el-icon-refresh"
                @click="handle('sql', scope.row.id, scope.row.stmt)"
                :loading="sql.loading[scope.row.id]"
                :disabled="isDisabled"
              ></el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cypher: { loading: {} },
      sql: { loading: {} },
      isDisabled: false,
      tableData: [
        {
          id: 0,
          query: "Reset Database",
          stmt: "reset",
          cypher: -1,
          sql: -1
        },
        {
          id: 1,
          query: "Flat select statement",
          stmt: "deals",
          cypher: -1,
          sql: -1
        },
        {
          id: 2,
          query: "Nested select statement",
          stmt: "histories",
          cypher: -1,
          sql: -1
        }
      ]
    };
  },
  methods: {
    handle: async function(adapter, id, stmt) {
      this.$set(this[adapter].loading, id, true);
      this.isDisabled = true;

      // const res = await fetch(`/api/${adapter}/${stmt}`);

      const res = await fetch(`/api/command/${stmt}`);
      const json = await res.json();
      this.tableData[id][adapter] = json.data;

      this.$set(this[adapter].loading, id, false);
      this.isDisabled = false;
    },
    handleClick: async (tab, event) => {
      const res = await fetch(`/api/command/${tab.name}`);
      const json = await res.json();
      console.log(json);
    }
  }
};
</script>

<style scoped>
</style>
