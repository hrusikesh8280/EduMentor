<template>
    <div>
      <h2>Create Instructor</h2>
      <form @submit.prevent="createInstructor">
        <div class="mb-3">
          <label for="name" class="form-label">Name</label>
          <input v-model="instructor.name" type="text" class="form-control" id="name" required>
        </div>
        <div class="mb-3">
          <label class="form-label">Gender</label>
          <div>
            <label class="form-check-label">
              <input v-model="instructor.gender" type="radio" class="form-check-input" value="Male"> Male
            </label>
            <label class="form-check-label">
              <input v-model="instructor.gender" type="radio" class="form-check-input" value="Female"> Female
            </label>
            <label class="form-check-label">
              <input v-model="instructor.gender" type="radio" class="form-check-input" value="Other"> Other
            </label>
          </div>
        </div>
        <div class="mb-3">
          <label for="dateOfBirth" class="form-label">Date of Birth</label>
          <input v-model="instructor.dateOfBirth" type="date" class="form-control" id="dateOfBirth" required>
        </div>
        <div class="mb-3">
          <label for="department" class="form-label">Department</label>
          <select v-model="instructor.department" class="form-select" id="department" required>
            <option value="Science">Science</option>
            <option value="Arts">Arts</option>
            <option value="Engineering">Engineering</option>
            <!-- Add more options as needed -->
          </select>
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input v-model="instructor.email" type="email" class="form-control" id="email" required>
        </div>
        <div class="mb-3">
          <label for="contactNumber" class="form-label">Contact Number</label>
          <input v-model="instructor.contactNumber" type="text" class="form-control" id="contactNumber" required>
        </div>
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
          gender: '',
          dateOfBirth: '',
          department: '',
          email: '',
          contactNumber: ''
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
  