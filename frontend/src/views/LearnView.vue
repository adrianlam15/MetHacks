<script setup>
import in_no_time from '../assets/in_no_time_-6-igu.svg'
import check from '../assets/check.svg'
import cloud_upload from '../assets/cloud-upload.svg'

const features = [
  {
    name: 'Valid extension name.',
    description: 'Make sure your file is a PDF file.',
    icon: check
  },
  {
    name: 'Upload.',
    description: 'Upload your PDF file using the form to the right and press `submit`.',
    icon: cloud_upload
  },
  {
    name: 'Wait.',
    description: 'Wait while we generate your flash cards and get all the facts right for you.',
    icon: in_no_time
  }
]
</script>

<template>
  <div id="generate" class="relative isolate overflow-hidden sm:py-32 max-h-screen">
    <div
      class="absolute -top-52 left-1/2 -z-10 -translate-x-1/2 transform-gpu blur-3xl sm:top-[-28rem] sm:ml-16 sm:translate-x-0 sm:transform-gpu"
      aria-hidden="true"
    >
      <div
        class="aspect-[1097/845] w-[68.5625rem] bg-gradient-to-tr from-[#ff4694] to-[#776fff] opacity-20"
        style="
          clip-path: polygon(
            74.1% 44.1%,
            100% 61.6%,
            97.5% 26.9%,
            85.5% 0.1%,
            80.7% 2%,
            72.5% 32.5%,
            60.2% 62.4%,
            52.4% 68.1%,
            47.5% 58.3%,
            45.2% 34.5%,
            27.5% 76.7%,
            0.1% 64.9%,
            17.9% 100%,
            27.6% 76.8%,
            76.1% 97.7%,
            74.1% 44.1%
          );
        "
      />
    </div>
    <div
      class="absolute -top-52 left-1/2 -z-10 -translate-x-1/2 transform-gpu blur-3xl sm:top-[-28rem] sm:ml-16 sm:translate-x-0 sm:transform-gpu"
      aria-hidden="true"
    >
      <div
        class="aspect-[1097/845] w-[68.5625rem] bg-gradient-to-tr from-[#ff4694] to-[#776fff] opacity-20"
        style="
          clip-path: polygon(
            74.1% 44.1%,
            100% 61.6%,
            97.5% 26.9%,
            85.5% 0.1%,
            80.7% 2%,
            72.5% 32.5%,
            60.2% 62.4%,
            52.4% 68.1%,
            47.5% 58.3%,
            45.2% 34.5%,
            27.5% 76.7%,
            0.1% 64.9%,
            17.9% 100%,
            27.6% 76.8%,
            76.1% 97.7%,
            74.1% 44.1%
          );
        "
      />
    </div>
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div
        class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2"
      >
        <div class="lg:pr-8 lg:pt-4">
          <div class="lg:max-w-lg">
            <h2 class="text-base font-semibold leading-7 text-indigo-600">Get started.</h2>
            <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
              Start by uploading your <span class="text-indigo-600">PDF</span>.
            </p>
            <p class="mt-6 text-lg leading-8 text-gray-600">
              Upload your PDF file containing learning objectives and questions you have. We'll take
              care of the flash card generation and the fact look-ups.
            </p>
            <dl class="mt-10 max-w-xl space-y-8 text-base leading-7 text-gray-600 lg:max-w-none">
              <div v-for="feature in features" :key="feature.name" class="relative pl-9">
                <dt class="inline font-semibold text-gray-900">
                  <component class="flex flex-col">
                    <img
                      :src="feature.icon"
                      class="absolute left-1 top-1 h-5 w-5"
                      aria-hidden="true"
                    />
                    <p class="text-indigo-600">
                      {{ feature.name }}
                    </p>
                  </component>
                </dt>
                {{ ' ' }}
                <dd class="inline">{{ feature.description }}</dd>
              </div>
            </dl>
          </div>
        </div>
        <div class="pdf-form flex justify-center items-center drop-shadow-sm">
        <form
          @submit.prevent="submitForm"
          enctype="multipart/form-data"
          class="text-gray-900 font-bold flex flex-col items-center space-y-4 p-10"
        >
          <label for="pdf" class="font-bold"> Upload your PDF: </label>
          <label for="pdf">
            <img :class="{'border-rose-500' : error,
          'border-emerald-500' : uploadSuccess}" src="../assets/add_files_re_v09g.svg" class="w-48 h-48 border-2 rounded-xl p-4" alt="Add files" />
          </label>
          <p v-if="error" class="text-rose-500 font-medium text-md">Error uploading PDf file.</p>
          <p v-if="uploadSuccess" class="text-emerald-500 font-medium text-md">File uploaded successfully.</p>
          <input
            id="pdf"
            class="ml-28 font-medium py-2 px-4 focus:outline-none text-gray-600 flex"
            type="file"
            name="pdf"
            ref="pdf"
          />
          <button
            type="submit"
            class="w-20 flex justify-center transition ease-in-out rounded-md bg-indigo-600 text-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 py-2 px-4 shadow-md duration-300"
          >
            <p v-if="!isLoading" class="text-white font-medium">Submit</p>
            <svg
              v-if="isLoading"
              class="animate-spin h-5 w-5 text-white"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                class="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                stroke-width="4"
              ></circle>
              <path
                class="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
              ></path>
            </svg>
          </button>
        </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLoading: false,
      uploadSuccess: false,
      error: false
    }
  },
  methods: {
    submitForm() {
      const formData = new FormData()
      this.isLoading = true
      formData.append('pdf', this.$refs.pdf.files[0])
      fetch('http://127.0.0.1:5000/api/upload', {
        method: 'POST',
        body: formData
      })
        .then((response) => {
          if (response.status === 200) {
            console.log('Uploaded successfully')
            this.uploadSuccess = true
            this.error = false
            response.json().then((data) => {
              console.log(data)
              console.log(data.content)
            })
          } else {
            console.log('Upload failed')
            ;(this.uploadSuccess = false), (this.error = true)
          }
          this.isLoading = false
        })
        .catch((error) => {
          console.error('Error:', error)
          ;(this.uploadSuccess = false), (this.error = true)
          this.isLoading = false
        })
    }
  }
}
</script>

<style scoped>
.pdf-form {
    background-color: rgb(241,241,242);
    border-radius: 10px;
    border-color: rgb(209,213,219);
    border-width: 1px;
}

form {
    background-color: #fff;
    border-radius: 10px;
    border-color: rgb(209,213,219);
    border-width: 1px;
}

::file-selector-button {
  display: none;
}
</style>