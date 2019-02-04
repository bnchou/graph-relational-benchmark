<template>
  <div id="app">
    <el-container>
      <el-header>Header</el-header>
      <el-container>
        <el-aside width="200px">Aside</el-aside>
        <el-main>
          <img alt="Vue logo" src="./assets/logo.png">
          <HelloWorld title="Benchmark: Graph vs Relational DB"/>
          <el-row :gutter="20">
            <el-col :span="8">
              <h3>Graph example</h3>
              <LineExample/>
            </el-col>
            <el-col :span="8">
              <h3>Gauge example</h3>
              <GaugeExample/>
            </el-col>
            <el-col :span="8">
              <h3>Pie example</h3>
              <PieExample/>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import LineExample from "./components/LineExample.vue";
import GaugeExample from "./components/GaugeExample.vue";
import PieExample from "./components/PieExample.vue";

export default {
  name: "app",
  components: {
    HelloWorld,
    LineExample,
    GaugeExample,
    PieExample
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
