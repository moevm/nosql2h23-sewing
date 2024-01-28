<template>
  <HeaderComponent/>
  <div>
    <h1 class="display-1" id="constructor_sign">
      Конструктор спецодежды</h1>
    <br>
    <div id="wrapper" style="font-family: Ubuntu,serif">
      <MenuComponent/>
      <div id="middle_block">
        <div id="viewer" @mousemove="mouseMove" @mousedown.left="mouseDownLeft" @mouseup.left="mouseUpLeft"
             @mousewheel='mouseWheel' oncontextmenu="return false;"
             @mousedown.right="mouseDownRight" @mouseup.right="mouseUpRight"
             @mouseenter="hover = true" @mouseleave="hover = false">
        </div>
        <div id="description">
          <li v-for="index in Object.keys(elements)" v-bind:key="index"
              style="list-style-type: none; padding-bottom: 10px">
            <div v-if="models_properties[this.work + '/' + this.season + '/' + this.sex + '/' + elements[index]]">
              <p style="font-size: 20px">
                {{
                  models_properties[this.work + '/' + this.season + '/' + this.sex + '/' + elements[index]]['model_name']
                }}
              </p>
              <p>
                {{
                  models_properties[this.work + '/' + this.season + '/' + this.sex + '/' + elements[index]]['description']
                }}
              </p>
            </div>
          </li>
          <br>
        </div>
      </div>

      <div id="select">
        <div style="padding-bottom: 10px; text-align: center">
          <select v-model="work_selected" @change="work_change($event)" class="select form-select"
                  style="display: inline-block; width: 75%; margin-bottom: 10px">
            <option v-for="option in work_options" :value="option.value" :key="option.value">
              {{ option.text }}
            </option>
          </select>

          <select v-model="season_selected" @change="season_change($event)" class="select form-select"
                  style="display: inline-block; width: 75%; margin-bottom: 10px">
            <option v-for="option in season_options" :value="option.value" :key="option.value">
              {{ option.text }}
            </option>
          </select>

          <select v-model="sex_selected" @change="sex_change($event)" class="select form-select"
                  style="display: inline-block; width: 75%; margin-bottom: 10px">
            <option v-for="option in sex_options" :value="option.value" :key="option.value">
              {{ option.text }}
            </option>
          </select>
        </div>
        <div style="padding-bottom: 10px; text-align: center">
          Начальный цвет:
          <color-picker style="width: 10%" v-model:pureColor="start_color"
                        @pureColorChange="changeStartColor($event)"
                        :disableAlpha="true" class="inline-element"/>
        </div>

        <div style="padding-bottom: 10px; text-align: center">
          Цвет ниток:
          <color-picker style="width: 10%" v-model:pureColor="ropes_color"
                        @pureColorChange="changeRopesColor($event)"
                        :disableAlpha="true" class="inline-element"/>
        </div>

        <hr style="margin-left: 30px">
        <ul class="row-container" style="margin-left: 0; padding-left: 0">
          <n-collapse>
            <n-collapse-item v-for="model_type in Object.keys(this.current_types)"
                             v-bind:key="model_type" :title="model_type" :name="model_type">
              <li v-for="index in Object.keys(elements).filter((object) => (this.models_properties[this.work + '/' + this.season + '/' + this.sex + '/' + elements[object]] && this.models_properties[this.work + '/' + this.season + '/' + this.sex + '/' + elements[object]]['type'].includes(model_type)) || elements[object] === -1)" v-bind:key="index" class="row_in_select"
                  style="list-style-type: none; padding-bottom: 10px" draggable="true">
                <button style="background: transparent; border: none !important; margin-top: 5px"  :disabled="elements[index] === -1"
                        @click="hide_element(index)">
                      <span class="material-symbols-outlined" v-if="hidden_elements_by_one[index]"
                            style="margin-right: 5px;">visibility_off</span>
                  <span class="material-symbols-outlined" v-else style="margin-right: 5px;">visibility</span>
                </button>

                <div style="width: 15%; display: inline-block; margin-right: 5px">
                  <div>
                    <color-picker v-model:pureColor="elements_color[index][0]"
                                  @pureColorChange="change_main_color($event, index)"
                                  :disableAlpha="true" class="inline-element"/>
                  </div>
                  <div
                      v-if="models_properties[this.work + '/' + this.season + '/' + this.sex + '/' + elements[index]]">
                    <color-picker style="padding-left: 30px" v-model:pureColor="elements_color[index][1]"
                                  v-if="models_properties[this.work + '/' + this.season + '/' + this.sex + '/' + elements[index]]['color_count'] === 2"
                                  @pureColorChange="change_second_color($event, index)"
                                  :disableAlpha="true" class="inline-element"/>
                  </div>
                </div>

                <div style="height: 100%; display: inline-block; width: 75%;">
                  <treeselect autocomplete="off" v-model="elements[index]" :close-on-select="false"
                              :clearable="false" @close="check_if_element_added"
                              :options="tree_options[this.current_types[model_type]]['children']" placeholder="Выберите элемент..."
                              :disable-branch-nodes="true"/>
                </div>

                <CCloseButton style="width: 10%; margin-left: 0" @click="deleteRow(index)" class="inline-element" :disabled="elements[index] === -1"/>
              </li>
            </n-collapse-item>
          </n-collapse>
        </ul>

        <hr style="margin-left: 30px">
        <button class="btn btn-primary small" @click="show_modal = 1" type="button"
                data-bs-toggle="modal" data-bs-target="#exampleModal"
                style="width: 70%; margin-left: 15%; color: #f3dfdf; background-color: #0353b2;">
          Сохранить макет
        </button>
      </div>
    </div>
  </div>

  <div class="modal fade" id="exampleModal" tabindex="-1" style="height: 320px" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" >
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title text-danger" id="exampleModalLabel">Настройки</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label">Название макета</label>
              <input type="text" class="form-control" placeholder="Введите название макета" v-model="layout_name">
            </div>
            <button class="btn btn-primary" @click="saveLayout">Сохранить</button>
          </form>
        </div>
      </div>
    </div>
  </div>

  <FooterComponent/>
</template>

<script>

import {CCloseButton} from '@coreui/vue'
import * as Three from 'three';
import {reactive, defineComponent} from 'vue';
import {GLTFLoader} from "three/addons/loaders/GLTFLoader";
import {ColorPicker} from "vue3-colorpicker";
import "vue3-colorpicker/style.css";

import HeaderComponent from "@/customer/HeaderComponent";
import MenuComponent from "@/customer/MenuComponent";
import FooterComponent from "@/FooterComponent";

import Treeselect from 'vue3-treeselect'
import 'vue3-treeselect/dist/vue3-treeselect.css'
import axios from "axios";

export default defineComponent({
  name: 'App',
  components: {ColorPicker, CCloseButton, Treeselect, HeaderComponent, MenuComponent, FooterComponent},

  data() {
    return {
      layout_name: '',
      show_modal: 0,
      new_element: -1,
      models_raw: [],
      current_types: {},
      models_properties: {},
      hover: false,
      hidden_elements_by_one: {},
      translates: [],
      work: "Factory",
      sex: "Man",
      season: "Summer",
      last_element_id: 0,
      start_color: "rgb(215, 215, 215)",
      ropes_color: "rgb(0, 0, 0)",
      elements: {},
      active_elements: {},
      elements_to_models: {},
      elements_color: {},
      sex_selected: 'Man/Man/Man',
      sex_options: [
        {text: 'Мужчина', value: 'Man/Man/Man'},
        {text: 'Женщина', value: 'Woman/Human/Woman'},
      ],
      season_selected: 'Summer',
      season_options: [
        {text: 'Лето', value: 'Summer'},
        {text: 'Зима', value: 'Winter'},
      ],
      work_selected: 'Factory',
      work_options: [
        {text: 'Рабочий', value: 'Factory'}
      ],
      tree_options: [],
    }
  },
  methods: {
    init: function () {
      this.targetElement = document.querySelector('#viewer');

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

      this.container = document.getElementById('viewer');

      this.camera = new Three.PerspectiveCamera(60, this.container.clientWidth / this.container.clientHeight, 0.01, 100);
      this.camera.position.y = 1.0;
      this.camera.position.z = 2.5;
      this.camera.lookAt(0, 0.7, -1)

      const color = 0xFFFFFF;
      const intensity = 1;

      const light = new Three.AmbientLight(color, 1.63);
      this.scene.add(light);


      const light1 = new Three.DirectionalLight(color, intensity);
      light1.castShadow = true;
      light1.position.set(5, 5, 5);
      light1.target.position.set(-2, 0, -1);
      light1.shadow.mapSize.width = 4096;
      light1.shadow.mapSize.height = 4096;
      this.scene.add(light1);
      this.scene.add(light1.target);

      const light2 = new Three.DirectionalLight(color, intensity);
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
      this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);

      this.container.appendChild(this.renderer.domElement);
    },

    array_index_object_by_id(array, id) {
      for (let i in array) {
        if (array[i]["id"] === id) {
          return i
        }
      }
      return -1
    },

    get_translates() {
      axios.get("/api/customer/get_translates", {
        headers: {
          "Content-Type": "application/json",
        }
      }).then((response) => {
        this.translates = response.data;
        this.get_models();
      })
    },

    get_models() {
      axios.post("/api/customer/models", {
        "work": String(this.work),
        "sex": String(this.sex),
        "season": String(this.season),
      }, {
        headers: {
          "Content-Type": "application/json",
        },
      })
          .then((response) => {
            let new_tree_select = [{
              id: -1,
              label: "Выберите элемент...",
              isDisabled: true
            }];
            this.models_raw = response.data
            for (let model in this.models_raw) {
              model = this.models_raw[model]
              this.models_properties[model["path_to_model"] + '/' + model["model"].slice(0, -4)] = {
                "model_name": model["name"],
                "description": model["description"],
                "color_count": model["color_count"],
                "type": model["type"],
              }

              let path_in_tree_select = model["path_to_model"].split('/').slice(3)

              //  BLOCK OF CREATING OF EXPANDING NODES
              if (path_in_tree_select.length === 1) {
                if (this.array_index_object_by_id(new_tree_select, path_in_tree_select[0]) === -1) {
                  let label_name = path_in_tree_select[0];
                  if (path_in_tree_select[0] in this.translates) {
                    label_name = this.translates[path_in_tree_select[0]]
                  }

                  new_tree_select.push({
                        id: path_in_tree_select[0],
                        label: label_name,
                        children: [{
                          id: -1,
                          label: "Выберите элемент...",
                          isDisabled: true
                        }]
                      }
                  )
                }
                new_tree_select[this.array_index_object_by_id(new_tree_select, path_in_tree_select[0])]["children"].push({
                  id: path_in_tree_select[0] + '/' + model["model"].slice(0, -4),
                  label: model["name"]
                })
              } else if (path_in_tree_select.length === 2) {
                if (this.array_index_object_by_id(new_tree_select, path_in_tree_select[0]) === -1) {
                  let label_name = path_in_tree_select[0];
                  if (path_in_tree_select[0] in this.translates) {
                    label_name = this.translates[path_in_tree_select[0]]
                  }
                  new_tree_select.push({
                        id: path_in_tree_select[0],
                        label: label_name,
                        children: [{
                          id: -1,
                          label: "Выберите элемент...",
                          isDisabled: true
                        }]
                      }
                  )
                }
                let object_index = this.array_index_object_by_id(new_tree_select, path_in_tree_select[0])
                if (this.array_index_object_by_id(new_tree_select[object_index]["children"], path_in_tree_select[0] + '/' + path_in_tree_select[1]) === -1) {
                  let label_name = path_in_tree_select[1];
                  if (path_in_tree_select[1] in this.translates) {
                    label_name = this.translates[path_in_tree_select[1]]
                  }
                  new_tree_select[object_index]["children"].push({
                        id: path_in_tree_select[0] + '/' + path_in_tree_select[1],
                        label: label_name,
                        children: []
                      }
                  )
                }

                new_tree_select[object_index]["children"][this.array_index_object_by_id(new_tree_select[object_index]["children"], path_in_tree_select[0] + '/' + path_in_tree_select[1])]["children"].push({
                  id: path_in_tree_select[0] + '/' + path_in_tree_select[1] + '/' + model["model"].slice(0, -4),
                  label: model["name"]
                })
              }
              // END OF BLOCK
            }
            this.tree_options = new_tree_select;
            for (let i in new_tree_select) {
              if (new_tree_select[i].id !== -1) {
                this.current_types[new_tree_select[i].label] = i;
              }
            }
          })
    },

    UpdateModel(value, option) {
      this.scene.remove(this.models[this.elements_to_models[option]]);

      let color = this.elements_color[option]
      this.load_model(value, color, false, option, this.ropes_color);
    },

    addRow(val) {
      this.elements[this.last_element_id] = val;
      this.elements_color[this.last_element_id] = [this.start_color, -1];
      this.hidden_elements_by_one[this.last_element_id] = 0;
    },

    deleteRow(index) {
      this.scene.remove(this.models[this.elements_to_models[index]]);
      delete this.elements[index];
      delete this.elements_color[index];
      delete this.hidden_elements_by_one[index];
    },

    hide_element(index) {
      this.hidden_elements_by_one[index] = 1 - this.hidden_elements_by_one[index];

      let type = this.models_properties[this.work + '/' + this.season + '/' + this.sex + '/' + this.elements[index]]["type"]
      if (type.slice(-5,) === "_main") {
        let need_to_hide_type = type.slice(0, -5)
        for (let model in this.models_properties) {
          if (this.models_properties[model]["type"] === need_to_hide_type) {
            let model_name = model.split("/").splice(3,).join('/')
            for (let el in this.elements) {
              if (this.elements[el] === model_name) {
                if (this.hidden_elements_by_one[index] === 1) {
                  this.scene.remove(this.models[this.elements_to_models[el]]);
                } else {
                  if (this.models[this.elements_to_models[index]])
                    this.scene.add(this.models[this.elements_to_models[el]]);
                }
              }
            }
          }
        }
      }

      if (this.hidden_elements_by_one[index] === 1) {
        this.scene.remove(this.models[this.elements_to_models[index]]);
      } else {
        if (this.models[this.elements_to_models[index]])
          this.scene.add(this.models[this.elements_to_models[index]]);
      }
    },

    animate: function () {
      requestAnimationFrame(this.animate);
      this.renderer.render(this.scene, this.camera);
    },

    changeStartColor: function () {
      for (let i in this.elements) {
        if (this.elements[i] === -1) {
          this.elements_color[i][0] = this.start_color;
        }
      }
    },

    changeRopesColor: function () {
      let color = this.ropes_color
      for (let i = 0; i < this.models.length; i++) {
        this.models[i].traverse(function (model) {
          if (model.isMesh) {
            if (model.material.name === "Rope") {
              model.material.color = new Three.Color(color);
            }
          }
        })
      }
    },

    work_change: function (event) {
      if (typeof (event) != "string") {
        event = event.target.value;
      }
      this.work = event;
    },

    season_change: function (event) {
      if (typeof (event) != "string") {
        event = event.target.value;
      }
      this.season = event;
      this.get_models();

      for (let index in this.elements) {
        this.scene.remove(this.models[this.elements_to_models[index]]);
        delete this.elements[index];
        delete this.elements_color[index];
      }
    },

    sex_change: function (model) {
      if (typeof (model) != "string") {
        model = model.target.value;
      }
      this.sex = model.split('/')[2]
      let model_path = model.split('/').slice(1).join('/');
      this.load_model(model_path, null, true)
    },

    load_model: function (model, color, sex_change_flag, index) {
      if (typeof (model) != "string") {
        model = model.target.value;
      }
      let rope_color = this.ropes_color;
      this.loader.load(`models/${this.work}/${this.season}/${this.sex}/${model}.glb`, (gltf) => {
        gltf.scene.position.y = -1;
        gltf.scene.position.z = -0.8;
        gltf.scene.rotation.y = this.rotation_angle;
        gltf.scene.traverse(function (model) {
          if (model.isMesh) {
            model.castShadow = true;
            if (color) {
              if (color[1] === -1) {
                model.material.color = new Three.Color(color[0]);
              } else {
                model.material.color = new Three.Color(color[0]);
                if (model.material.name === "Pocket_Left_V1_N") {
                  model.material.color = new Three.Color(color[1]);
                }
              }
            }
            if (model.material.name === "Rope") {
              model.material.color = new Three.Color(rope_color);
            }
          }
        });
        if (sex_change_flag) {
          for (let i = 0; i < this.models.length; i++) {
            this.scene.remove(this.models[i]);
          }

          this.models = [];
          this.models.push(gltf.scene);

          for (let key in this.elements) {
            if (this.elements[key] !== -1) {
              this.load_model(this.elements[key], this.elements_color[key], false, key, this.ropes_color)
            }
          }
        } else {
          this.models.push(gltf.scene);
        }
        this.elements_to_models[index] = this.models.length - 1;
        this.scene.add(gltf.scene);
      }, undefined, function (error) {
        console.error(error);
      });
    },

    change_main_color(value, index) {
      if (this.models[this.elements_to_models[index]]) {
        this.models[this.elements_to_models[index]].traverse(function (model) {
          if (model.isMesh) {
            if (model.material.name !== "Rope" && model.material.name !== "Pocket_Left_V1_N") {
              model.material.color = new Three.Color(value);
            }
          }
        })
      }
    },

    change_second_color(value, index) {
      if (this.models[this.elements_to_models[index]]) {
        this.models[this.elements_to_models[index]].traverse(function (model) {
          if (model.isMesh) {
            if (model.material.name === "Pocket_Left_V1_N") {
              model.material.color = new Three.Color(value);
            }
          }
        })
      }
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
      this.camera.position.z = this.camera.position.z + event.deltaY / 500
      this.camera.position.z = Math.max(this.camera.position.z, -0.2)
      this.camera.position.z = Math.min(this.camera.position.z, 5)
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
        this.camera.position.y = Math.max(this.camera.position.y, -0.6)
        this.camera.position.y = Math.min(this.camera.position.y, 2.2)

        this.camera.position.x += (this.lastMPos.x - event.clientX) * 0.002;
        this.camera.position.x = Math.max(this.camera.position.x, -0.3)
        this.camera.position.x = Math.min(this.camera.position.x, 0.3)
      }

      this.lastMPos = {
        x: event.clientX,
        y: event.clientY
      };
    },

    check_if_element_added() {
      if (!(Object.values(this.elements).includes(-1))) {
        this.last_element_id += 1;
        this.addRow(-1)
      }
    },

    saveLayout() {
      axios.post("/api/customer/save_layout", {
            "access_token": String(localStorage.getItem("access_token")),
            "elements": this.elements,
            "name": this.layout_name,
            "elements_color": this.elements_color,
            "active_elements": this.active_elements,
            "elements_to_models": this.elements_to_models,
            "last_element_id": this.last_element_id,
          }, {
            headers: {
              'Accept':
                  'application/json',
              'Content-Type':
                  'application/json'
            }
          }
      ).then(() => {
        alert("Макет успешно сохранён!")
      }).catch((reason) => {
        console.log(reason)
        console.log(reason.response.data)
        alert(reason.response.data.detail)
      })
    }
  },

  watch: {
    elements: {
      handler(val) {
        localStorage.setItem("elements", JSON.stringify(this.elements));
        for (let key in val) {
          if (!(key in Object.keys(this.active_elements)) || val[key] !== this.active_elements[key]) {
            if (val[key] !== -1) {
              this.UpdateModel(val[key], key);
            }
          }
        }
        Object.assign(this.active_elements, val)
      },
      deep: true,
    },

    hover: function () {
      if (this.hover) {
        document.body.style.paddingRight = "6px";
        document.body.style.overflow = "hidden";
      } else {
        document.body.style.paddingRight = "0px";
        document.body.style.overflow = "auto";
      }
    },

    new_element: {
      handler(val) {
        this.addRow(val)
        Object.assign(this.active_elements, val)
        this.new_element = -1;
      }
    },

    work_selected: {
      handler() {
        localStorage.setItem("work_selected", JSON.stringify(this.work_selected));
      }
    },
    season_selected: {
      handler() {
        localStorage.setItem("season_selected", JSON.stringify(this.season_selected));
      }
    },
    sex_selected: {
      handler() {
        localStorage.setItem("sex_selected", JSON.stringify(this.sex_selected));
      }
    },
    last_element_id: {
      handler() {
        localStorage.setItem("last_element_id", JSON.stringify(this.last_element_id));
      }
    },
    active_elements: {
      handler() {
        localStorage.setItem("active_elements", JSON.stringify(this.active_elements));
      },
      deep: true,
    },
    elements_to_models: {
      handler() {
        localStorage.setItem("elements_to_models", JSON.stringify(this.elements_to_models));
      },
      deep: true,
    },
    elements_color: {
      handler() {
        localStorage.setItem("elements_color", JSON.stringify(this.elements_color));
      },
      deep: true,
    },
  },

  mounted() {
    this.init();
    if (localStorage.getItem('work_selected'))
      this.work_selected = JSON.parse(localStorage.getItem('work_selected'));

    if (localStorage.getItem('season_selected'))
      this.season_selected = JSON.parse(localStorage.getItem('season_selected'));

    if (localStorage.getItem('sex_selected'))
      this.sex_selected = JSON.parse(localStorage.getItem('sex_selected'));
    this.sex_change(this.sex_selected);

    if (localStorage.getItem('last_element_id'))
      this.last_element_id = JSON.parse(localStorage.getItem('last_element_id'));

    if (localStorage.getItem('elements'))
      this.elements = JSON.parse(localStorage.getItem('elements'));
    if (localStorage.getItem('active_elements'))
      this.active_elements = JSON.parse(localStorage.getItem('active_elements'));
    if (localStorage.getItem('elements_to_models'))
      this.elements_to_models = JSON.parse(localStorage.getItem('elements_to_models'));
    if (localStorage.getItem('elements_color'))
      this.elements_color = JSON.parse(localStorage.getItem('elements_color'));

    this.animate();
    this.get_translates();
    // this.get_models();

    for (let i in this.elements) {
      this.hidden_elements_by_one[i] = 0;
    }

    if (!(Object.values(this.elements).includes(-1))) {
      this.addRow(-1);
    }
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

.ps {
  height: 100vh;
}

#constructor_sign {
  text-align: center;
  font-size: 40px;
  font-family: Ubuntu, serif;
  color: #24509c;
  margin-right: 5vw;
  margin-top: 3vh;
}

#middle_block {
  display: table-cell;
  height: 60vh;
}

#viewer {
  margin-bottom: 30px;
  width: 50vw;
  height: 60vh;
  text-align: center;
}

#select {
  right: 0;
  top: 0;
  display: table-cell;
  vertical-align: top;
  width: 40%;
  padding-left: 20px;
  margin-left: 5vw;
  margin-right: 0;
}

#wrapper {
  font-family: Ubuntu;
  margin-left: 4vw;
  width: 92vw;
  min-height: 70vh;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 2vh;
  margin-bottom: 2vh;
}

.row-container {
  white-space: nowrap;
}

.row_in_select > * {
  vertical-align: middle;
}

.inline-element {
  display: inline-block;
  vertical-align: middle;
  height: 100%;
}

body::-webkit-scrollbar {
  width: 6px; /* ширина scrollbar */
}

body::-webkit-scrollbar-track {
  background-color: #FFFFFF; /* цвет дорожки */
}

body::-webkit-scrollbar-thumb {
  background-color: #062051; /* цвет плашки */
  border-radius: 10px; /* закругления плашки */
  border: 1px solid #FFFFFF; /* padding вокруг плашки */
}

.modal-shadow {
  position: absolute;
  top: 0;
  left: 0;
  min-height: 100%;
  width: 100%;
  background: rgba(0, 0, 0, 0.39);
}

.modal {
  background: #fff;
  border-radius: 8px;
  padding: 15px;
  min-width: 420px;
  max-width: 480px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.modal-close {
   border-radius: 50%;
   color: #fff;
   background: #2a4cc7;
   display: flex;
   align-items: center;
   justify-content: center;
   position: absolute;
   top: 7px;
   right: 7px;
   width: 30px;
   height: 30px;
   cursor: pointer;
 }

.modal-title {
   color: #0971c7;
 }

.modal-content {
   margin-bottom: 20px
 }


</style>
