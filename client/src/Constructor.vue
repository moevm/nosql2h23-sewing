<template>
  <header style="font-family: Ubuntu;">
    <img src="@/assets/logo.png" id="logo"/>
    <div class="header_core">
      <a href="/constructor" class="header_link">Конструктор</a>
      <a href="/projects" class="header_link">Мои проекты</a>
      <a href="/orders" class="header_link">Мои заказы</a>
      <a href="/chat" class="header_link">Чат с производителем</a>
      <a href="/faq" class="header_link">FAQ</a>
    </div>
    <div style="display: table; float: right; padding-right: 5vw">
      <div style="display: table-cell;">
        <a style="display: table-row">
          Phone number 1
        </a>
        <a style="display: table-row">
          Phone number 2
        </a>
        <a style="display: table-row">
          info@lensiz.ru
        </a>
      </div>
      <div style="display: table-cell; padding-left: 1vw; text-align: center; vertical-align: middle">
        <button class="btn btn-danger" style="height: 2.5vw; background-color: #cb292f">
          Заказать звонок
        </button>
      </div>
    </div>
  </header>

  <hr style="width: 92vw; margin-left: 4vw; margin-top: 0vw">
  <h1 class="display-1" style="text-align: center; font-size: 46px; font-family: Ubuntu; color: #24509c">
    Конструктор спецодежды</h1>
  <br>
  <div id="wrapper" style="font-family: Ubuntu">
    <div id="menu">
      <ul class="list-group list-group-flush">
        <li class="menu_button list-group-item" style="border-radius: 10px">
          <a href="/constructor" class="menu_text">Конструктор</a></li>
        <li class="menu_button list-group-item">
          <a href="/projects" class="menu_text">Мои проекты</a></li>
        <li class="menu_button list-group-item">
          <a href="/orders" class="menu_text">Мои заказы</a></li>
        <li class="menu_button list-group-item">
          <a href="/chat" class="menu_text">Чат с производителем</a></li>
        <li class="menu_button list-group-item">
          <a href="/offer" class="menu_text">Оферта</a></li>
        <li class="menu_button list-group-item">
          <a href="/instruction_text" class="menu_text">Инструкция (текстовая)</a></li>
        <li class="menu_button list-group-item">
          <a href="/instruction_video" class="menu_text">Видео-инструкция</a></li>
        <li class="menu_button list-group-item">
          <a href="/edit" class="menu_text">Управление профилем</a></li>
        <li class="menu_button list-group-item" style="border-radius: 10px">
          <a href="/faq" class="menu_text">FAQ</a></li>
      </ul>
    </div>
    <div id="viewer" @mousemove="mouseMove" @mousedown.left="mouseDownLeft" @mouseup.left="mouseUpLeft"
         @mousewheel='mouseWheel' oncontextmenu="return false;"
         @mousedown.right="mouseDownRight" @mouseup.right="mouseUpRight">
    </div>
    <div id="select">
      <div style="padding-bottom: 10px; text-align: center">
        <select v-model="selected" @change="load_model($event)" class="select form-select"
                style="display: inline-block; width: 75%">
          <option v-for="option in options" :value="option.value" :key="option.value">
            {{ option.text }}
          </option>
        </select>
      </div>

      <hr>

      <ul class="row-container" style="margin-left: 0; padding-left: 0">
        <li v-for="index in Object.keys(elements)" v-bind:key="index"
            style="list-style-type: none; padding-bottom: 10px">
          <color-picker style="width: 10%" v-model:pureColor="elements_color[index]"
                        @pureColorChange="change_color($event, index)"
                        :disableAlpha="true" class="inline-element"/>
          <n-tree-select style="width: 70%" :options="tree_options"
                         @update:value="value => handleUpdateValue(value, index)" check-strategy="child"
                         class="inline-element"/>
          <CCloseButton style="width: 10%" @click="deleteRow(index)" class="inline-element"/>
        </li>
      </ul>

      <button @click="addRow" class="btn btn-primary small" id="add_button">
        <svg width="33px" height="33px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M4 12H20M12 4V20" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>

      <hr>
      <button class="btn btn-primary small"
              style="width: 70%; margin-left: 15%; color: #f3dfdf; background-color: #0353b2;">
        Сохранить макет
      </button>
    </div>
  </div>
  <div id="footer">
    © Компания ООО "ЛенСИЗ", 2019.
  </div>
</template>

<script>

import {CCloseButton} from '@coreui/vue'
import * as Three from 'three';
import {reactive, defineComponent} from 'vue';
import {GLTFLoader} from "three/addons/loaders/GLTFLoader";
import {ColorPicker} from "vue3-colorpicker";
import "vue3-colorpicker/style.css";

export default defineComponent({
  name: 'App',
  components: {ColorPicker, CCloseButton},

  data() {
    return {
      last_element_id: 0,
      elements: {},
      elements_to_models: {},
      elements_color: {},
      selected: 'Human/Man',
      options: [
        {text: 'Мужчина', value: 'Human/Man'},
      ],
      tree_options: [
        {
          label: "Куртки",
          key: "jackets",
          children: [
            {
              label:
                  "Куртка 1",
              key: "Jacket/Jac_Main",
            },
            {
              label:
                  "Карманы",
              key: "Pockets",
              children: [
                {
                  label:
                      "Карман левый 1",
                  key: "Jacket/Jac_Pocket_LEFT_V1",
                },
                {
                  label:
                      "Карман левый 2",
                  key: "Jacket/Jac_Pocket_LEFT_V2",
                },
                {
                  label:
                      "Карман правый 1",
                  key: "Jacket/Jac_Pocket_RIGHT_V1",
                },
                {
                  label:
                      "Карман правый 2",
                  key: "Jacket/Jac_Pocket_RIGHT_V2",
                },
              ],
            },
            {
              label:
                  "Flic",
              key: "Flics",
              children: [
                {
                  label:
                      "Jac_Flic_BEHIND_V1",
                  key: "Jacket/Jac_Flic_BEHIND_V1",
                },
                {
                  label:
                      "Jac_Flic_BEHIND_V2",
                  key: "Jacket/Jac_Flic_BEHIND_V2",
                },
                {
                  label:
                      "Jac_Flic_BOTTOM_BACK",
                  key: "Jacket/Jac_Flic_BOTTOM_BACK",
                },
                {
                  label:
                      "Jac_Flic_BOTTOM_FACE",
                  key: "Jacket/Jac_Flic_BOTTOM_FACE",
                },
              ],
            },
          ],
        },
        {
          label: "Штаны",
          key: "pants",
          children: [
            {
              label:
                  "Штаны 1",
              key: "Pants/Pants_Main",
            },
            {
              label:
                  "Карманы",
              key: "Pockets",
              children: [
                {
                  label: "Декоративные",
                  key: "Decorative pockets",
                  children: [
                    {
                      label:
                          "Левый 1",
                      key: "Pants/Pants_Decor_Pocket_Left_V1",
                    },
                    {
                      label:
                          "Левый 2",
                      key: "Pants/Pants_Decor_Pocket_Left_V2",
                    },
                    {
                      label:
                          "Правый 1",
                      key: "Pants/Pants_Decor_Pocket_Right_V1",
                    },
                    {
                      label:
                          "Правый 2",
                      key: "Pants/Pants_Decor_Pocket_Right_V2",
                    },
                  ],
                },
                {
                  label: "Обычные",
                  key: "Pockets_Full",
                  children: [
                    {
                      label:
                          "Левый 1",
                      key: "Pants/Pants_Pocket_Left_V1",
                    },
                    {
                      label:
                          "Левый 2",
                      key: "Pants/Pants_Pocket_Left_V2",
                    },
                    {
                      label:
                          "Правый 1",
                      key: "Pants/Pants_Pocket_Right_V1",
                    },
                    {
                      label:
                          "Правый 2",
                      key: "Pants/Pants_Pocket_Right_V2",
                    },
                  ],
                },
              ],
            },
          ],
        },
      ],
    }
  },
  methods: {
    init: function () {
      this.rotation_angle = 0

      this.color = reactive({
        alpha: 1,
      });

      this.loader = new GLTFLoader();
      this.scene = new Three.Scene();

      this.models = [];

      this.lastMPos = {
        x: 0,
        y: 0
      };
      this.mouseClickedLeft = false;
      this.mouseClickedRight = false;

      let container = document.getElementById('viewer');

      this.camera = new Three.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.01, 100);
      this.camera.position.y = 1.0;
      this.camera.position.z = 2.5;
      this.camera.lookAt(0, 0.7, -1)

      const color = 0xFFFFFF;
      const intensity = 2.5;

      const light = new Three.AmbientLight(color, 0.5);
      this.scene.add(light);


      const light1 = new Three.DirectionalLight(color, intensity);
      light1.castShadow = true;
      light1.position.set(1, 5, 5);
      light1.target.position.set(-2, 0, -1);
      light1.shadow.mapSize.width = 4096;
      light1.shadow.mapSize.height = 4096;
      this.scene.add(light1);
      this.scene.add(light1.target);

      const light2 = new Three.DirectionalLight(color, 1);
      light2.castShadow = true;
      light2.position.set(-6, 3, 5);
      light2.target.position.set(-2, 0, -1);
      light2.shadow.mapSize.width = 4096;
      light2.shadow.mapSize.height = 4096;
      this.scene.add(light2);
      this.scene.add(light2.target);

      const loadManager = new Three.LoadingManager();
      const loader = new Three.TextureLoader(loadManager);
      const lensiz_texture = loader.load("lensiz_logo.jpg");

      let width = 8;

      const logoGeo = new Three.PlaneGeometry(width, width / 2.4);
      const logoMat = new Three.MeshPhongMaterial({map: lensiz_texture});

      const logo = new Three.Mesh(logoGeo, logoMat);
      logo.receiveShadow = true;
      logo.position.x = 0;
      logo.position.y = 1.1;
      logo.position.z = -1.99;
      this.scene.add(logo);

      const planeGeo = new Three.PlaneGeometry(40, 40);
      const planeMat = new Three.MeshPhongMaterial({color: 0xFFFFFF});
      const mesh1 = new Three.Mesh(planeGeo, planeMat);
      mesh1.receiveShadow = true;
      mesh1.rotation.x = Math.PI * -.5;
      mesh1.position.y = -1;
      this.scene.add(mesh1);

      const mesh2 = new Three.Mesh(planeGeo, planeMat);
      mesh2.receiveShadow = true;
      mesh2.position.z = -2;
      this.scene.add(mesh2);

      this.renderer = new Three.WebGLRenderer({antialias: true});
      this.renderer.shadowMap.enabled = true;
      this.renderer.setClearColor(0xaaaaaa, 1);
      this.renderer.setSize(container.clientWidth, container.clientHeight);

      container.appendChild(this.renderer.domElement);
    },

    handleUpdateValue(value, option) {
      this.scene.remove(this.models[this.elements_to_models[option]]);
      delete this.elements[option];
      this.elements[option] = value;

      let color = this.elements_color[option]
      this.load_model(value, color);
      this.elements_to_models[option] = this.models.length;
    },

    addRow() {
      this.elements[this.last_element_id] = -1;
      this.elements_color[this.last_element_id] = {r: 215, g: 215, b: 215};
      this.last_element_id += 1;
    },
    deleteRow(index) {
      this.scene.remove(this.models[this.elements_to_models[index]]);
      delete this.elements[index];
    },

    animate: function () {
      requestAnimationFrame(this.animate);
      this.renderer.render(this.scene, this.camera);
    },

    load_model: function (model, color) {
      if (typeof (model) != "string") {
        model = model.target.value;
      }

      this.loader.load(`models/${model}.glb`, (gltf) => {
        gltf.scene.position.y = -1;
        gltf.scene.position.z = -0.8;
        gltf.scene.rotation.y = this.rotation_angle;
        gltf.scene.traverse(function (model) {
          if (model.isMesh) {
            model.castShadow = true;
            model.material.color = new Three.Color(color);
          }
        });
        this.models.push(gltf.scene);
        this.scene.add(gltf.scene);
      }, undefined, function (error) {
        console.error(error);
      });
    },

    change_color(value, index) {
      this.models[this.elements_to_models[index]].traverse(function (model) {
        if (model.isMesh) {
          model.material.color = new Three.Color(value);
        }
      })
    },

    mouseDownLeft() {
      this.mouseClickedLeft = true;
    },
    mouseUpLeft() {
      this.mouseClickedLeft = false;
    },
    mouseDownRight() {
      this.mouseClickedRight = true;
    },
    mouseUpRight() {
      this.mouseClickedRight = false;
    },
    mouseWheel(event) {
      this.camera.position.z = Math.max(this.camera.position.z + event.deltaY / 100, 0.5)
    },
    mouseMove(event) {
      if (this.mouseClickedLeft) {
        for (let i = 0; i < this.models.length; i++) {
          this.models[i].rotation.y -= (this.lastMPos.x - event.clientX) * .005;
          this.rotation_angle = this.models[i].rotation.y
        }
      }
      if (this.mouseClickedRight) {
        this.camera.position.y -= (this.lastMPos.y - event.clientY) * 0.001;
        this.camera.position.x += (this.lastMPos.x - event.clientX) * 0.002;
      }

      this.lastMPos = {
        x: event.clientX,
        y: event.clientY
      };
    }
  },
  mounted() {
    this.init();
    this.animate();
    this.load_model(this.selected);
    // this.load_model("Jacket/Jac_Main");
    // this.load_model("Pants/Pants_Main");
  }
})
</script>

<style>
@font-face {
  font-family: Verdana;
  src: url('~@/assets/fonts/Verdana.ttf');
}

@font-face {
  font-family: Ubuntu;
  src: url('~@/assets/fonts/Ubuntu.ttf');
}

#menu {
  display: table-cell;
  float: left;
  width: 20%;
  border-radius: 10px;
  padding-right: 5%;
}

#viewer {
  display: table-cell;
  width: 70vw;
  height: 60vh;
  text-align: center;
}

#select {
  right: 0;
  top: 0;
  display: table-cell;
  vertical-align: middle;
  width: 30%;
  padding-left: 5%;
  margin-left: auto;
  margin-right: 0;
}

.menu_text:hover {
  text-decoration: underline;
}

.menu_button {
  margin-bottom: 0.2vh;
  border-radius: 10px;
  background-color: #0353b2;
}

.menu_text {
  text-decoration: none;
  color: #f3dfdf;
}

#logo {
  display: inline;
  vertical-align: middle;
  margin-right: 5vw;
  width: 15vw;
  padding-left: 5vw;
}

#wrapper {
  margin-left: 5vw;
  width: 90vw;
  height: 70vh;
}


#footer {
  background-color: #062051;
  position: fixed;
  right: 0;
  bottom: 0;
  text-align: center;
  width: 100%;
  font-size: 19px;
  color: #fafaff;
}

#add_button {
  width: 35px;
  height: 35px;
  margin-left: 42%;
  padding: 0;
  text-align: center;
  background-color: #1ea83a
}

#add_button:hover {
  background-color: #96ff40;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 2vh;
  margin-bottom: 2vh;
}

.header_core {

}

.header_link {
  font-size: 1vw;
  padding-left: 2vw;
  color: black;
  text-decoration: none;
}

.header_link:hover {
  text-decoration: underline;
}


.row-container {
  white-space: nowrap;
}

.inline-element {
  display: inline-block;
  margin-right: 10px;
  vertical-align: middle;
  height: 100%;
}

</style>
