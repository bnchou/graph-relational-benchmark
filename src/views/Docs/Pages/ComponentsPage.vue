<template>
  <div>
    <h1>Components</h1>
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
    </el-row>
  </div>
</template>

<script>
import TableExample from "@/components/Charts/TableExample.vue";
import LineExample from "@/components/Charts/LineExample.vue";
import PieExample from "@/components/Charts/PieExample.vue";

export default {
  components: {
    TableExample,
    LineExample,
    PieExample
  }
};
</script>

<style>
</style>
