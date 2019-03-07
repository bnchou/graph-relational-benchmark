import Vue from "vue";
import VueRouter from "vue-router";

import Benchmark from "@/views/Benchmark";
import InsertionPage from "@/views/Benchmark/Pages/InsertionPage";
import UpdatingPage from "@/views/Benchmark/Pages/UpdatingPage";
import RetrievalPage from "@/views/Benchmark/Pages/RetrievalPage";
import ComplexityPage from "@/views/Benchmark/Pages/ComplexityPage";
import ConfigurationPage from "@/views/Benchmark/Pages/ConfigurationPage";
import AdvancedRetrievalPage from "@/views/Benchmark/Pages/AdvancedRetrievalPage";

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
          component: RetrievalPage
        },
        {
          path: "complexity",
          component: ComplexityPage
        },
        {
          path: "updating",
          component: UpdatingPage
        },
        {
          path: "insertion",
          component: InsertionPage
        },
        {
          path: "settings",
          component: ConfigurationPage
        },
        {
          path: "advanced_retrieval",
          component: AdvancedRetrievalPage
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
