<template>
  <div class="outside-background">
    <form action="//msiter.ru/action_page.php">
      <div class="container">
<!--        <img src="@/assets/logo.png" id="logo"/>-->

        <hr>
        <div class="form-group">
          <label for="login"><b>Логин</b></label>
          <input class="form-control" type="text" placeholder="Введите логин" name="login" id="login" required>
        </div>

        <div class="form-group">
          <label for="psw"><b>Пароль</b></label>
          <input class="form-control" type="password" placeholder="Введите пароль" name="psw" id="psw" required>
        </div>
        <hr>

        <button type="submit" class="registerbtn">Войти</button>
      </div>
    </form>
  </div>

</template>

<script>
export default {
  name: "MyLogin"
}
</script>

<style scoped>
.outside-background {
  width: 100vw;
  height: 100vh;
  background-color: black;
}

.login-form {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50%;
  height: 50%;
  background-color: white;

}



/* Добавляем отступы для контейнеров */
.container {
  padding: 16px;
  text-align: center;
  /*background: red;*/
}

/* Поля ввода на всю ширину */
input[type=text], input[type=password] {
  width: 50%;
  padding: 15px;
  /*margin: 5px 0 22px 0;*/
  display: block;
  margin: auto;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

/* Переопределяем стиль по умолчанию для hr */
hr {
  border: none;
  margin-bottom: 25px;
}

/* Стиль для кнопки регистрации */
.registerbtn {
  background-color: #4CAF50;
  color: white;
  padding: 16px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 50%;
  opacity: 0.9;
}

.registerbtn:hover {
  opacity: 1;
}

/* Добавляем синий цвет для текста ссылок */
a {
  color: dodgerblue;
}

#logo {
  text-align: center;
}
</style>