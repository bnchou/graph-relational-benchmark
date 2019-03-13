<template>
  <div>
    <el-tabs type="border-card" :stretch="true" style="min-height: 80vh;">
      <el-tab-pane
        :key="key"
        :name="`${method}_${key}`"
        v-loading="isLoading"
        v-for="(query, key) in commands[method]"
      >
        <span slot="label">
          <v-icon :name="getIcon(key)"/>
          <!-- Newline -->
          {{$_.startCase(key)}}
        </span>
        <h1>
          {{$_.startCase(key)}}
          <el-button @click="() => handleClick(`${method}_${key}`)" icon="el-icon-refresh" circle></el-button>
        </h1>
        <benchmark-pane :data="`${method}_${key}`" :query="query" :isLoading="isLoading"/>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import _ from "lodash";
import BenchmarkPane from "@/components/Panes/BenchmarkPane";

export default {
  props: {
    method: String
  },
  components: { BenchmarkPane },
  data() {
    return {
      isLoading: false,
      commands: {}
    };
  },
  async created() {
    const res = await fetch("/api/commands");
    const commands = await res.json();
    const ncommands = _.map(commands, (methods, dialect) =>
      _.mapValues(methods, queries =>
        _.mapValues(queries, value => ({ [dialect]: value }))
      )
    );
    this.commands = _.merge(...ncommands);
  },
  methods: {
    handleClick: async function(action) {
      this.isLoading = true;

      const res = await fetch(`/api/command/${action}`);
      const json = await res.json();

      this.$set(this.$store.state.executionData, action, json);

      this.isLoading = false;
    },
    getIcon: function(key) {
      return this.$store.state.icons[key];
    }
  }
};
</script>

<style scoped>
</style>
