<template>
  <section>
    <div class="content">
      <div class="card">
        <form>
          <div class="container">
            <img src="@/assets/logo.png" id="logo" alt="logo"/>
            <div style="font-size: 12px">
              <div class="form-group">
                <label for="login"><b>Email</b></label>
                <input style="font-size: 12px" class="form-control" type="text" placeholder="Введите логин" name="login"
                       id="login" v-model="login" required>
              </div>

              <div class="form-group">
                <label for="psw"><b>Пароль</b></label>
                <input style="font-size: 12px" class="form-control" type="password" placeholder="Введите пароль"
                       name="psw" id="psw" v-model="password" required>
              </div>  

              <div class="form-group">
                <label for="inn"><b>ИНН</b></label>
                <input style="font-size: 12px" class="form-control" type="text" placeholder="Введите ИНН" name="inn"
                       id="inn" v-model="TIN" required>
              </div>

              <div class="form-group">
                <label for="company-name"><b>Наименование компании</b></label>
                <input style="font-size: 12px" class="form-control" type="text" placeholder="Введите имя компании"
                       name="company-name"
                       id="company-name" v-model="companyName" required>
              </div>

              <div class="form-group">
                <label for="contact"><b>Контактное лицо (ФИО - должность)</b></label>
                <input style="font-size: 12px" class="form-control" type="text" placeholder="Введите контактное лицо"
                       name="contact"
                       id="contact" v-model="contact_person" required>
              </div>

              <div class="form-group">
                <label for="phone"><b>Телефон для связи</b></label>
                <input style="font-size: 12px" class="form-control" type="text" placeholder="+7 (XXX)-XXX-XXXX"
                       name="phone"
                       id="phone" v-model="phone" required>
              </div>

              <div class="form-group" style="padding-bottom: 1.5vh">
                <label class="radio-inline">
                  <input type="radio" style="vertical-align: middle" value="customer" v-model="pickedRadio"  checked>
                  <label style="padding-left: 5px; vertical-align: middle">
                    Покупатель
                  </label>
                </label>
                <label class="radio-inline" style="margin-left: 20px; margin-bottom: 6px;">
                  <input type="radio" style="vertical-align: middle" value="company" v-model="pickedRadio">
                  <label style="padding-left: 5px; vertical-align: middle">
                    Поставщик
                  </label>
                </label>
              </div>
            </div>
            <button @click.prevent="onSubmit" class="register_button" ref="submit">Регистрация</button>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  name: "RegistrationPage",

  data() {
    return {
      login: '',
      password: '',
      TIN: '',
      companyName: '',
      contact_person: '',
      phone: '',
      pickedRadio: "customer",
    }
  },

  methods: {
    onSubmit() {
      let register_url = "/api/" + this.pickedRadio + "/register"

      axios.post(register_url, {
            "email": String(this.login),
            "password": String(this.password),
            "TIN": String(this.TIN),
            "name": String(this.companyName),
            "contact_person": String(this.contact_person),
            "phone": String(this.phone),
          }, {
            headers: {
              'Accept':
                  'application/json',
              'Content-Type':
                  'application/json'
            }
          }
      ).then((response) => {
        if (response.status === 201) {
          window.location.href = "/wait_page"
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
  padding-bottom: 4px;
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