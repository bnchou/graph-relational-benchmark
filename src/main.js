import Vue from "vue";

import _ from "lodash";
import ElementUI from "element-ui";
import VueHighlightJS from "vue-highlightjs";
import Icon from "vue-awesome/components/Icon";
import "highlight.js/styles/agate.css";
import "vue-awesome/icons";
// import "element-ui/lib/theme-chalk/index.css";
// import "element-ui/lib/theme-chalk/display.css";

import App from "./App";
import Router from "./router";
import Store from "./store";
import "./element-variables.scss";

Vue.config.productionTip = false;
Object.defineProperty(Vue.prototype, "$_", { value: _ });

Vue.use(ElementUI);
Vue.use(VueHighlightJS);
Vue.component("v-icon", Icon);

new Vue({
  render: h => h(App),
  router: Router,
  store: Store
}).$mount("#app");
