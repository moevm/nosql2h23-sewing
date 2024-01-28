<template>
  <HeaderComponent/>
  <div id="wrapper">
    <AdminMenuComponent/>
    <div class="form-check-inline">
      <form>
        <div class="form-group">
          <label><b>Имя менеджера у пользователей</b></label>
          <input class="form-control" placeholder="Введите путь к модели" type="text" v-model="name"/>
        </div>

        <div class="form-group">
          <label><b>Почта менеджера</b></label>
          <input class="form-control" placeholder="Введите путь к модели" type="text" v-model="email"/>
        </div>

        <div class="form-group">
          <label><b>Пароль менеджера</b></label>
          <input class="form-control" placeholder="Введите путь к модели" type="text" v-model="password"/>
        </div>

        <div class="form-group">
          <label><b>Описание менеджера</b></label>
          <input class="form-control" placeholder="Введите путь к модели" type="text" v-model="about"/>
        </div>

        <button class="btn btn-success" @click.prevent="addManager" style="margin-top: 10px; background-color: #0353b2">
          Добавить менеджера
        </button>

        {{ message }}
      </form>
    </div>
  </div>
  <FooterComponent/>
</template>

<script>
import AdminMenuComponent from "@/admin/AdminMenuComponent";
import HeaderComponent from "@/customer/HeaderComponent";
import FooterComponent from "@/FooterComponent";
import axios from "axios";

export default {
  name: "CreateManager",
  components: {AdminMenuComponent, HeaderComponent, FooterComponent},

  data() {
    return {
      name: '',
      email: '',
      password: '',
      about: '',
      message: ''
    }
  },

  methods: {
    addManager() {
      if (!this.name || !this.email || !this.password || !this.about) {
        this.message = "Введены не все данные"
        return
      }

      axios.post("/api/admin/create_manager", {
            "name": String(this.name),
            "email": String(this.email),
            "password": String(this.password),
            "about": String(this.about),
          }, {
            headers: {
              'Accept':
                  'application/json',
              'Content-Type':
                  'application/json'
            }
          }
      ).then(() => {
        this.message = "Менеджер успешно добавлен"
      }).catch((reason) => alert(reason.response.data.detail))
    }
  }
}
</script>

<style scoped>
#wrapper {
  font-family: Ubuntu;
  display: flex;
  margin-left: 4vw;
  width: 92vw;
  min-height: 70vh;
}
</style>