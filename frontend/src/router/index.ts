import { createRouter, createMemoryHistory } from "vue-router";
import type { RouteRecordRaw } from "vue-router";

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        name: 'Home',
        component: () => import('@/views/home/Home.vue'),
    },
    {
        path: '/setores',
        name: 'Setores',
        component: () => import('@/views/setores/SetoresList.vue'),
    }
]

const router = createRouter({
    history: createMemoryHistory(),
    routes
})

export default router