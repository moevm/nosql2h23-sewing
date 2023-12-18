<template>
  <section>
    <div class="content">
      <div class="card">
        <form>
          <div class="container">
            <img src="@/assets/logo.png" id="logo"/>
            <div style="font-size: 12px">
              <div class="form-group">
                <label for="login"><b>Логин</b></label>
                <input style="font-size: 12px" class="form-control" type="text" placeholder="Введите логин" name="login"
                       id="login" ref="login" required>
              </div>

              <div class="form-group">
                <label for="psw"><b>Пароль</b></label>
                <input style="font-size: 12px" class="form-control" type="password" ref="psw" placeholder="Введите пароль"
                       name="psw" id="psw" required>
              </div>
            </div>
            <div>
              <input type="checkbox" id="remember-me" name="remember" style="scale: 90%"/>
              <label for="remember-me" style="font-size: 12px; margin-left: 5px; margin-bottom: 5px">Запомнить меня</label>
            </div>
            <button type="submit" class="registerbtn" ref="submit">Войти</button>
          </div>
        </form>
        <a href="/registration" style="text-align: center; font-size: 14px; padding-bottom: 10px">Регистрация</a>

      </div>

    </div>
  </section>
</template>

<script>
export default {
  name: "LoginPage",
  mounted() {
    this.$refs.submit.addEventListener('click', async () => {
      const response = await fetch("http://127.0.0.1:3000/api/customer/login", {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          "email": String(this.$refs.login.value),
          "password": String(this.$refs.psw.value),
        })
      })
      console.log(await response.json()["access_token"])
    })
  }
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
  width: 100%;
}
</style>