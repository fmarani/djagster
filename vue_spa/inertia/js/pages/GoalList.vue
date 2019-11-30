<template>
  <Layout>
    <p>User: {{shared.user.username || "-"}}</p>
    <h2 class="mb-4">Goals</h2>
    <ul v-if="goal_list.length">
      <li :key="goal.id" v-for="goal in goal_list">
        <inertia-link :href="'/goals/' + goal.id">
          {{goal.thing}}
        </inertia-link>
      </li>
    </ul>
    <div v-if="!goal_list.length">
      No goals
    </div>
  </Layout>
</template>

<script>
import { InertiaLink } from "@inertiajs/inertia-vue";
import Layout from "@/components/Layout";

export default {
  props: ["goal_list", "shared"],
  components: { Layout, InertiaLink }
};
</script>
