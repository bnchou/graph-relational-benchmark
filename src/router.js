import Vue from "vue";
import VueRouter from "vue-router";

import Benchmark from "@/views/Benchmark";
import Docs from "@/views/Docs";

Vue.use(VueRouter);

export default new VueRouter({
  routes: [
    {
      path: "/",
      component: Benchmark
    },
    {
      path: "/docs",
      component: Docs
    }
  ]
});
