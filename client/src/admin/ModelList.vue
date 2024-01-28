<template>
  <HeaderComponent/>
  <h1 class="display-1"
      style="text-align: center; font-size: 46px; font-family: Ubuntu; padding-top: 10px; color: #24509c">
    Список моделей</h1>
  <div id="wrapper">
    <AdminMenuComponent/>
    <div>
      <button style="border-radius: 10px">
        <a href="/admin/load_model" style="color: black; font-size: 20px">Загрузить модель</a>
      </button>

      <div style="vertical-align: middle; width: 75vw; text-align: center">
        <div class="form-group" style="display: inline-block">
          <input class="form-control" placeholder="Путь" type="text" v-model="path_of_model"/>
        </div>
        <div class="form-group" style="display: inline-block; margin-left: 20px">
          <input class="form-control" placeholder="Тип" type="text" v-model="type_of_model"/>
        </div>
      </div>

      <table>
        <tr style="text-align: center">
          <th>id</th>
          <th>Название</th>
          <th>Название в ФС</th>
          <th>Путь</th>
          <th>Тип</th>
          <th>Статус</th>
          <th></th>
          <th></th>
        </tr>
        <tr v-for="index in Object.keys(models.filter((model) =>
        (model['path_to_model'].toLowerCase().indexOf(path_of_model.toLowerCase()) >= 0) &&
        (model['type'].toLowerCase().indexOf(type_of_model.toLowerCase()) >= 0)))"
            v-bind:key="index" style="width: 100%;">
          <td> {{ models[index]["_id"] }}</td>
          <td> {{ models[index]["name"] }}</td>
          <td> {{ models[index]["model"] }}</td>
          <td> {{ models[index]["path_to_model"] }}</td>
          <td> {{ models[index]["type"] }}</td>
          <td> {{ models[index]["status"] }}</td>
          <td>
            <a :href="'/admin/models/' + models[index]['_id']" style="color: black">
              Редактировать
            </a>
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
  name: 'ModelList',
  components: {HeaderComponent, FooterComponent, AdminMenuComponent},

  data() {
    return {
      models: [],

      type_of_model: '',
      path_of_model: '',
    }
  },

  methods: {
    get_models() {
      axios.get("/api/admin/models", {
        headers: {
          "Content-Type": "application/json",
        }
      }).then((response) => {
        this.models = response.data;
      })
    }
  },

  mounted() {
    this.get_models()
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