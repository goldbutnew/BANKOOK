import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import CompareView from '@/views/CompareView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import MapView from '@/views/MapView.vue'
import CommunityView from '@/views/CommunityView.vue'
import SavingsView from '@/views/SavingsView.vue'
import DepositView from '@/views/DepositView.vue'
import LogInView from '@/views/LogInView.vue'
import CreateView from '@/views/CreateView.vue'
import DetailView from '@/views/DetailView.vue'
import UserProfileView from '@/views/UserProfileView.vue'
import SignUpView from '@/views/SignUpView.vue'
import UpdateView from '@/views/UpdateView.vue'
import DepositDetailView from '@/views/DepositDetailView.vue'
import SavingsDetailView from '@/views/SavingsDetailView.vue'

import { useCounterStore } from '@/stores/counter'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/compare',
      name: 'compare',
      component: CompareView
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView
    },
    {
      path: '/create',
      name: 'create',
      component: CreateView
    },
    {
      path: '/update/:id',
      name: 'update',
      component: UpdateView
    },
    {
      path: '/community/:id',
      name: 'detail',
      component: DetailView
    },
    {
      path: '/compare/deposit',
      name: 'deposit',
      component: DepositView
    },
    {
      path: '/compare/deposit/:id',
      name: 'deposit_detail',
      component: DepositDetailView
    },
    {
      path: '/compare/savings',
      name: 'savings',
      component: SavingsView
    },
    {
      path: '/compare/savings/:id',
      name: 'savings_detail',
      component: SavingsDetailView
    },
    {
      path: '/profile',
      name: 'profile',
      component: UserProfileView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
  ]
})

router.beforeEach((to, from) =>{
  const store = useCounterStore()
  if(to.name === 'community' && !store.isLogin){
    window.alert('로그인이 필요합니다.')
    return { name: 'login' }
  }
})
export default router
