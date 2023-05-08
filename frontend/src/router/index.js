import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/learn',
      name: 'learn',
      component: () => import('../views/LearnView.vue')
    },
    {
      path: '/:catchAll(.*)',
      name: 'not-found',
      component: () => import('../views/NotFoundView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('../views/DashboardView.vue')
    }
    // {
    //   path: '/forgot-password',
    //   name: 'forgot-password',
    //   component: () => import('../views/ForgotPasswordView.vue')
    // },
    // {
    //   path: '/reset-password',
    //   name: 'reset-password',
    //   component: () => import('../views/ResetPasswordView.vue')
    // },
    // {
    //   path: '/about',
    //   name: 'about',
    //   component: () => import('../views/AboutView.vue')
    // },
    // {
    //   path: '/contact',
    //   name: 'contact',
    //   component: () => import('../views/ContactView.vue')
    // },
    // {
    //   path: '/pricing',
    //   name: 'pricing',
    //   component: () => import('../views/PricingView.vue')
    // },
    // {
    //   path: '/careers',
    //   name: 'careers',
    //   component: () => import('../views/CareersView.vue')
    // },
    // {
    //   path: '/privacy',
    //   name: 'privacy',
    //   component: () => import('../views/PrivacyView.vue')
    // },
    // {
    //   path: '/blog',
    //   name: 'blog',
    //   component: () => import('../views/BlogView.vue')
    // },
    // {
    //   path: '/team',
    //   name: 'team',
    //   component: () => import('../views/TeamView.vue')
    // },
    // {
    //   path: '/support',
    //   name: 'support',
    //   component: () => import('../views/SupportView.vue')
    // },
    // {
    //   path: '/privacy-policy',
    //   name: 'privacy-policy',
    //   component: () => import('../views/PrivacyPolicyView.vue')
    // },
    // {
    //   path: '/terms-of-use',
    //   name: 'terms-of-use',
    //   component: () => import('../views/TermsOfUseView.vue')
    // },
  ]
})

export default router
