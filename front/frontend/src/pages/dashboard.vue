<template>
    <div class="dashboard container my-5">
        <h2 class="text-center mb-4">Vos tâches</h2>
        <div class="row">
            <div class="col-md-4" v-for="task in tasks" :key="task.id">
                <div class="card mb-4 shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title">{{ task.title }}</h5>
                        <p class="card-text">{{ task.description }}</p>
                        <p class="text-muted">Échéance : {{ task.dueDate }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            tasks: [
                { id: 1, title: "Tâche 1", description: "Description de la tâche 1", dueDate: "20/09/2024" },
                { id: 2, title: "Tâche 2", description: "Description de la tâche 2", dueDate: "22/09/2024" },
                { id: 3, title: "Tâche 3", description: "Description de la tâche 3", dueDate: "25/09/2024" }
            ]
        }
    }
}
</script>

<style scoped>
.card {
    transition: transform 0.2s;
}

.card:hover {
    transform: translateY(-10px);
}

.dashboard h2 {
    font-weight: bold;
}
</style>
