<template>
    <div class="lg:px-32 pt-28 mx-auto h-screen">
        <h2 class="text-base font-semibold leading-7 text-indigo-600">Flashcards.</h2>
        <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            Here's what we found for <span class="text-indigo-600">you</span>.
        </p>
        <p class="mt-6 text-lg leading-8 text-gray-600 w-96">
            Here's a list of flashcards that we thought you might find helpful based on your requests.
        </p>
        <div class="mt-20 flex justify-center items-center">
            <div v-for="(card, index) in flashcards" :key="index">
                <div @click="flipCard(card)" class="border-gray-600 border-2 py-4 px-6 rounded-lg w-96 h-52">
                    <div v-if="!card.flipped">
                    <h1 class="p-2 text-3xl font-bold text-center">Question</h1>
                    <p class="text-lg text-center">{{ card.Q }}</p>
                    </div>
                    <div v-else>
                    <h1 class="p-2 text-3xl font-bold text-center">Answer</h1>
                    <p class="text-lg text-center">{{ card.A }}</p>
                    </div>
                </div>
                </div>
        </div>
    </div>

</template>
<script>
export default {
  methods: {
    flipCard(card) {
      card.flipped = !card.flipped;
    },
  },
  props: {
    flashcards: {
        type: Array,
        required: true,
    }
  }
  
};
</script>