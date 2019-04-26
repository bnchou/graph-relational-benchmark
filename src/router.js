import Vue from "vue";
import VueRouter from "vue-router";

import Benchmark from "@/views/Benchmark";
import BenchmarkPage from "@/views/Benchmark/Pages/BenchmarkPage";
import ConfigurationPage from "@/views/Benchmark/Pages/ConfigurationPage";

import Docs from "@/views/Docs";
import IntroductionPage from "@/views/Docs/Pages/IntroductionPage";

Vue.use(VueRouter);

export default new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      redirect: "/benchmark"
    },
    {
      path: "/benchmark",
      redirect: "/benchmark/retrieval",
      component: Benchmark,
      children: [
        {
          path: "retrieval",
          component: BenchmarkPage,
          props: { method: "get" }
        },
        {
          path: "insertion",
          component: BenchmarkPage,
          props: { method: "post" }
        },
        {
          path: "updating",
          component: BenchmarkPage,
          props: { method: "put" }
        },
        {
          path: "settings",
          component: ConfigurationPage
        }
      ]
    },
    {
      path: "/docs",
      component: Docs,
      redirect: "/docs/intro",
      children: [
        {
          path: "intro",
          component: IntroductionPage
        }
      ]
    }
  ]
});
