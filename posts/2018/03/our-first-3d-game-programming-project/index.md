---
title: "Our first 3D game programming project"
date: 2018-03-28
---

My son Nathan made this:

<script src="https://threejs.org/build/three.js"></script>

<script>// This is where stuff in our game will happen: var scene = new THREE.Scene(); // This is what sees the stuff: var aspect_ratio = 400 / 300; var camera = new THREE.PerspectiveCamera(75, aspect_ratio, 1, 10000); camera.position.z = 500; scene.add(camera); // This will draw what the camera sees onto the screen: var renderer = new THREE.WebGLRenderer({antialias: true}); renderer.setSize(400, 300); document.getElementById('ice-code-2018-03-20').appendChild(renderer.domElement) // ******** START CODING ON THE NEXT LINE ******** var shape = new THREE.SphereGeometry(100, 20, 15); var cover = new THREE.MeshNormalMaterial(); var ball = new THREE.Mesh(shape, cover); scene.add(ball); ball.position.set(-250, 250, -250); var shape = new THREE.CubeGeometry(100, 100, 100); var cover = new THREE.MeshNormalMaterial(); var box = new THREE.Mesh(shape, cover); scene.add(box); box.rotation.set(0.5, 0.5, 0); box.position.set(250, 250, -250); var shape = new THREE.CylinderGeometry(20, 20, 100); var cover = new THREE.MeshNormalMaterial(); var tube = new THREE.Mesh(shape, cover); scene.add(tube); tube.rotation.set(0.5, 0, 0); tube.position.set(250, -250, -250); var shape = new THREE.PlaneGeometry(300, 100); var cover = new THREE.MeshNormalMaterial(); var ground = new THREE.Mesh(shape, cover); scene.add(ground); ground.rotation.set(0.5, 0, 0); ground.position.set(-250, -250, -250); var shape = new THREE.TorusGeometry(100, 25, 8, 25); var cover = new THREE.MeshNormalMaterial(); var donut = new THREE.Mesh(shape, cover); scene.add(donut); var clock = new THREE.Clock(); function animate() { requestAnimationFrame(animate); var t = clock.getElapsedTime(); ball.rotation.set(t, 2*t, 0); box.rotation.set(t, 2*t, 0); tube.rotation.set(t, 2*t, 0); ground.rotation.set(t, 2*t, 0); donut.rotation.set(t, 2*t, 0); renderer.render(scene, camera); } animate();</script>

We made it by following the first project in the book [3D Game Programming for Kids](https://pragprog.com/book/csjava/3d-game-programming-for-kids) by Chris Strom.

<iframe style="max-width: 100%;" src="https://lesen.amazon.de/kp/card?asin=B00HUEG8O6&amp;preview=inline&amp;linkCode=kpe&amp;ref_=cm_sw_r_kb_dp_zmuSAbC04SH4J" width="336" height="550" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
