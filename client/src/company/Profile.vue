<template>
  <HeaderComponent/>
  <div id="wrapper">
    <MenuComponent/>
    <div class="form-check-inline" style="width: 30vw">
      <h3>Личный кабинет производителя</h3>
      <div class="form-group">
        <label><b>Почта</b></label>
        <input class="form-control" type="text" v-model="this.user['email']" disabled/>
      </div>

      <div class="form-group">
        <label><b>ИНН</b></label>
        <input class="form-control" type="text" v-model="this.user['TIN']" disabled/>
      </div>

      <div class="form-group">
        <label><b>Контактное лицо</b></label>
        <input class="form-control" type="text"
               v-model="this.user['contact_person']" disabled/>
      </div>

      <div class="form-group">
        <label><b>Телефон</b></label>
        <input class="form-control" type="text" v-model="this.user['phone']" disabled/>
      </div>
    </div>
  </div>
  <FooterComponent/>
</template>

<script>
import HeaderComponent from "@/company/HeaderComponent";
import MenuComponent from "@/company/MenuComponent";
import FooterComponent from "@/FooterComponent";
import axios from "axios";

export default {
  name: "ProfilePage",

  components: {HeaderComponent, MenuComponent, FooterComponent},

  data() {
    return {
      user: {}
    }
  },

  methods: {
    get_user() {
      axios.post("/api/company/profile", {
            "token": localStorage.getItem("access_token"),
          }, {
            headers: {
              'Accept':
                  'application/json',
              'Content-Type':
                  'application/json'
            }
          }
      ).then((response) => this.user = response.data)
    }
  },

  mounted() {
    this.get_user()
  }
}
</script>

<style scoped>
#wrapper {
  font-family: Ubuntu;
  display: flex;
  margin-left: 4vw;
  min-height: 70vh;
}
</style>