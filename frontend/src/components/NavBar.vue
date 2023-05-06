<template>
<nav class="fixed top-0 flex items-center justify-between p-6 lg:px-8 z-50 w-screen bg-white border-b" aria-label="Global">
        <div class="flex lg:flex-1">
          <RouterLink to="/" class="-m-1.5 p-1.5">
            <span class="sr-only">Flash Cards Not Me!</span>
            <img
              class="h-8 w-auto"
              src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600"
              alt=""
            />
          </RouterLink>
        </div>
        <div class="flex lg:hidden">
          <button
            type="button"
            class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
          >
            <span class="sr-only">Open main menu</span>
            <svg
              class="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              aria-hidden="true"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
              />
            </svg>
          </button>
        </div>
        <div class="hidden lg:flex lg:gap-x-12">
            <a href="#features" v-smooth-scroll class="text-sm font-semibold leading-6 text-gray-900 hover:text-indigo-600
          transition ease-in-out"
            >Features</a
          >
          <RouterLink  to="/learn" class="text-sm font-semibold leading-6 text-gray-900 hover:text-indigo-600
          transition ease-in-out"
            >Learn<span class="animate-ping bg-indigo-700 absolute top-8 w-2 h-2 rounded-full"></span>
        <span class="bg-indigo-700 absolute top-8 w-2 h-2 rounded-full"></span></RouterLink>
          <a v-smooth-scroll href="/#about" class="text-sm font-semibold leading-6 text-gray-900 hover:text-indigo-600
          transition ease-in-out" 
            >About</a
          >
        </div>
        <div class="hidden lg:flex lg:flex-1 lg:justify-end">
          <!-- REPLACE LATER -->
        </div>
      </nav>
</template>