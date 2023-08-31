import { createRouter, createWebHistory } from 'vue-router';
import InstructorList from '@/components/InstructorManagement/InstructorList.vue';
import InstructorProfile from '@/components/InstructorManagement/InstructorProfile.vue';
import CreateInstructor from '@/components/InstructorManagement/CreateInstructor.vue';
import EditInstructor from '@/components/InstructorManagement/EditInstructor.vue';

const routes = [
  { path: '/', redirect: '/instructors' },
  { path: '/instructors', component: InstructorList },
  { path: '/instructors/:id', component: InstructorProfile },
  { path: '/instructors/create', component: CreateInstructor },
  { path: '/instructors/edit/:id', component: EditInstructor }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
