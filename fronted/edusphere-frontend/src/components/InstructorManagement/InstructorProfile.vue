<template>
    <div>
      <h2>Instructor Profile</h2>
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">{{ instructor.name }}</h5>
          <p class="card-text"><strong>Email:</strong> {{ instructor.email }}</p>
          <p class="card-text"><strong>Gender:</strong> {{ instructor.gender }}</p>
          <p class="card-text"><strong>Date of Birth:</strong> {{ instructor.date_of_birth }}</p>
          <p class="card-text"><strong>Contact Number</strong> {{ instructor.contact_number }}</p>
          <p class="card-text"><strong>Department</strong> {{ instructor.department }}</p>
          <!-- Add more instructor details here -->
        </div>
      </div>
      <router-link to="/instructors" class="btn btn-secondary mt-3">Back to List</router-link>
    </div>
  </template>
  
  <script>
import axios from 'axios';

export default {
  data() {
    return {
      instructor: {}
    };
  },
  created() {
    this.fetchInstructor();
  },
  methods: {
    async fetchInstructor() {
      const instructorId = this.$route.params.id;
      try {
        const response = await axios.get(`http://127.0.0.1:8000/instructors/${instructorId}`);
        this.instructor = response.data;
      } catch (error) {
        console.error('Error fetching instructor:', error);
      }
    }
  }
};
</script>
