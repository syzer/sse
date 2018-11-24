<template>
  <div id="app">
    <v-app>
      <v-toolbar app>
        <app-header></app-header>
      </v-toolbar>
        <v-content>
          <v-container fluid>
            <router-view></router-view>
          </v-container>
        </v-content>
      <v-footer app>
        <app-footer></app-footer>
      </v-footer>
    </v-app>
  </div>
</template>

<script>
import AppHeader from '@/components/Header'
import AppFooter from '@/components/Footer'

export default {
  name: 'App',
  components: {
    AppHeader,
    AppFooter
  }
}
</script>
