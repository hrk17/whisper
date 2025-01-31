<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';

const showUploadModal = ref(false)
const transcript = ref(undefined as string | undefined)

const handleFileUpload = async (event: Event) => {
    const target = event.target as HTMLInputElement;

    if (!target.files || target.files.length === 0) return;
    const file = target.files[0];

    console.log("Selected file:", file.name);

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await axios.post("/api/transcribe/", formData);

        console.log("Transcription:", response.data.transcription);
        transcript.value = response.data.transcription;
        showUploadModal.value = false
    } catch (error) {
        console.error("Error transcribing audio:", error);
    }
};

const downloadTranscript = async () => {
    if (transcript.value === undefined) {
        return
    }
    const blob = new Blob([transcript.value], { type: "text/plain" });

    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "transcript.txt";

    document.body.appendChild(a);
    a.click();

    URL.revokeObjectURL(url);
    document.body.removeChild(a);
}
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


    <div class="mt-3 block p-6 bg-twilight text-white border border-gray-200 rounded-lg">
        <div class="flex justify-between">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-white">Transcription</h5>
            <button @click="downloadTranscript"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                    stroke-width="1.5" stroke="currentColor" class="size-6">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3" />
                </svg>
            </button>
        </div>
        <p class="font-normal text-white">{{ transcript }}.</p>
    </div>

</template>