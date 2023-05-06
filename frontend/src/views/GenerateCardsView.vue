<script setup>
//   import { CloudArrowUpIcon, LockClosedIcon, ServerIcon } from '@heroicons/vue/20/solid'
  
  const features = [
    {
      name: 'Valid extension name.',
      description:
        'Make sure your file is a PDF file.',
    //   icon: CloudArrowUpIcon,
    },
    {
      name: 'Upload.',
      description: 'Upload your PDF file using the form to the right and press `submit`.',
    //   icon: LockClosedIcon,
    },
    {
      name: 'Wait',
      description: 'Wait while we generate your flash cards and get all the facts right for you.',
    //   icon: ServerIcon,
    },
  ]
</script>

<template>
    <div id="features" class="relative isolate overflow-hidden py-24 sm:py-32">
        <div class="absolute -top-52 left-1/2 -z-10 -translate-x-1/2 transform-gpu blur-3xl sm:top-[-28rem] sm:ml-16 sm:translate-x-0 sm:transform-gpu" aria-hidden="true">
      <div class="aspect-[1097/845] w-[68.5625rem] bg-gradient-to-tr from-[#ff4694] to-[#776fff] opacity-20" style="clip-path: polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)" />
    </div>
    <div class="absolute -top-52 left-1/2 -z-10 -translate-x-1/2 transform-gpu blur-3xl sm:top-[-28rem] sm:ml-16 sm:translate-x-0 sm:transform-gpu" aria-hidden="true">
      <div class="aspect-[1097/845] w-[68.5625rem] bg-gradient-to-tr from-[#ff4694] to-[#776fff] opacity-20" style="clip-path: polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)" />
    </div>
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2">
          <div class="lg:pr-8 lg:pt-4">
            <div class="lg:max-w-lg">
              <h2 class="text-base font-semibold leading-7 text-indigo-600">Get started.</h2>
              <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Start by uploading your PDF.</p>
              <p class="mt-6 text-lg leading-8 text-gray-600">Upload your PDF file containing learning objectives and questions you have. We'll take care of the flash card generation and the fact look-ups.</p>
              <dl class="mt-10 max-w-xl space-y-8 text-base leading-7 text-gray-600 lg:max-w-none">
                <div v-for="feature in features" :key="feature.name" class="relative pl-9">
                  <dt class="inline font-semibold text-gray-900">
                    <!-- <component :is="feature.icon" class="absolute left-1 top-1 h-5 w-5 text-indigo-600" aria-hidden="true" />
                    {{ feature.name }} -->
                  </dt>
                  {{ ' ' }}
                  <dd class="inline">{{ feature.description }}</dd>
                </div>
              </dl>
            </div>
          </div>
          <form
  @submit.prevent="submitForm"
  enctype="multipart/form-data"
  class="text-gray-900 font-bold flex flex-col items-center space-y-4 pt-32"
>
  <label for="pdf" class="font-bold">
    Upload your PDF:
  </label>
  <input
    id="pdf"
    class="font-medium py-2 px-4 border-2 border-gray-900 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
    type="file"
    name="pdf"
    ref="pdf"
  />
  <button
    type="submit"
    class="transition ease-in-out hover:-translate-y-1 rounded-md bg-indigo-600 text-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 text-white font-medium py-2 px-4 shadow-md duration-300"
  >
    Submit
  </button>
</form>

      <div v-if="uploadSuccess">UPLOADED SUCCESSFULLY</div>
      <div v-if="error">ERROR</div>
        </div>
      </div>
    </div>
  </template>

<script>
export default {
  methods: {
    submitForm() {
      const formData = new FormData()
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
            this.uploadSuccess = false,
            this.error = true
          }
        })
        .catch((error) => {
          console.error('Error:', error)
          this.uploadSuccess = false,
          this.error = true
   })
}}}
</script>
