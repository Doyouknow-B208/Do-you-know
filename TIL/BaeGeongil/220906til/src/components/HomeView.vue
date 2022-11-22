<template>
  <div>
    <div>hello</div>
    <canvas class="webgl"></canvas>
  </div>
</template>

<script>
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";

export default {
  setup() {
    const scene = new THREE.Scene();
    const fov = 60;
    const aspect = window.innerWidth / window.innerHeight;
    const near = 0.1;
    const far = 1000;

    const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
    camera.position.z = 2;

    const renderer = new THREE.WebGLRenderer({
      antialias: true,
    });

    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.autoClear = false;
    //renderer background color
    renderer.setClearColor(0xfffff, 0.0);

    document.body.appendChild(renderer.domElement);

    const texture = new THREE.TextureLoader().load("texture/earthmap1k.jpg");

    const earthGeometry = new THREE.SphereGeometry(0.6, 32, 32);
    const earthMaterial = new THREE.MeshPhongMaterial({
      // roughness: 1,
      // metalness: 0,
      map: texture,
      // bumpMap: THREE.ImageUtils.loadTexture('')
      // bumpScale: 0.3;
    });

    const earth = new THREE.Mesh(earthGeometry, earthMaterial);
    scene.add(camera);
    scene.add(earth);

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.2);
    scene.add(ambientLight);

    const pointLight = new THREE.PointLight(0xffffff, 1);
    pointLight.position.set(5, 3, 5);
    scene.add(pointLight);

    // camera.position(0, 0, 0);
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.update();

    function animate() {
      requestAnimationFrame(animate);
      controls.update();

      earth.rotation.y += 0.0015;

      render();
    }

    const render = () => {
      renderer.render(scene, camera);
    };
    animate();
  },
};
</script>

<style>
.webgl {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
