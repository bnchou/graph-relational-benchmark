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
      <el-col :sm="8">
        <h3>Fetch cypher api</h3>
        <el-button
          @click="handle(0, () => insert('cypher'))"
          :loading="buttons[0].loading"
          :disabled="buttons[0].disabled"
        >Fetch</el-button>
        {{ cypher.time }} ms
      </el-col>
      <el-col :sm="8">
        <h3>Fetch mssql api</h3>
        <el-button
          @click="handle(1, () => insert('mssql'))"
          :loading="buttons[1].loading"
          :disabled="buttons[1].disabled"
        >Fetch</el-button>
        {{ mssql.time }} ms
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
  data: function() {
    return {
      cypher: {},
      mssql: {},
      buttons: [
        { loading: false, disabled: false },
        { loading: false, disabled: false }
      ]
    };
  },
  components: {
    LineExample,
    GaugeExample,
    PieExample
  },
  methods: {
    insert: async function(adapter) {
      const res = await fetch(`/api/${adapter}/insert`);
      const json = await res.json();
      this[adapter] = json;
    },
    handle: async function(id, func) {
      this.buttons[id].loading = true;
      this.buttons.filter(b => b.id !== id).forEach(b => (b.disabled = true));
      await func();
      this.buttons[id].loading = false;
      this.buttons.filter(b => b.id !== id).forEach(b => (b.disabled = false));
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
