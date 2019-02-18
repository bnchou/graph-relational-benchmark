import Vue from "vue";

import _ from "lodash";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import "element-ui/lib/theme-chalk/display.css";

import App from "./App";
import Router from "./router";
import Store from "./store";

Vue.config.productionTip = false;
Object.defineProperty(Vue.prototype, "$_", { value: _ });

Vue.use(ElementUI);

new Vue({
  render: h => h(App),
  router: Router,
  store: Store
}).$mount("#app");
