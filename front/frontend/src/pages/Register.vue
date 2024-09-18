<template>
    <div class="register d-flex justify-content-center align-items-center vh-100">
      <div class="card p-4 shadow-sm" style="max-width: 400px; width: 100%;">
        <h2 class="text-center mb-4">Inscription</h2>
        <form @submit.prevent="register">
          <!-- Email -->
          <div class="form-group mb-3">
            <label for="email" class="form-label">Adresse email</label>
            <div class="input-group">
              <span class="input-group-text"><i class="fas fa-envelope"></i></span>
              <input v-model="email" id="email" type="email" class="form-control" placeholder="Entrez votre email" required>
            </div>
          </div>
          
          <!-- Password -->
          <div class="form-group mb-3">
            <label for="password" class="form-label">Mot de passe</label>
            <div class="input-group">
              <span class="input-group-text"><i class="fas fa-lock"></i></span>
              <input v-model="password" id="password" type="password" class="form-control" placeholder="Entrez votre mot de passe" required>
            </div>
          </div>
          
          <!-- Error or Success Message -->
          <p v-if="error" class="text-danger text-center">{{ error }}</p>
          <p v-if="success" class="text-success text-center">{{ success }}</p>
          
          <!-- Submit Button -->
          <div class="d-grid mb-3">
            <button type="submit" class="btn btn-primary btn-block">S'inscrire</button>
          </div>
  
          <!-- Login Link -->
          <div class="text-center">
            <p>Déjà un compte ? <router-link to="/login">Se connecter</router-link></p>
          </div>
  
          <!-- Divider -->
          <hr>
          
          <!-- Sign Up with Google -->
          <div class="d-grid">
            <button class="btn btn-outline-danger btn-block">
              <i class="fab fa-google me-2"></i> Inscription avec Google
            </button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import { getCSRFToken } from '../store/auth'
  
  export default {
    data() {
      return {
        email: '',
        password: '',
        error: '',
        success: ''
      }
    },
    methods: {
      async register() {
        try {
          const response = await fetch('http://localhost:8000/api/register', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({
              email: this.email,
              password: this.password
            }),
            credentials: 'include'
          })
          const data = await response.json()
          if (response.ok) {
            this.success = 'Inscription réussie ! Veuillez vous connecter.'
            setTimeout(() => {
              this.$router.push('/login')
            }, 1000)
          } else {
            this.error = data.error || 'Échec de l\'inscription'
          }
        } catch (err) {
          this.error = 'Une erreur est survenue lors de l\'inscription : ' + err
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .register {
    background: url('@/assets/register-background.jpg') no-repeat center center;
    background-size: cover;
  }
  
  .card {
    background-color: rgba(255, 255, 255, 0.85);
    border-radius: 15px;
  }
  
  input {
    border-radius: 0 !important;
  }
  
  button {
    border-radius: 5px;
  }
  
  .fas, .fab {
    font-size: 1.2rem;
  }
  </style>
  