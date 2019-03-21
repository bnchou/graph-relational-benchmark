<template>
  <div>
    <h2>Configuration</h2>
    <el-form ref="form" :model="form" :rules="rules" label-width="130px">
      <el-form-item label="Query Amount" prop="amount">
        <el-input v-model="form.amount"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit('form')">Save</el-button>
      </el-form-item>
    </el-form>

    <h3>Database size</h3>
    <div class="div-padding">
      <el-button plain>Small</el-button>
      <span>~10,000 entries</span>
    </div>
    <div class="div-padding">
      <el-button plain>Medium</el-button>
      <span>~100,000 entries</span>
    </div>
    <div>
      <el-button plain>Large</el-button>
      <span>~4,000,000 entries</span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    const checkInteger = (rule, value, callback) => {
      if (isNaN(value)) {
        return callback(new Error("Please input digits"));
      }
      return callback();
    };

    return {
      form: {
        amount: ""
      },
      rules: {
        amount: [
          {
            required: true,
            message: "Please enter an amount",
            trigger: "blur"
          },
          {
            validator: checkInteger,
            trigger: "change"
          }
        ]
      }
    };
  },
  methods: {
    onSubmit(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          fetch("/api/command/amount", {
            method: "POST",
            body: this.form.amount
          });
          return true;
        }
        // Invalid input
        return false;
      });
    }
  }
};
</script>

<style scoped>
.el-input {
  width: 80px;
  margin-right: 4px;
}

.div-padding {
  padding-bottom: 8px;
}

.el-button {
  width: 90px;
  margin-right: 8px;
}
</style>
