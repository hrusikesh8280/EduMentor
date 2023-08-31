<template>
    <div>
      <h2>Instructor List</h2>
      <table class="table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Actions</th>
            <th> Department</th>
          </tr>
        </thead>
        <tbody>
          <!-- Loop through instructors -->
          <tr v-for="instructor in instructors" :key="instructor.id">
            <td>{{ instructor.name }}</td>
            <td>{{ instructor.email }}</td>
            <td>{{ instructor. Department }}</td>
            <td>
              <button @click="viewProfile(instructor.id)" class="btn btn-primary">View</button>
              <button @click="editInstructor(instructor.id)" class="btn btn-warning">Edit</button>
              <button @click="deleteInstructor(instructor.id)" class="btn btn-danger">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
      <router-link to="/instructors/create" class="btn btn-success">Create Instructor</router-link>
      <router-link to="/instructors" class="btn btn-secondary mt-3">Back to List</router-link>
      <router-link to="/instructors" class="btn btn-secondary">Cancel</router-link>
    </div>
  </template>
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        instructors: []
      };
    },
    created() {
      this.fetchInstructors();
    },
    methods: {
      async fetchInstructors() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/instructors/');
          this.instructors = response.data;
        } catch (error) {
          console.error('Error fetching instructors:', error);
        }
      },
      viewProfile(id) {
        this.$router.push(`/instructors/${id}`);
      },
      editInstructor(id) {
        this.$router.push(`/instructors/edit/${id}`);
      },
      async deleteInstructor(id) {
        try {
          await axios.delete(`http://127.0.0.1:8000/instructors/${id}`);
          this.fetchInstructors(); // Refresh the list after deletion
        } catch (error) {
          console.error('Error deleting instructor:', error);
        }
      }
    }
  };
  </script>
  