<template>
  <div>
    <h1>{{$page.value}}</h1>
    <h1>{{$page.shared.title}}</h1>
    <h2>Success!</h2>
    <p>Inertia.js django Boilerplate is working!</p>
    <inertia-link href="/goals/index">LINK</inertia-link>
  </div>
</template>

<script>
import { InertiaLink } from "@inertiajs/inertia-vue";

export default {
  components: { InertiaLink }
};
</script>
