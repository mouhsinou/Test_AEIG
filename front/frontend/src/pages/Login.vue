<template>
    <div class="login d-flex justify-content-center align-items-center vh-100">
      <div class="card p-4 shadow-sm" style="max-width: 400px; width: 100%;">
        <h2 class="text-center mb-4">Connexion</h2>
        <form @submit.prevent="login">
          <!-- Email -->
          <div class="form-group mb-3">
            <label for="email" class="form-label">Adresse email</label>
            <div class="input-group">
              <span class="input-group-text"><i class="fas fa-envelope"></i></span>
              <input v-model="email" id="email" type="email" class="form-control" placeholder="Entrez votre email" required @input="resetError">
            </div>
          </div>
          
          <!-- Password -->
          <div class="form-group mb-3">
            <label for="password" class="form-label">Mot de passe</label>
            <div class="input-group">
              <span class="input-group-text"><i class="fas fa-lock"></i></span>
              <input v-model="password" id="password" type="password" class="form-control" placeholder="Entrez votre mot de passe" required @input="resetError">
            </div>
          </div>
          
          <!-- Error Message -->
          <p v-if="error" class="text-danger text-center">{{ error }}</p>
          
          <!-- Submit Button -->
          <div class="d-grid mb-3">
            <button type="submit" class="btn btn-primary btn-block">Se connecter</button>
          </div>
  
          <!-- Sign Up Link -->
          <div class="text-center">
            <p>Pas encore de compte ? <router-link to="/register">S'inscrire</router-link></p>
          </div>
  
          <!-- Divider -->
          <hr>
          
          <!-- Login with Google -->
          <div class="d-grid">
            <button class="btn btn-outline-danger btn-block">
              <i class="fab fa-google me-2"></i> Connexion avec Google
            </button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import { useAuthStore } from '../store/auth'
  
  export default {
    setup() {
      const authStore = useAuthStore()
      return {
        authStore
      }
    },
    data() {
      return {
        email: "",
        password: "",
        error: ""
      }
    },
    methods: {
      async login(){
        await this.authStore.login(this.email, this.password, this.$router)
        if (!this.authStore.isAuthenticated){
          this.error = 'La connexion a échoué. Vérifiez vos informations.'
        }
      },
      resetError(){
        this.error = ""
      }
    }
  }
  </script>
  
  <style scoped>
  .login {
    background: url('@/assets/login-background.jpg') no-repeat center center;
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
  