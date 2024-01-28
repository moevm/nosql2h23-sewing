<template>
  <HeaderComponent/>
  <h1 class="display-1"
      style="text-align: center; font-size: 46px; font-family: Ubuntu; padding-top: 10px; color: #24509c">
    Новые регистрации</h1>

  <div id="wrapper">
    <AdminMenuComponent/>
    <div id="applications">
      <h3>
        Заказчики
      </h3>
      <table>
        <tr>
          <th style="padding-left: 10px">ID</th>
          <th>Дата регистрации</th>
          <th>ФИО/Должность</th>
          <th>Телефон</th>
          <th>Компания</th>
          <th>ИНН</th>
          <th>Email</th>
          <th></th>
          <th></th>
        </tr>
        <tr v-for="index in Object.keys(customers)" v-bind:key="index" style="width: 100%;">
          <td> {{ customers[index]["_id"] }}</td>
          <td> {{ new Date(customers[index]["created_at"]).toLocaleString() }}</td>
          <td> {{ customers[index]["contact_person"] }}</td>
          <td> {{ customers[index]["phone"] }}</td>
          <td> {{ customers[index]["name"] }}</td>
          <td> {{ customers[index]["TIN"] }}</td>
          <td> {{ customers[index]["email"] }}</td>
          <td>
            <button class="btn btn-danger" style="height: 2.5vw; width: 100px; background-color: green; border: 0"
            @click="approve(customers[index]['_id'], 'customer')">
              Принять
            </button>
          </td>
          <td>
            <button class="btn btn-danger" style="height: 2.5vw; width: 100px; background-color: red; border: 0"
                    @click="decline(customers[index]['_id'], 'customer')">
              Отклонить
            </button>
          </td>
        </tr>
      </table>

      <h3>
        Производители
      </h3>
      <table>
        <tr style="width: 2000px">
          <th style="padding-left: 10px">ID</th>
          <th>Дата и время</th>
          <th>ФИО/Должность</th>
          <th>Телефон</th>
          <th>Компания</th>
          <th>ИНН</th>
          <th>Email</th>
          <th></th>
          <th></th>
        </tr>
        <tr v-for="index in Object.keys(companies)" v-bind:key="index" style="width: 100%;">
          <td> {{ companies[index]["_id"] }}</td>
          <td> {{ new Date(companies[index]["created_at"]).toLocaleString() }}</td>
          <td> {{ companies[index]["contact_person"] }}</td>
          <td> {{ companies[index]["phone"] }}</td>
          <td> {{ companies[index]["name"] }}</td>
          <td> {{ companies[index]["TIN"] }}</td>
          <td> {{ companies[index]["email"] }}</td>
          <td>
            <button class="btn btn-danger" style="height: 2.5vw; width: 100px; background-color: green; border: 0"
                    @click="approve(companies[index]['_id'], 'company')">
              Принять
            </button>
          </td>
          <td>
            <button class="btn btn-danger" style="height: 2.5vw; width: 100px; background-color: red; border: 0"
                    @click="decline(companies[index]['_id'], 'company')">
              Отклонить
            </button>
          </td>
        </tr>
      </table>
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
  name: 'App',
  components: {HeaderComponent, FooterComponent, AdminMenuComponent},

  data() {
    return {
      customers: [],
      companies: [],
    }
  },

  methods: {
    get_users() {
      axios.get("/api/admin/registration_applications", {
        headers: {
          "Content-Type": "application/json",
        }
      }).then((response) => {
        this.customers = response.data["customers"];
        this.companies = response.data["companies"];
      })
    },

    approve(user_id, user_type) {
      if (user_type === "customer") {
        for (let i in this.customers) {
          if (this.customers[i]["_id"] === user_id) {
            delete this.customers[i];
          }
        }
      } else if (user_type === "company") {
        for (let i in this.companies) {
          if (this.companies[i]["_id"] === user_id) {
            delete this.companies[i];
          }
        }
      }

      axios.post("/api/admin/approve_application", {
            "id": String(user_id),
            "type": user_type,
          }, {
            headers: {
              'Accept':
                  'application/json',
              'Content-Type':
                  'application/json'
            }
          }
      )
    },

    decline(user_id, user_type) {
      if (user_type === "customer") {
        for (let i in this.customers) {
          if (this.customers[i]["_id"] === user_id) {
            delete this.customers[i];
          }
        }
      } else if (user_type === "company") {
        for (let i in this.companies) {
          if (this.companies[i]["_id"] === user_id) {
            delete this.companies[i];
          }
        }
      }

      axios.post("/api/admin/decline_application", {
            "id": String(user_id),
            "type": user_type,
          }, {
            headers: {
              'Accept':
                  'application/json',
              'Content-Type':
                  'application/json'
            }
          }
      )
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
  /*width: 2000px;*/
  min-height: 70vh;
}

table {
  width: 80vw;
  font-size: 12px;
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

#applications {
  display: inline-block;
}

</style>