<template>
  <section>
    <div class="content">
      <div class="card">
        <form action="//msiter.ru/action_page.php">
          <div class="container">
            <img src="@/assets/logo.png" id="logo"/>
            <div style="font-size: 12px">
              <div class="form-group">
                <label for="login"><b>Логин</b></label>
                <input style="font-size: 12px" class="form-control" type="text" placeholder="Введите логин" name="login"
                       id="login" required>
              </div>

              <div class="form-group">
                <label for="psw"><b>Пароль</b></label>
                <input style="font-size: 12px" class="form-control" type="password" placeholder="Введите пароль"
                       name="psw" id="psw" required>
              </div>
            </div>
            <div>
              <input type="checkbox" id="remember-me" name="remember" style="scale: 90%"/>
              <label for="remember-me" style="font-size: 12px; margin-left: 5px; margin-bottom: 5px">Remember Me</label>
            </div>
            <button type="submit" class="registerbtn">Войти</button>
          </div>
          <VueRecaptcha
              :sitekey="siteKey"
              :load-recaptcha-script="true"
              @verify="handleSuccess"
              @error="handleError"
          ></VueRecaptcha>
        </form>
      </div>
    </div>
  </section>
</template>

<script>
import {VueRecaptcha} from 'vue-recaptcha';

export default {
  name: "LoginPage",
  components: {
    VueRecaptcha
  },
}
</script>

<style scoped>
section {
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

.registerbtn {
  height: 30px;
  width: 100%;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
  opacity: 0.9;
}

.registerbtn:hover {
  opacity: 1;
}

a {
  color: dodgerblue;
}

#logo {
  margin-bottom: 20px;
  text-align: center;
}
</style>