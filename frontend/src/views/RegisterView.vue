<template>
    <div class="flex min-h-screen flex-1 flex-col justify-center px-6 py-12 lg:px-8">
      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <img class="mx-auto h-10 w-auto" src="../assets/logo.svg" alt="SmartCard" />
        <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Register your account</h2>
      </div>
  
      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form class="space-y-6" action="#" method="POST">
          <div>
            <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
            <div class="mt-2">
              <input v-model="email" id="email" name="email" type="email" autocomplete="email" placeholder="Enter your email" required="true" class="px-2 w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            </div>
          </div>
  
          <div>
            <div class="flex items-center justify-between">
              <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
            </div>
            <div class="mt-2">
              <input :class="{ 'ring-rose-500' : error,
              'ring-2' : error}" v-model="password" id="password" name="password" type="password" placeholder="Enter your password" autocomplete="current-password" required="true" class="px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            </div>
          </div>

          <div>
            <div class="flex items-center justify-between">
                <label for="retype-password" class="block text-sm font-medium leading-6 text-gray-900">Retype Password</label>
            </div>
            <div class="mt-2">
                <input :class="{ 'ring-rose-500' : error,
              'ring-2' : error}" v-model="retypePassword" id="retype-password" name="retypePassword" type="password" placeholder="Retype your password" required="true" class="px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            </div>
          </div>
  
          <div>
            <button @click.prevent="submitForm" type="submit" class="hover:-translate-y-1 transition ease-in-out flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Register</button>
          </div>
        </form>
        </div>
    </div>
  </template>

  <script>
  export default {
    data() {
      return {
        email: '',
        password: '',
        retypePassword: '',
        error: false
      }
    },
    methods: {
      submitForm() {
        if (this.password !== this.retypePassword) {
          this.error = true
          alert('Passwords do not match')
          return
        }
        this.error = false
        console.log(this.email, this.password)
        fetch('http://127.0.0.1:5000/api/auth/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password
          })
        }).then(response => console.log(response))
      }
    },
  }
  </script>
  