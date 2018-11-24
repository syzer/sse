<template>
  <div>
     <v-container grid-list-md>
       <v-layout row>
      <!-- SEARCH -->
        <v-flex xs2>
          TODO FILTERS
        </v-flex>
          <v-flex xs10>
            <v-autocomplete
                v-model="model"
                :items="randomMedicalWords"
                :readonly="!isEditing"
                @click="toggleEdit()"
                :search-input.sync="search"
                append-icon="mdi-magnify"
                chips
                multiple
              >
              <template
                slot="selection"
                slot-scope="data"
              >
                <v-chip
                  :selected="data.selected"
                  close
                  class="chip--select-multi"
                  @input="remove(data.item)"
                >
                  {{ data.item }}
                </v-chip>
              </template>
            </v-autocomplete>
              <!-- END OF SEARCH -->

              <!-- RESULTS DISPLAY -->
              <v-card class="my-2" v-for="article in dummyArticles" :key="article.id">
                <v-card-title primary-title>
                  <div>
                    <div class="headline">{{article.title}}</div>
                    <div>{{article.text}}</div>
                  </div>
                  <br>
                  <span class="grey--text">{{article.date}}</span>
                </v-card-title>
            </v-card>
              <!-- END OF RESULTS DISPLAY -->
            </v-flex>
        </v-layout>
      </v-container>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      model: null,
      isEditing: false,
      search: null,
      items: [],
      randomMedicalWords: [
        'aspirin', 'insulin', 'hemoglobin', 'chlorophyl', 'diabetes',
        'blood pressure', 'leukemia', 'multiple sclerosis', 'glucose', 'LSD',
        'chemistry', 'quantum', 'evolution', 'rat', 'yeast',
        'adenine', 'hair loss', 'protein', 'hydrolic pressure', 'antibodies'
      ],
      dummyArticles: [
        {id: 0, title: 'Title of example article', text: 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At glucose eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet...', date: '11 November 2018'},
        {id: 1, title: 'Title of another article', text: 'Lorem antibodies dolor sit amet, leukemia sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, glucose diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet...', date: '01 December 2011'},
        {id: 2, title: 'Title of awesome article', text: 'Lorem ipsum dolor sit amet, antibodies sadipscing elitr, sed diam hydrolic eirmod tempor LSD ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet...', date: '06 May 2015'},
        {id: 3, title: 'Title of dummy article', text: 'Lorem rat dolor sit amet, yeast sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet...', date: '12 March 1977'},
        {id: 4, title: 'Title of fake article', text: 'Lorem ipsum hydrolic pressure sit amet, consetetur sadipscing elitr, sed diam LSD eirmod tempor invidunt ut hair loss et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet...', date: '07 November 1996'},
        {id: 5, title: 'Title of medical article', text: 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet...', date: '22 March 2001'},
        {id: 6, title: 'Title of article about diabetes', text: 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna yeast erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet...', date: '09 February 2017'},
        {id: 7, title: 'Title of last article', text: 'Lorem ipsum dolor sit amet, hair loss sadipscing leukemia, sed diam rat eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet...', date: '30 January 2017'}
      ]
    }
  },
  watch: {
    search (val) {
      val && this.querySelections(val)
    }
  },
  methods: {
    toggleEdit () {
      this.isEditing = !this.isEditing
    },
    querySelections (v) {
      this.items = this.randomMedicalWords.filter(e => {
        return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
      })
    },
    remove (item) {
      const index = this.randomMedicalWords.indexOf(item)
      if (index >= 0) this.randomMedicalWords.splice(index, 1)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
