<template>
  <section>
    <div class="content">
      <div class="card">
        <form>
          <div class="container">
            <img src="@/assets/logo.png" id="logo"/>
            <div style="font-size: 12px">
              <div class="form-group">
                <label for="login"><b>Логин/Email</b></label>
                <input style="font-size: 12px" class="form-control" type="text" placeholder="Введите логин" name="login"
                       id="login" ref="login" required>
              </div>

              <div class="form-group">
                <label for="psw"><b>Пароль</b></label>
                <input style="font-size: 12px" class="form-control" type="password" placeholder="Введите пароль"
                       name="psw" id="psw" ref="psw" required>
              </div>

              <div class="form-group">
                <label for="inn"><b>ИНН</b></label>
                <input style="font-size: 12px" class="form-control" type="text" placeholder="Введите ИНН" name="inn"
                       id="inn" ref="inn" required>
              </div>

              <div class="form-group">
                <label for="company-name"><b>Наименование компании</b></label>
                <input style="font-size: 12px" class="form-control" type="text" placeholder="Введите имя компании"
                       name="company-name"
                       id="company-name" ref="companyName" required>
              </div>

              <div class="form-group">
                <label for="contact"><b>Контактное лицо (ФИО - должность)</b></label>
                <input style="font-size: 12px" class="form-control" type="text" placeholder="Введите контактное лицо"
                       name="contact"
                       id="contact" ref="contact" required>
              </div>

              <div class="form-group">
                <label for="phone"><b>Телефон для связи</b></label>
                <input style="font-size: 12px" class="form-control" type="text" placeholder="+7 (XXX)-XXX-XXXX"
                       name="phone"
                       id="phone" ref="phone" required>
              </div>

              <div class="form-group">
                <label class="radio-inline">
                  <input type="radio" name="optradio" ref="customerRadio" checked>Покупатель
                </label>
                <label class="radio-inline" style="margin-left: 10px; margin-bottom: 6px;">
                  <input type="radio" name="optradio" ref="companyRadio">Поставщик
                </label>
              </div>
            </div>
            <button type="submit" class="registerbtn" ref="submit">Регистрация</button>
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
export default {
  name: "RegistrationPage",
  mounted() {
    this.$refs.submit.addEventListener('click', () => {
      let url = ""
      if (this.$refs.customerRadio.checked) {
        url = 'http://127.0.0.1:3000/api/customer/register'
      } else {
        url = 'http://127.0.0.1:3000/api/company/register'
      }

      fetch(url, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          "email": String(this.$refs.login.value),
          "password": String(this.$refs.psw.value),
          "TIN": String(this.$refs.inn.value),
          "name": String(this.$refs.companyName.value),
          "contact_person": String(this.$refs.contact.value),
          "phone": String(this.$refs.phone.value)
        })
      })
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