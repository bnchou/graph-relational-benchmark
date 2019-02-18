<template>
  <div>
    <h1>{{ title }}</h1>
    <p>This project enables you to benchmark graph and relational databases to compare their performance.</p>
    <h3>Packages</h3>
    <ul>
      <li>
        <a href="https://router.vuejs.org" target="_blank">vue-router</a>
      </li>
      <li>
        <a href="https://vuex.vuejs.org" target="_blank">vuex</a>
      </li>
      <li>
        <a href="https://github.com/vuejs/vue-devtools#vue-devtools" target="_blank">vue-devtools</a>
      </li>
      <li>
        <a href="https://vue-loader.vuejs.org" target="_blank">vue-loader</a>
      </li>
      <li>
        <a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a>
      </li>
    </ul>
    <el-row :gutter="20">
      <el-col :sm="8">
        <h3>Table example</h3>
        <table-example/>
      </el-col>
      <el-col :sm="8">
        <h3>Graph example</h3>
        <line-example/>
      </el-col>
      <el-col :sm="8">
        <h3>Pie example</h3>
        <pie-example/>
      </el-col>
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
import TableExample from "./Examples/TableExample.vue";
import LineExample from "./Examples/LineExample.vue";
import PieExample from "./Examples/PieExample.vue";

export default {
  props: {
    title: String
  },
  data: function() {
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
          stmt: "flat_select",
          cypher: -1,
          sql: -1
        },
        {
          id: 2,
          query: "Nested select statement",
          stmt: "nested_select",
          cypher: -1,
          sql: -1
        }
      ]
    };
  },
  components: {
    TableExample,
    LineExample,
    PieExample
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
    }
  }
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
