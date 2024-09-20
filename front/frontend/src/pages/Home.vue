<template>
    <div class="home">
        <!-- Ajout d'un en-tête pour le bouton de déconnexion -->
        <header v-if="authStore.isAuthenticated" class="logout-header">
            <button @click="logout" class="btn-icon logout-btn" title="Se déconnecter">
                <i class="fas fa-sign-out-alt"></i>
            </button>
        </header>

        <!-- Hero Section -->
        <section class="hero-section d-flex justify-content-center align-items-center text-center">
            <div class="container">
                <h1 class="display-3">Bienvenue sur notre plateforme</h1>
                <p class="lead">Découvrez une nouvelle façon de collaborer et gérer vos projets en toute simplicité.</p>
                <div class="mt-5">
                    <router-link v-if="!authStore.isAuthenticated" to="/register" class="btn btn-primary btn-lg me-3">S'inscrire</router-link>
                    <router-link v-if="!authStore.isAuthenticated" to="/login" class="btn btn-outline-light btn-lg">Se connecter</router-link>
                    <p v-if="authStore.isAuthenticated" class="welcome-msg text-white">Bienvenue {{ authStore.user?.username }} !</p>
                    <div v-if="authStore.isAuthenticated">
                        <a href="http://localhost:8000/dashboard/" style="text-decoration: none; color :green ">Commencer</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Features Section -->
        <section class="features-section py-5">
            <div class="container">
                <h2 class="text-center mb-5">Cette plateforme vous failite : </h2>
                <div class="row">
                    <div class="col-md-4 mb-4">
                        <div class="card h-100">
                            <div class="card-body text-center">
                                <i class="fas fa-tasks fa-3x mb-3"></i>
                                <h5 class="card-title">Gestion de Projets</h5>
                                <p class="card-text">Organisez, priorisez et suivez vos projets en toute simplicité.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4 mb-4">
                        <div class="card h-100">
                            <div class="card-body text-center">
                                <i class="fas fa-comments fa-3x mb-3"></i>
                                <h5 class="card-title">Collaboration en Temps Réel</h5>
                                <p class="card-text">Travaillez ensemble sur les projets avec des mises à jour en direct.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4 mb-4">
                        <div class="card h-100">
                            <div class="card-body text-center">
                                <i class="fas fa-shield-alt fa-3x mb-3"></i>
                                <h5 class="card-title">Sécurité Avancée</h5>
                                <p class="card-text">Vos données sont sécurisées grâce à un système robuste.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import { useAuthStore } from '../store/auth'
import { useRouter } from 'vue-router'

export default {
    setup() {
        const authStore = useAuthStore()
        const router = useRouter()

        const logout = async () => {
            try {
                await authStore.logout()
                router.push('/login')
            } catch (error) {
                console.error(error)
            }
        }

        return {
            authStore,
            logout
        }
    },
    async mounted() {
        await this.authStore.fetchUser()
    }
}
</script>

<style scoped>
.home {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    position: relative;  /* Ajouté pour le positionnement du bouton de déconnexion */
}

.logout-header {
    position: absolute;
    top: 10px;
    right: 10px;
    z-index: 1000;
}

.btn-icon {
    background: none;
    border: none;
    color: white;
    font-size: 1.5rem;
    cursor: pointer;
    padding: 5px 10px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.btn-icon:hover {
    background-color: rgba(255, 255, 255, 0.2);
}

.hero-section {
    flex: 1;
    background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
                url('@/assets/OIP.jpeg') no-repeat center center;
    background-size: cover;
    color: #ffffff;
    padding: 4rem 0;
}

.hero-section h1 {
    font-weight: 700;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);
}

.hero-section p {
    font-size: 1.25rem;
    margin-bottom: 2rem;
    text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.7);
}

.features-section {
    background-color: #f8f9fa;
    padding: 4rem 0;
}

.card {
    border: none;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.card-body {
    padding: 2rem;
}

.fas {
    color: #4a90e2;
}

.btn {
    border-radius: 30px;
    padding: 0.75rem 2rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: all 0.3s ease;
}

.btn-primary {
    background-color: #4a90e2;
    border-color: #4a90e2;
}

.btn-primary:hover {
    background-color: #3a7bc8;
    border-color: #3a7bc8;
}

.btn-outline-light:hover {
    background-color: #ffffff;
    color: #4a90e2;
}

.welcome-msg {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 1rem;
}

@media (max-width: 768px) {
    .hero-section {
        padding: 2rem 0;
    }

    .hero-section h1 {
        font-size: 2.5rem;
    }

    .hero-section p {
        font-size: 1rem;
    }

    .btn-lg {
        padding: 0.5rem 1.5rem;
        font-size: 1rem;
    }
}
</style>