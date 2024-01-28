<template>
  <footer>
    <div class="container">
      <div class="d-flex w-100">
        <div class="">
          <table>
            <tr>
              <img src="@/assets/white_logo.png" id="white-icon">
            </tr>
            <tr>
              <p style="font-size: 16px; color: #2e508c;">ООО "ЛенСИЗ", 2022.
              <br>Все права защищены</p>
            </tr>
            <tr>
              <button class="btn btn-danger" style="height: 1.8vw; width: 11vw; background-color: #cb292f; padding-top: 2px; font-size: 13px">
                В Интернет-магазин
              </button>
            </tr>
          </table>
        </div>
        <div style="font-size: 20px; margin-top: 10px; margin-left: 4vw;">
          Навигация по сайту
          <div>
            <table class="navigation">
              <tr><td style="padding-right: 50px"><a>О компании</a></td><td><a>Наши клиенты</a></td></tr>
              <tr><td style="padding-right: 50px"><a>Продукция</a></td><td><a>Отзывы</a></td></tr>
              <tr><td style="padding-right: 50px"><a>Этапы работы</a></td><td><a>Вопросы и ответы</a></td></tr>
              <tr><td style="padding-right: 50px"><a>Производство</a></td><td><a>Интернет магазин</a></td></tr>
            </table>
          </div>
        </div>
        <div class="ms-auto" style="display: flex;">
          <div>
            <div id="contacts">
              <table>
                <tbody>
                <tr>
                  <td>
                    <img src="@/assets/location_icon.png" id="info-logo">
                  </td>
                  <td>
                    <a style="text-align: left" href="https://yandex.ru/maps/-/CDaOzIPM">
                      г. Санкт-Петербург, п. Парголово, ул. Заречная, д. 41, стр.1
                    </a>
                  </td>
                </tr>
                <tr>
                  <td>
                    <img src="@/assets/phone_icon.png" id="info-logo">
                  </td>
                  <td>
                    <a style="text-align: left">
                      8 (812) 660 51 41
                      <br> 8 (911) 849 37 70
                    </a>
                  </td>
                </tr>
                <tr>
                  <td>
                    <img src="@/assets/email_icon.png" id="info-logo">
                  </td>
                  <td>
                    <a style="text-align: left">
                      info@lensiz.ru
                    </a>
                  </td>
                </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "FooterComponent"
}
</script>

<style>
footer {
  bottom: 0;
  background: #062051;
  color: #fafaff;
  padding-top: 20px;
  padding-bottom: 20px;
  margin-top: 20px;
  font-family: Ubuntu;
}

a:link {
  color: white;
  text-decoration: none;
}

a:visited {
  color: white;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

#contacts {
  font-size: 16px;
}

table {
  border-collapse: separate;
  border-spacing: 0 10px
}

#info-logo {
  width: 20px;
}

#white-icon {
  width: 150px;
  padding-bottom: 30px;
}

.navigation {
  font-size: 16px;
  color: #2e508c;
}

table.navigation td {
  padding-left: 0;
  text-align: left;
}
</style>