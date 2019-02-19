import Vue from "vue";
import VueRouter from "vue-router";

import Benchmark from "@/views/Benchmark";
import BenchmarkPage from "@/views/Benchmark/BenchmarkPage";
import ConfigurationPage from "@/views/Benchmark/ConfigurationPage";
import Docs from "@/views/Docs";
import IntroductionPage from "@/views/Docs/IntroductionPage";
import QuickStartPage from "@/views/Docs/QuickStartPage";
import ComponentsPage from "@/views/Docs/ComponentsPage";

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
