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
        <h3>Graph example</h3>
        <LineExample/>
      </el-col>
      <el-col :sm="8">
        <h3>Gauge example</h3>
        <GaugeExample/>
      </el-col>
      <el-col :sm="8">
        <h3>Pie example</h3>
        <PieExample/>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import LineExample from "@/components/LineExample.vue";
import GaugeExample from "@/components/GaugeExample.vue";
import PieExample from "@/components/PieExample.vue";

export default {
  props: {
    title: String
  },
  components: {
    LineExample,
    GaugeExample,
    PieExample
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
