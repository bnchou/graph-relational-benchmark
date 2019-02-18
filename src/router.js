import Vue from "vue";
import VueRouter from "vue-router";

import Benchmark from "@/views/Benchmark";
import BenchmarkPage from "@/views/Benchmark/BenchmarkPage";
import ConfigurationPage from "@/views/Benchmark/ConfigurationPage";
import Docs from "@/views/Docs";

Vue.use(VueRouter);

export default new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      component: Benchmark,
      children: [
        {
          path: "",
          component: BenchmarkPage
        },
        {
          path: "settings",
          component: ConfigurationPage
        }
      ]
    },
    {
      path: "/docs",
      component: Docs
    }
  ]
});
