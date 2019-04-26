import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    executionData: {},
    data: {}
  },
  getters: {
    getIcon: () => icon => {
      switch (icon) {
        case "companies":
          return "building";
        case "person":
        case "persons":
        case "filter_coworkers":
        case "relationships":
        case "related":
          return "users";
        case "deal":
        case "deals":
          return "handshake";
        case "history":
        case "histories":
        case "histories_type":
        case "filter_histories":
          return "history";
        default:
          return "question";
      }
    }
  }
});
