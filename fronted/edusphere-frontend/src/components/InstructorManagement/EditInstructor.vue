<template>
    <div>
      <h2>Create Instructor</h2>
      <form @submit.prevent="createInstructor">
        <div class="mb-3">
          <label for="name" class="form-label">Name</label>
          <input v-model="instructor.name" type="text" class="form-control" id="name" required>
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input v-model="instructor.email" type="email" class="form-control" id="email" required>
        </div>
        <div class="mb-3">
          <label for="department" class="form-label">Department</label>
          <input v-model="instructor.department" type="email" class="form-control" id="email" required>
        </div>
        <div class="mb-3">
          <label for="contact_number" class="form-label">Contact_Number</label>
          <input v-model="instructor.contact_number" type="email" class="form-control" id="email" required>
        </div>
        <!-- Add more fields here -->
        <button type="submit" class="btn btn-primary">Create</button>
        <router-link to="/instructors" class="btn btn-secondary">Cancel</router-link>
      </form>
    </div>
  </template>
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        instructor: {
          name: '',
          email: '',
          department:'',
          contact_number :''
        }
      };
    },
    methods: {
      async createInstructor() {
        try {
          await axios.post('http://127.0.0.1:8000/instructors/', this.instructor);
          this.$router.push('/instructors'); // Navigate back to the list
        } catch (error) {
          console.error('Error creating instructor:', error);
        }
      }
    }
  };
  </script>
  