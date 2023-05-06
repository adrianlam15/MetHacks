<template>
  <main class="flex justify-center items-center h-screen">
    <div>
      <form
        @submit.prevent="submitForm"
        enctype="multipart/form-data"
        class="flex flex-col items-center"
      >
        Upload a PDF:
        <input type="file" name="pdf" ref="pdf" />
        <button type="submit">Submit</button>
      </form>
      <div v-if="uploadSuccess">UPLOADED SUCCESSFULLY</div>
      <div v-if="error">ERROR</div>
    </div>
  </main>
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
            this.uploadSuccess = false
            this.error = true
          }
        })
        .catch((error) => {
          console.error('Error:', error)
          this.uploadSuccess = false
          this.error = true
        })
    }
  },
  data() {
    return {
      uploadSuccess: false,
      prompt: ''
    }
  }
}
</script>
