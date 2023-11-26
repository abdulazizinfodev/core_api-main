<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'

export default {

    data() {
        return {
            video: [],
            video_access: true,
            errors: [],
            add_access: '',
        }
    },

    mounted() {
        this.getFeed()
    },

    methods: {
        getFeed() {
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': `JWT ${localStorage.getItem('user.access')}`,
                }
            };
            axios
                .get(`/api/videos/video/${this.$route.params.id}/`, config)
                .then(response => {
                    console.log(response.data)
                    this.video = response.data['video']
                    this.video_access = false

                })
                .catch(error => {
                })
        },
        async AddAccess(id) {
            if ((localStorage.getItem('user.access'))) {
                const config = {
                    headers: {
                        'Authorization': `JWT ${localStorage.getItem('user.access')}`,
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    }
                };
                const video_id = id;
                const body = JSON.stringify({
                    video_id
                });
                axios
                    .post(`/api/videos/video-mark/${this.$route.params.id}/`, body, config)
                    .then(response => {
                        if (response.status === 202) {
                            this.add_access = response.data['data']
                        }
                    })
                    .catch(error => {
                    })
            } else {
                this.toastStore.showToast(3000, "Please, Log In", 'Unauthorized', 'bg-red-500 text-white');
            }
        },
    }
}
</script>

<template>
    <template v-if="video_access">
        <div class="pr-2 pb-2">
            <div class="py-3 px-1 mx-1 w-full">
                <div class="pt-6 px-5">
                    <div role="status" class="space-y-8 animate-pulse md:space-y-0 md:space-x-8 md:flex md:items-center">
                        <div
                            class="flex items-center justify-center w-full h-48 bg-gray-300 rounded sm:w-96 dark:bg-gray-700">
                            <p>Video not access</p>
                        </div>
                        <span class="sr-only">Loading...</span>
                    </div>
                </div>
            </div>
        </div>
    </template>
    <template v-else>
        <section class="ml-4 mr-4">
            <div class="bg-gray-800 relative overflow-hidden rounded-lg">
                <div class="flex flex-col md:flex-row items-center justify-between space-y-3 md:space-y-0 md:space-x-4 p-4">
                    <div class="w-full md:w-1/2">
                        <h2 class="text-gray-100 font-semibold text-xl">{{ video.name }}</h2>
                    </div>
                    <div
                        class="w-full md:w-auto flex flex-col md:flex-row space-y-2 md:space-y-0 items-stretch md:items-center justify-end md:space-x-3 flex-shrink-0">
                        <p @click="AddAccess(video.id)" class="text-xl tracking-tight mb-1 text-gray-900 cursor-pointer">
                            <span
                                class="bg-blue-600 text-gray-100 text-xs font-medium me-2 px-2.5 py-2.5 rounded dark:bg-green-900 dark:text-green-300">
                                Mark is view
                            </span>
                        </p>
                    </div>
                </div>
                <div class="overflow-x-auto">
                    <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
                        <div class="max-w-screen-lg text-gray-100 sm:text-lg">
                            <h2 class="mb-4 text-4xl tracking-tight font-bold text-gray-100">Powering
                                innovation at <span class="font-extrabold">200,000+</span> companies worldwide</h2>
                            <p class="mb-4 font-light">Track work across the enterprise through an open, collaborative
                                platform. Link issues across Jira and ingest data from other software development tools,
                                so your IT support and operations teams have richer contextual information to rapidly
                                respond to requests, incidents, and changes.</p>
                            <p class="mb-4 font-medium">Deliver great service experiences fast - without the complexity
                                of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and
                                deploy changes with ease.</p>
                            <a href="#" class="inline-flex items-center font-medium text-gray-100 hover:text-gray-500">
                                Learn more
                                <svg class="ml-1 w-6 h-6" fill="currentColor" viewBox="0 0 20 20"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd"
                                        d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                                        clip-rule="evenodd"></path>
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>
                <nav class="flex flex-col md:flex-row justify-between items-start md:items-center space-y-3 md:space-y-0 p-4"
                    aria-label="Table navigation">
                    <span class="text-sm font-normal text-gray-500 dark:text-gray-400">
                        Showing
                        <span class="font-semibold text-gray-900 dark:text-white">1-10</span>
                        of
                        <span class="font-semibold text-gray-900 dark:text-white">1000</span>
                    </span>
                    <ul class="inline-flex items-stretch -space-x-px">
                        <li>
                            <a href="#"
                                class="flex items-center justify-center h-full py-1.5 px-3 ml-0 text-gray-500 bg-white rounded-l-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                                <span class="sr-only">Previous</span>
                                <svg class="w-5 h-5" aria-hidden="true" fill="currentColor" viewbox="0 0 20 20"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd"
                                        d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
                                        clip-rule="evenodd" />
                                </svg>
                            </a>
                        </li>
                        <li>
                            <a href="#"
                                class="flex items-center justify-center text-sm py-2 px-3 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">1</a>
                        </li>
                        <li>
                            <a href="#"
                                class="flex items-center justify-center text-sm py-2 px-3 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">2</a>
                        </li>
                        <li>
                            <a href="#" aria-current="page"
                                class="flex items-center justify-center text-sm z-10 py-2 px-3 leading-tight text-primary-600 bg-primary-50 border border-primary-300 hover:bg-primary-100 hover:text-primary-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white">3</a>
                        </li>
                        <li>
                            <a href="#"
                                class="flex items-center justify-center text-sm py-2 px-3 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">...</a>
                        </li>
                        <li>
                            <a href="#"
                                class="flex items-center justify-center text-sm py-2 px-3 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">100</a>
                        </li>
                        <li>
                            <a href="#"
                                class="flex items-center justify-center h-full py-1.5 px-3 leading-tight text-gray-500 bg-white rounded-r-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                                <span class="sr-only">Next</span>
                                <svg class="w-5 h-5" aria-hidden="true" fill="currentColor" viewbox="0 0 20 20"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd"
                                        d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                                        clip-rule="evenodd" />
                                </svg>
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
        </section>
    </template>
</template>