<template>
  <div>
    <el-form ref="registerForm" :model="form" :rules="rules" label-width="80px" class="register-box">
      <h3 class="register-title">欢迎Register</h3>
      <el-form-item label="账号" prop="username">
        <el-input type="text" placeholder="请输入用户名" v-model="form.username"/>
      </el-form-item>
      <el-form-item label="mail" prop="email">
        <el-input type="text" placeholder="请输入mail" v-model="form.email"/>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input type="password" placeholder="请输入密码" v-model="form.password"/>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" v-on:click="onSubmit('registerForm')">Register</el-button>
      </el-form-item>
    </el-form>

    <el-dialog
      title="温馨提示"
      :visible.sync="dialogVisible"
      width="30%"
      :before-close="handleClose">
      <span>请输入用户名和密码</span>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  export default {
    name: "Register",
    data() {
      return {
        form: {
          username: '',
          email: '',
          password: ''
        },

        // 表单验证，需要在 el-form-item 元素中增加 prop 属性
        rules: {
          username: [
            {required: true, message: '账号不可为空', trigger: 'blur'}
          ],
          email: [
            {required: true, message: 'Email不可为空', trigger: 'blur'}
          ],
          password: [
            {required: true, message: '密码不可为空', trigger: 'blur'}
          ]
        },

        // 对话框显示和隐藏
        dialogVisible: false
      }
    },
    methods: {
      onSubmit(formName) {
        // 为表单绑定验证功能
        this.$refs[formName].validate((valid) => {
          if (valid) {
            // 使用 vue-router 路由到指定页面，该方式称之为编程式导航

        this.$axios({
          url: 'user/register/',
          method: 'post',
          data: {
            username: this.form.username,
            email: this.form.email,
            password: this.form.password
          }
        }).then(res => {
          let result = res.data
          alert(result.msg)
          //alert(res.status)
          if (result.msg == 'succeed to register') {
            alert(result.data[0].username)
            alert(result.data[0].token)
            //sessionStorage.setItem('user', this.form.username);
            sessionStorage.setItem('user', result.data[0].username);
            sessionStorage.setItem('token',result.data[0].token)
            //localStorage.setItem('token',result.data[0].token)
            this.$store.dispatch('setUser', this.form.username);
            this.$router.push("/");
          }
          else {
            alert('register please')
          }
        })

          } else {
            this.dialogVisible = true;
            return false;
          }
        });
      }
    }
  }
</script>

<style lang="css" scoped>
  .register-box {
    border: 1px solid #DCDFE6;
    width: 350px;
    margin: 180px auto;
    padding: 35px 35px 15px 35px;
    border-radius: 5px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    box-shadow: 0 0 25px #909399;
    background: #fff;
  }

  .register-title {
    text-align: center;
    margin: 0 auto 40px auto;
    color: #303133;
  }
</style>
