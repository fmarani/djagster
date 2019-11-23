<template>
  <Layout>
    <h2>Success!</h2>
    <p>{{ $page.shared.title }}</p>
    <p>Inertia.js Django Boilerplate is working!</p>
  </Layout>
</template>

<script>
import Layout from "@/components/Layout";

export default {
  components: { Layout }
};
</script>
