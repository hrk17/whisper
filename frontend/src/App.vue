<script setup lang="ts">
import HomePage from './pages/HomePage.vue';


</script>

<template>
  <div class="min-h-full">
    <!-- <nav class="bg-gray-800"> -->
    <nav class="bg-twilight">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="flex h-16 items-center justify-between">
          <div class="flex items-center">
            <div class="shrink-0">
              <!-- icon -->
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white"
                class="size-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M12 18.75a6 6 0 0 0 6-6v-1.5m-6 7.5a6 6 0 0 1-6-6v-1.5m6 7.5v3.75m-3.75 0h7.5M12 15.75a3 3 0 0 1-3-3V4.5a3 3 0 1 1 6 0v8.25a3 3 0 0 1-3 3Z" />
              </svg>

            </div>
            <div class="p-2.5 text-white">
              Relay: An Audio Transcription Application
            </div>
          </div>
        </div>
      </div>
    </nav>
    <main>
      <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <HomePage></HomePage>
      </div>
    </main>
  </div>
</template>

<style scoped></style>
