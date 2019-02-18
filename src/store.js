import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    data: {
      "line-example": {
        columns: ["date", "cost", "profit", "growthRate", "people"],
        rows: [
          {
            cost: 1523,
            date: "01/01",
            profit: 1523,
            growthRate: 0.12,
            people: 100
          },
          {
            cost: 1223,
            date: "01/02",
            profit: 1523,
            growthRate: 0.345,
            people: 100
          },
          {
            cost: 2123,
            date: "01/03",
            profit: 1523,
            growthRate: 0.7,
            people: 100
          },
          {
            cost: 4123,
            date: "01/04",
            profit: 1523,
            growthRate: 0.31,
            people: 100
          },
          {
            cost: 3123,
            date: "01/05",
            profit: 1523,
            growthRate: 0.12,
            people: 100
          },
          {
            cost: 7123,
            date: "01/06",
            profit: 1523,
            growthRate: 0.65,
            people: 100
          }
        ]
      },
      "pie-example": {
        columns: ["date", "cost", "profit"],
        rows: [
          { date: "01/01", cost: 123, profit: 3 },
          { date: "01/02", cost: 1223, profit: 6 },
          { date: "01/03", cost: 2123, profit: 90 },
          { date: "01/04", cost: 4123, profit: 12 },
          { date: "01/05", cost: 3123, profit: 15 },
          { date: "01/06", cost: 7123, profit: 20 }
        ]
      },
      "table-example": {
        columns: ["name", "website", "city"],
        rows: [
          {
            name: "Chang & Fisher Ltd",
            website: "changfisher.com",
            city: "North Laurenshire"
          },
          {
            name: "Boone & Gallagher Inc",
            website: "boonegallagher.biz",
            city: "Katiechester"
          },
          {
            name: "Gould & Brown Ltd",
            website: "gouldbrown.com",
            city: "Lindahaven"
          },
          {
            name: "Stephens & Wood",
            website: "stephenswood.info",
            city: "Hallland"
          }
        ]
      }
    }
  }
});
