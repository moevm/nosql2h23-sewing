<template>
  <section>
    <div class="content">
      <div class="card">
        <form>
          <div class="container">
            <img src="@/assets/logo.png" id="logo"/>
            <div style="font-size: 12px">
              <div class="form-group">
                <label for="login"><b>E-mail</b></label>
                <input style="font-size: 12px" class="form-control" type="text" placeholder="Введите почту" name="login"
                       id="login" v-model="login" required>
                <p style="color: red">{{ email_message }}</p>
              </div>

              <div class="form-group">
                <label for="psw"><b>Пароль</b></label>
                <input id="psw" style="font-size: 12px" class="form-control" type="password"
                       placeholder="Введите пароль"
                       name="psw" v-model="password" required>
                <p style="color: red">{{ password_message }}</p>
              </div>
            </div>
            <div style="margin-bottom: 1.5vh">
              <input type="checkbox" id="remember-me" name="remember" style="scale: 90%"/>
              <label for="remember-me"
                     style="font-size: 12px; margin-left: 5px; vertical-align: middle; padding-bottom: 1vh">Запомнить
                меня</label>
            </div>
            <button @click.prevent="onSubmit">Войти</button>
          </div>
        </form>
        <a href="/registration" style="text-align: center; font-size: 14px; padding-bottom: 10px">Регистрация</a>

      </div>

    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginPage",
  data() {
    return {
      login: '',
      password: '',
      email_message: '',
      password_message: ''
    }
  },
  methods: {
    onSubmit() {
      if (!this.login) {
        this.email_message = "Введите почту"
        return
      } else this.email_message = ""
      if (!this.password) {
        this.password_message = "Введите пароль"
        return
      } else this.password_message = ""

      axios.post("/api/login", {
            "email": String(this.login),
            "password": String(this.password),
          }, {
            headers: {
              'Accept':
                  'application/json',
              'Content-Type':
                  'application/json'
            }
          }
      ).then((response) => {
        if (response.data["access_token"] && response.data["refresh_token"]) {
          localStorage.setItem("access_token", response.data["access_token"])
          localStorage.setItem("refresh_token", response.data["refresh_token"])
          window.location.href = '/' + response.data["role"] + "/profile"
        }
      }).catch((reason) => alert(reason.response.data.detail))
    }
  }
}
</script>

<style scoped>
section {
  font-family: Ubuntu;
  background-color: #e8e8e8;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card {
  width: 350px;
}

* {
  box-sizing: border-box;
}

.container {
  padding: 16px;
}

input[type=text], input[type=password] {
  width: 100%;
  height: 30px;
  padding: 15px;
  margin: 5px 0 16px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

.register_button {
  height: 30px;
  width: 100%;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
  opacity: 0.9;
}

.register_button:hover {
  opacity: 1;
}

a {
  color: dodgerblue;
}

#logo {
  margin-bottom: 20px;
  text-align: center;
  width: 100%;
}
</style>