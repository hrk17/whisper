<script setup lang="ts">
import { ref } from 'vue';

const showUploadModal = ref(false)

const handleFileUpload = async (event: Event) => {
    const target = event.target as HTMLInputElement;

    if (!target.files || target.files.length === 0) return;
    const file = target.files[0];

    console.log("Selected file:", file.name);

    const formData = new FormData();
    formData.append("audio", file);

    try {
        // post to api
        console.log("Upload success:", file)
    } catch (error) {
        console.error("Upload failed:", error);
    }
};
</script>

<template>
    <button class="text-white bg-rose" @click="showUploadModal = true">Upload new audio file</button>
    <!-- Begin dropbox -->
    <form v-if="showUploadModal" class="pt-2">
        <div class="flex items-center justify-center w-full">
            <label for="dropzone-file"
                class="flex flex-col items-center justify-center w-full my-3 pt-2 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                <div class="flex flex-col items-center justify-center pt-5 pb-6">
                    <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2" />
                    </svg>
                    <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to
                            upload</span> or drag and drop</p>
                    <p class="text-xs text-gray-500 dark:text-gray-400">Audio files only</p>
                </div>
                <input id="dropzone-file" type="file" class="hidden" accept="audio/*" @change="handleFileUpload" />
                <button @click.stop="showUploadModal = false"
                    class="bg-rose justify-left text-white rounded-md text-sm hover:bg-rose-800" style="width: 100%;">
                    ✖ Cancel
                </button>
            </label>
        </div>
    </form>
    <!-- End dropbox -->

    <card>
        hi
    </card>
</template>