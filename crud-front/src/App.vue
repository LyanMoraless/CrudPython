<template>

<div> 
  <table>
    <thead>
      <tr>
        <th>Nome</th>
        <th>Posição</th>
        <th>Time</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="player, key in state.playersList" :key="key">
        <td>{{player.name}}</td>
        <td>{{player.position}}</td>
        <td>{{player.team}}</td>
      </tr>
    </tbody>
  </table>
</div>

</template>

<script setup>

import axios from 'axios'; 
import { reactive, onBeforeMount } from 'vue';

const state = reactive({
  playersList: [],
});

onBeforeMount(() => {
  selectPlayers()
})

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000'
})

const selectPlayers = () => {
  api.get('/players')
  .then(res => state.playersList = res.data.Players)
  .catch(err => console.log(err))
}

</script>

<style scoped>

</style>
