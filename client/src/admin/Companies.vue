<template>
  <HeaderComponent/>
  <h1 class="display-1"
      style="text-align: center; font-size: 46px; font-family: Ubuntu; padding-top: 10px; color: #24509c">
    Список производителей</h1>
  <div id="wrapper">
    <AdminMenuComponent/>
    <div style="display: table">
      <div style="vertical-align: middle; width: 75vw; text-align: center">
        <div class="form-group" style="display: inline-block">
          <input class="form-control" placeholder="Наименование" type="text" v-model="name_of_company"/>
        </div>
        <div class="form-group" style="display: inline-block; margin-left: 20px">
          <input class="form-control" placeholder="ИНН" type="text" v-model="TIN_of_company"/>
        </div>
        <div class="form-group" style="display: inline-block; margin-left: 20px">
          <input class="form-control" placeholder="Описание" type="text" v-model="about_company"/>
        </div>
        <button class="btn btn-danger"
                style="height: 100%; width: 100px; background-color: green; border: 0; margin-bottom: 3px; margin-left: 20px"
                @click="update_users(this.current_page)">
          Поиск
        </button>
      </div>

      <table>
        <tr>
          <th style="padding-left: 10px">ID</th>
          <th>Компания</th>
          <th>ИНН</th>
          <th>Описание</th>
          <th></th>
          <th></th>
        </tr>
        <tr v-for="index in Object.keys(users)" v-bind:key="index" style="width: 100%;">
          <td> {{ users[index]["_id"] }}</td>
          <td> {{ users[index]["name"] }}</td>
          <td> {{ users[index]["TIN"] }}</td>
          <td> {{ users[index]["about"] }}</td>
          <td>
            <a :href="'/admin/companies/' + users[index]['_id']" style="color: black">
              Редактировать
            </a>
          </td>
        </tr>
      </table>
      <br>
      <div v-for="page in Math.ceil(users_count/current_limit)" v-bind:key="page" style="display: inline-block;">
        <a @click="update_users(page)" :class="{ page_button: true, active: page===current_page}">{{ page }} </a>
      </div>
    </div>
  </div>
  <FooterComponent/>
</template>

<script>
import {defineComponent} from "vue";
import AdminMenuComponent from "@/admin/AdminMenuComponent";
import HeaderComponent from "@/company/HeaderComponent";
import FooterComponent from "@/FooterComponent";
import axios from "axios";

export default defineComponent({
  name: 'CompaniesPage',
  components: {HeaderComponent, FooterComponent, AdminMenuComponent},

  data() {
    return {
      users: [],
      users_count: 0,
      current_page: 1,
      current_limit: 60,
      name_of_company: '',
      TIN_of_company: '',
      about_company: '',
    }
  },

  methods: {
    get_users: function () {
      axios.post("/api/admin/companies", {
            "page": this.current_page,
            "limit": this.current_limit,
            "find_options": {
              "name": {$regex: `${this.name_of_company}`, $options: 'i'},
              "TIN": {$regex: `${this.TIN_of_company}`, $options: 'i'},
              "about": {$regex: `${this.about_company}`, $options: 'i'}
            },
          }, {
            headers: {}
          }
      ).then((response) => {
        console.log(response.data)
        this.users = response.data["users"];
        this.users_count = response.data["users_count"];
      })
    },

    update_users(page) {
      this.current_page = page;
      this.get_users()
    }
  },

  mounted() {
    this.get_users()
  }
})
</script>

<style scoped>
#wrapper {
  font-family: Ubuntu;
  display: flex;
  margin-left: 4vw;
  min-height: 70vh;
}

table {
  width: 75vw;
  text-align: center;
}

td {
  border: 1px solid #c4c4c4;
}

table th {
  background: #333333;
  color: white;
  padding-top: 10px;
  padding-bottom: 10px;
}

.active {
  text-decoration: underline;
  text-decoration-color: black;
  text-decoration-thickness: 2px;
}

.page_button {
  color: black;
  padding-right: 5px;
}
</style>