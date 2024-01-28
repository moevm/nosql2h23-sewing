<template>
  <HeaderComponent/>
  <h1 class="display-1"
      style="text-align: center; font-size: 46px; font-family: Ubuntu; padding-top: 10px; color: #24509c">
    Редактирование заказчика
  </h1>
  <div id="wrapper">
    <AdminMenuComponent/>
    <div class="form-check-inline">
      <form>
        <div class="form-group">
          <label><b>ID</b></label>
          <input class="form-control" type="text" v-model="this.user['_id']" disabled/>
        </div>

        <div class="form-group">
          <label><b>Наименование</b></label>
          <input class="form-control" type="text" v-model="this.user['name']"/>
        </div>

        <div class="form-group">
          <label><b>Контактное лицо</b></label>
          <input class="form-control" type="text" v-model="this.user['contact_person']"/>
        </div>

        <div class="form-group">
          <label><b>Телефон</b></label>
          <input class="form-control" type="text" v-model="this.user['phone']"/>
        </div>

        <div class="form-group">
          <label><b>Почта</b></label>
          <input class="form-control" type="text" v-model="this.user['email']"/>
        </div>

        <div class="form-group">
          <label><b>ИНН</b></label>
          <input class="form-control" type="text" v-model="this.user['TIN']"/>
        </div>

        <div class="form-group" style="width: 40vw">
          <label><b>Описание</b></label>
          <textarea class="form-control" type="text" v-model="this.user['about']" style="min-height: 20vh"></textarea>
        </div>

        <button class="btn btn-success" @click="updateUser" style="margin-top: 10px; background-color: green">
          Внести изменения
        </button>
      </form>
    </div>
  </div>
  <FooterComponent/>
</template>

<script>
import {defineComponent} from "vue";
import AdminMenuComponent from "@/admin/AdminMenuComponent";
import HeaderComponent from "@/customer/HeaderComponent";
import FooterComponent from "@/FooterComponent";
import axios from "axios";

export default defineComponent({
  name: 'CustomerEditor',
  components: {HeaderComponent, FooterComponent, AdminMenuComponent},

  data() {
    return {
      user: {},
      message: ''
    }
  },

  methods: {
    updateUser() {
      this.user["user_id"] = this.user["_id"]

      axios.post("/api/admin/update_user", this.user, {
        headers: {
          "Content-Type": "application/json",
        },
      })
    },

    get_user() {
      axios.get("/api/admin/customers/" + this.$route.params["id"], {
        headers: {
          "Content-Type": "application/json",
        }
      }).then((response) => {
        this.user = response.data;
      })
    }
  },

  mounted()
  {
    this.get_user()
  }
})
</script>

<style scoped>
#wrapper {
  font-family: Ubuntu;
  display: flex;
  margin-left: 4vw;
  width: 92vw;
  min-height: 70vh;
}

td {
  padding-right: 15px;
  padding-left: 15px;
  border: 1px solid #c4c4c4;
  height: 5vh
}

table th {
  background: #333333;
  color: white;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 15px;
}
</style>