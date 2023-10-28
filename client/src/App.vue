<template>
  <header>
    <div class="logo">
      <a href="/">
        <img src="@/asserts/logo.png" width="170" height="60px" />
      </a>
    </div>
    <div class="menu">
      <ul>
        <li><a href="/about_company">О компании</a></li>
        <li><a href="/catalog">Каталог</a></li>
        <li><a href="/constructor">Конструктор спецодежды</a></li>
        <li><a href="/works">Этапы работы</a></li>
        <li><a href="/production">Производство</a></li>
        <li><a href="/clients">Клиенты</a></li>
        <li><a href="/faq">FAQ</a></li>
      </ul>
    </div>
    <div class="tel">
      <a href="tel:88126605141">8 (812) 660 51 41</a>
    </div>
    <div class="tel">
    </div>
  </header>
    <div id="viewer">
      <vue3dLoader
          :height="500"
          :width="500"
          :showFps="false"
          :filePath="'http://localhost:8081/static/mers.obj'"
          :backgroundColor="0x000000"
      ></vue3dLoader>
    </div>
  <div id="table">
    <ag-grid-vue
        style="width: 300px; height: 300px;"
        class="ag-theme-alpine"
        :columnDefs="columnDefs"
        :rowSelection="rowSelection"
        :rowData="rowData"
        @select="onSelectionChanged"
        @selection-changed="onSelectionChanged"
    >
    </ag-grid-vue>
  </div>
</template>

<script>

import {AgGridVue} from "ag-grid-vue3";
import {vue3dLoader} from "vue-3d-loader";
import {ref} from "vue";

export default {
  name: 'App',

  components: {
    'ag-grid-vue': AgGridVue,
    "vue3dLoader": vue3dLoader,
  },

  data() {
    const rowSelection = ref(null);
    const onSelectionChanged = () => {
      // const selectedRows = gridApi.value.getSelectedRows();
      console.log("!!!")
    };
    return {
      onSelectionChanged,
      rowSelection,
      columnDefs: [
        {headerName: "Model", field: "model"},
      ],
      rowData: [
        {model: "mers"},
        {model: "ferra"},
        {model: "!!!"},
      ],
    };
  }
}
</script>

<style>
#viewer {
  position: absolute;
  top: 150px;
  left: 750px;
}
#table {
  position: absolute;
  top: 700px;
  left: 880px;
}
header {
  display: flex;
  flex-flow: row nowrap;
  justify-content: flex-start;
  align-items: center;
  text-align: center;
}
.menu {
  flex-grow: 1;
}
.menu ul {
  display: flex;
  flex-flow: row nowrap;
  margin: 0;
  padding: 0;
  font-size: 16px;
  line-height: 18px;
  list-style: none;
}
.menu li {
  margin-right: 20px;
}
.menu li:last-child {
  margin-right: 0;
}
.menu a {
  padding: 8px 10px;
}
.menu a,
.menu .active {
  display: block;
  padding: 8px 10px;
}
.menu a {
  color: #000;
  text-decoration: none;
}
</style>
