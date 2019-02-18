<template>
  <el-table :data="tableData.rows" style="width: 100%">
    <el-table-column
      v-for="column in tableData.columns"
      :key="column"
      :prop="column"
      :label="$_.capitalize(column)"
    ></el-table-column>
  </el-table>
</template>

<script>
export default {
  data() {
    return {
      tableData: this.$store.state.data["table-example"]
    };
  }
};
</script>