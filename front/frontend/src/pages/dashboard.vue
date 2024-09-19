<template>
    <div class="dashboard container-fluid">
      <!-- En-tête avec message de bienvenue et bouton de déconnexion -->
      <header class="row bg-primary text-white py-3 mb-4">
        <div class="col-10">
          <h1 class="mb-0">Bienvenue, {{ authStore.user.name }} !</h1>
        </div>
        <div class="col-2 text-end">
          <button @click="logout" class="btn btn-light">
            <i class="fas fa-sign-out-alt me-2"></i>Déconnexion
          </button>
        </div>
      </header>
  
      <div class="row">
        <!-- Barre latérale gauche avec les boutons de filtrage -->
        <nav class="col-md-3 mb-4">
          <div class="list-group">
            <button 
              @click="currentFilter = 'all'"
              :class="['list-group-item list-group-item-action', currentFilter === 'all' ? 'active' : '']"
            >
              Toutes les tâches
            </button>
            <button 
              @click="currentFilter = 'assigned'"
              :class="['list-group-item list-group-item-action', currentFilter === 'assigned' ? 'active' : '']"
            >
              Tâches assignées
            </button>
            <button 
              @click="currentFilter = 'completed'"
              :class="['list-group-item list-group-item-action', currentFilter === 'completed' ? 'active' : '']"
            >
              Tâches terminées
            </button>
          </div>
        </nav>
  
        <!-- Contenu principal avec la liste des tâches -->
        <main class="col-md-9">
          <h2 class="mb-4">{{ getFilterTitle() }}</h2>
          <div class="row">
            <div class="col-md-4 mb-4" v-for="task in filteredTasks" :key="task.id">
              <div class="card h-100 shadow-sm hover-effect">
                <div class="card-body d-flex flex-column">
                  <h5 class="card-title">{{ task.title }}</h5>
                  <p class="card-text flex-grow-1">{{ task.description }}</p>
                  <div class="task-info">
                    <p class="text-muted mb-2">
                      <i class="fas fa-calendar-alt me-2"></i>Échéance : {{ formatDate(task.dueDate) }}
                    </p>
                    <p :class="['mb-3', getStatusClass(task.status)]">
                      <i class="fas fa-tasks me-2"></i>Statut : {{ task.status }}
                    </p>
                  </div>
                  <div class="d-flex justify-content-between">
                    <button @click="openChat(task)" class="btn btn-primary btn-sm">
                      <i class="fas fa-comments me-2"></i>Chat
                    </button>
                    <button 
                      @click="toggleTaskCompletion(task)" 
                      :class="['btn btn-sm', task.status === 'terminé' ? 'btn-secondary' : 'btn-success']"
                    >
                      <i :class="['fas me-2', task.status === 'terminé' ? 'fa-undo' : 'fa-check']"></i>
                      {{ task.status === 'terminé' ? 'Annuler' : 'Marquer comme terminé' }}
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, computed } from 'vue'
  import { useAuthStore } from '../store/auth'
  
  export default {
    setup() {
      const authStore = useAuthStore()
      const currentFilter = ref('all')
  
      const tasks = ref([
        { id: 1, title: "Tâche 1", description: "Description de la tâche 1", dueDate: "2024-09-20", status: "à faire" },
        { id: 2, title: "Tâche 2", description: "Description de la tâche 2", dueDate: "2024-09-22", status: "en cours" },
        { id: 3, title: "Tâche 3", description: "Description de la tâche 3", dueDate: "2024-09-25", status: "terminé" }
      ])
  
      const filteredTasks = computed(() => {
        switch (currentFilter.value) {
          case 'assigned':
            return tasks.value.filter(task => task.status !== 'terminé')
          case 'completed':
            return tasks.value.filter(task => task.status === 'terminé')
          default:
            return tasks.value
        }
      })
  
      const getFilterTitle = () => {
        switch (currentFilter.value) {
          case 'assigned':
            return 'Tâches assignées'
          case 'completed':
            return 'Tâches terminées'
          default:
            return 'Toutes les tâches'
        }
      }
  
      const formatDate = (date) => {
        return new Date(date).toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric' })
      }
  
      const openChat = (task) => {
        console.log(`Ouverture du chat pour la tâche : ${task.title}`)
      }
  
      const toggleTaskCompletion = (task) => {
        task.status = task.status === 'terminé' ? 'à faire' : 'terminé'
      }
  
      const getStatusClass = (status) => {
        switch(status) {
          case 'en cours':
            return 'text-warning'
          case 'terminé':
            return 'text-success'
          default:
            return 'text-danger'
        }
      }
  
      const logout = () => {
        authStore.logout()
        // Rediriger vers la page de connexion
      }
  
      return {
        authStore,
        currentFilter,
        tasks,
        filteredTasks,
        getFilterTitle,
        formatDate,
        openChat,
        toggleTaskCompletion,
        getStatusClass,
        logout
      }
    }
  }
  </script>
  
  <style scoped>
  .dashboard {
    min-height: 100vh;
    background-color: #f8f9fa;
  }
  
  .hover-effect {
    transition: transform 0.3s ease-in-out;
  }
  
  .hover-effect:hover {
    transform: translateY(-5px);
  }
  
  .btn-secondary {
    background-color: #95a5a6;
    border-color: #95a5a6;
  }
  
  .btn-secondary:hover {
    background-color: #7f8c8d;
    border-color: #7f8c8d;
  }
  
  .text-warning {
    color: #f39c12 !important;
  }
  </style>