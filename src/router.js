import Vue from "vue";
import VueRouter from "vue-router";

import Benchmark from "@/views/Benchmark";
import BenchmarkPage from "@/views/Benchmark/Pages/BenchmarkPage";
import ComplexityPage from "@/views/Benchmark/Pages/ComplexityPage";
import ConfigurationPage from "@/views/Benchmark/Pages/ConfigurationPage";

import Docs from "@/views/Docs";
import IntroductionPage from "@/views/Docs/Pages/IntroductionPage";
import QuickStartPage from "@/views/Docs/Pages/QuickStartPage";
import ComponentsPage from "@/views/Docs/Pages/ComponentsPage";

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
          path: "complexity",
          component: ComplexityPage
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
        },
        {
          path: "quick-start",
          component: QuickStartPage
        },
        {
          path: "components",
          component: ComponentsPage
        }
      ]
    }
  ]
});
