<template>
  <HeaderComponent/>
  <h1 class="display-1"
      style="text-align: center; font-size: 46px; font-family: Ubuntu; padding-top: 10px; color: #24509c">
    Редактирование модели
  </h1>
  <div id="wrapper">
    <AdminMenuComponent/>
    <div class="form-check-inline">
      <form>
        <div class="form-group">
          <label for="login"><b>Загрузка модели</b></label>
          <input class="form-control" placeholder="Выберите файл с моделью" type="file" ref="fileInput" disabled
                 @change="handleFileChange"/>
        </div>

        <div class="form-group">
          <label><b>Путь к модели на сервере</b></label>
          <input class="form-control" placeholder="Введите путь к модели" type="text" disabled
                 :value="this.model['path_to_model']"/>
        </div>

        <div class="form-group">
          <label><b>Имя модели у пользователя</b></label>
          <input class="form-control" placeholder="Введите путь к модели" type="text" v-model="this.model['name']"/>
        </div>

        <div class="form-group">
          <label><b>Тип модели</b></label>
          <input class="form-control" placeholder="Введите путь к модели" type="text" v-model="this.model['type']"/>
        </div>

        <div class="form-group">
          <label><b>Описание</b></label>
          <input class="form-control" placeholder="Введите путь к модели" type="text"
                 v-model="this.model['description']"/>
        </div>

        <div class="form-group">
          <label><b>ID моделей, с которыми конфликтует</b></label>
          <input class="form-control" placeholder="Введите ID конфликтующих моделей" type="text"
                 v-model="this.model['conflicts_to']"/>
        </div>

        <div class="form-group">
          <label><b>Статус модели</b></label>
          <input class="form-control" placeholder="Введите статус к модели" type="number" v-model="this.model['status']"/>
        </div>

        <div class="form-group">
          <label><b>Количество цветов модели</b></label>
          <select class="form-select" name="color_count" v-model="this.model['color_count']">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
          </select>
        </div>

        <button class="btn btn-success" @click.prevent="updateModel" style="margin-top: 10px; background-color: green">
          Изменить модель
        </button>
      </form>
      <p>Статус : {{ message }}</p>
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
          model: {},
          message: ''
        }
      },

      methods: {
        updateModel() {
          this.model["model_id"] = this.model["_id"]
          this.model["conflicts_to"] = String(this.model["conflicts_to"])
          this.model['color_count'] = parseInt(this.model['color_count'])

          console.log(this.model)

          axios.post("/api/admin/update_model", this.model, {
            headers: {
              "Content-Type": "application/json",
            },
          })
              .then((response) => {
                if (response.data === 200) {
                  this.message = "модель успешно обновлена"
                } else {
                  this.message = "произошла ошибка"
                }
              })
              .catch((error) => {
                console.error("Error uploading file:", error);
              });
        },
      get_models() {
        axios.get("/api/admin/model/" + this.$route.params["id"], {
          headers: {
            "Content-Type": "application/json",
          }
        }).then((response) => {
          this.model = response.data;
        })
      }
    },

    mounted()
{
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