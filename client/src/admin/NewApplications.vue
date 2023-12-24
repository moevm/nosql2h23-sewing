<template>
  <HeaderComponent/>
  <h1 class="display-1"
      style="text-align: center; font-size: 46px; font-family: Ubuntu; padding-top: 10px; color: #24509c">
    Новые регистрации</h1>

  <div id="wrapper" style="">
    <AdminMenuComponent/>
    <div>
      <table>
        <tr>
          <th>№</th>
          <th>Дата и время</th>
          <th>ФИО/Должность</th>
          <th>Телефон</th>
          <th>Компания</th>
          <th>ИНН</th>
          <th>Email</th>
          <th></th>
          <th></th>
        </tr>
        <tr>
          <td>1</td>
          <td>02:23 15.09.2002</td>
          <td>Иванов Иван Иванович</td>
          <td>89005312196</td>
          <td>Компания</td>
          <td>7802701660</td>
          <td>tv.kozlov.2002@gmail.com</td>
          <td>
            <button class="btn btn-danger" style="height: 2.5vw; width: 100px; background-color: green; border: 0px">
              Принять
            </button>
          </td>
          <td>
            <button class="btn btn-danger" style="height: 2.5vw; width: 100px; background-color: red; border: 0px">
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
import HeaderComponent from "@/HeaderComponent";
import FooterComponent from "@/FooterComponent";

export default defineComponent({
  name: 'App',
  components: {HeaderComponent, FooterComponent, AdminMenuComponent},
})
</script>

<style scoped>
td {
  padding-right: 15px;
  padding-left: 15px;
  border: 1px solid #c4c4c4;
}
table th {
  background: #333333;
  color: white;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 15px;
}
</style>