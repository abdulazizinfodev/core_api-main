<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'
import { defineComponent } from 'vue'
export default defineComponent({
    data() {
        return {
            loading: true,
            modeuls: [],
            videos: [],
        };
    },

    mounted() {
        this.getModuls()
        this.getFeed()
    },

    methods: {
        getModuls() {
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': `JWT ${localStorage.getItem('user.access')}`,
                }
            };
            axios
                .get('/api/videos/moduls/', config)
                .then(response => {
                    console.log(response.data)
                    this.modeuls = response.data['moduls']
                    this.loading = false
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
        getFeed() {
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': `JWT ${localStorage.getItem('user.access')}`,
                }
            };
            axios
                .get('/api/videos/', config)
                .then(response => {
                    console.log(response.data)
                    this.videos = response.data['videos']
                    this.loading = false
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
    }
})
</script>


<template>
    <div class="pr-2 pb-2" v-if="loading">
        <section class="bg-white dark:bg-gray-900">
            <div class="py-3 px-1 mx-1 w-full">
                <div class="grid gap-3 mb-6 md:grid-cols-5">
                    <div role="status" class="max-w-sm p-3 border border-gray-100 rounded shadow animate-pulse md:p-3">
                        <div class="flex items-center justify-center h-36 w-38 mb-4 bg-gray-300 rounded">
                            <svg class="w-10 h-10 text-gray-200 dark:text-gray-600" aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 20">
                                <path
                                    d="M14.066 0H7v5a2 2 0 0 1-2 2H0v11a1.97 1.97 0 0 0 1.934 2h12.132A1.97 1.97 0 0 0 16 18V2a1.97 1.97 0 0 0-1.934-2ZM10.5 6a1.5 1.5 0 1 1 0 2.999A1.5 1.5 0 0 1 10.5 6Zm2.221 10.515a1 1 0 0 1-.858.485h-8a1 1 0 0 1-.9-1.43L5.6 10.039a.978.978 0 0 1 .936-.57 1 1 0 0 1 .9.632l1.181 2.981.541-1a.945.945 0 0 1 .883-.522 1 1 0 0 1 .879.529l1.832 3.438a1 1 0 0 1-.031.988Z" />
                                <path d="M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.98 2.98 0 0 0 .13 5H5Z" />
                            </svg>
                        </div>
                        <div class="h-2.5 bg-gray-200 rounded-full w-28 mb-4"></div>
                        <div class="h-2 bg-gray-200 rounded-full mb-2.5"></div>
                        <div class="h-2 bg-gray-200 rounded-full mb-2.5"></div>
                        <div class="h-2 bg-gray-200 rounded-full"></div>
                        <div class="flex items-center mt-4 space-x-3">
                            <svg class="w-10 h-10 text-gray-200 dark:text-gray-700" aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                <path
                                    d="M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z" />
                            </svg>
                            <div>
                                <div class="h-2.5 bg-gray-200 rounded-full w-28 mb-2"></div>
                                <div class="w-28 h-2 bg-gray-200 rounded-full"></div>
                            </div>
                        </div>
                        <span class="sr-only">Loading...</span>
                    </div>
                    <div role="status" class="max-w-sm p-3 border border-gray-100 rounded shadow animate-pulse md:p-3">
                        <div class="flex items-center justify-center h-36 w-38 mb-4 bg-gray-300 rounded">
                            <svg class="w-10 h-10 text-gray-200 dark:text-gray-600" aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 20">
                                <path
                                    d="M14.066 0H7v5a2 2 0 0 1-2 2H0v11a1.97 1.97 0 0 0 1.934 2h12.132A1.97 1.97 0 0 0 16 18V2a1.97 1.97 0 0 0-1.934-2ZM10.5 6a1.5 1.5 0 1 1 0 2.999A1.5 1.5 0 0 1 10.5 6Zm2.221 10.515a1 1 0 0 1-.858.485h-8a1 1 0 0 1-.9-1.43L5.6 10.039a.978.978 0 0 1 .936-.57 1 1 0 0 1 .9.632l1.181 2.981.541-1a.945.945 0 0 1 .883-.522 1 1 0 0 1 .879.529l1.832 3.438a1 1 0 0 1-.031.988Z" />
                                <path d="M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.98 2.98 0 0 0 .13 5H5Z" />
                            </svg>
                        </div>
                        <div class="h-2.5 bg-gray-200 rounded-full w-28 mb-4"></div>
                        <div class="h-2 bg-gray-200 rounded-full mb-2.5"></div>
                        <div class="h-2 bg-gray-200 rounded-full mb-2.5"></div>
                        <div class="h-2 bg-gray-200 rounded-full"></div>
                        <div class="flex items-center mt-4 space-x-3">
                            <svg class="w-10 h-10 text-gray-200 dark:text-gray-700" aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                <path
                                    d="M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z" />
                            </svg>
                            <div>
                                <div class="h-2.5 bg-gray-200 rounded-full w-28 mb-2"></div>
                                <div class="w-28 h-2 bg-gray-200 rounded-full"></div>
                            </div>
                        </div>
                        <span class="sr-only">Loading...</span>
                    </div>
                    <div role="status" class="max-w-sm p-3 border border-gray-100 rounded shadow animate-pulse md:p-3">
                        <div class="flex items-center justify-center h-36 w-38 mb-4 bg-gray-300 rounded">
                            <svg class="w-10 h-10 text-gray-200 dark:text-gray-600" aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 20">
                                <path
                                    d="M14.066 0H7v5a2 2 0 0 1-2 2H0v11a1.97 1.97 0 0 0 1.934 2h12.132A1.97 1.97 0 0 0 16 18V2a1.97 1.97 0 0 0-1.934-2ZM10.5 6a1.5 1.5 0 1 1 0 2.999A1.5 1.5 0 0 1 10.5 6Zm2.221 10.515a1 1 0 0 1-.858.485h-8a1 1 0 0 1-.9-1.43L5.6 10.039a.978.978 0 0 1 .936-.57 1 1 0 0 1 .9.632l1.181 2.981.541-1a.945.945 0 0 1 .883-.522 1 1 0 0 1 .879.529l1.832 3.438a1 1 0 0 1-.031.988Z" />
                                <path d="M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.98 2.98 0 0 0 .13 5H5Z" />
                            </svg>
                        </div>
                        <div class="h-2.5 bg-gray-200 rounded-full w-28 mb-4"></div>
                        <div class="h-2 bg-gray-200 rounded-full mb-2.5"></div>
                        <div class="h-2 bg-gray-200 rounded-full mb-2.5"></div>
                        <div class="h-2 bg-gray-200 rounded-full"></div>
                        <div class="flex items-center mt-4 space-x-3">
                            <svg class="w-10 h-10 text-gray-200 dark:text-gray-700" aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                <path
                                    d="M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z" />
                            </svg>
                            <div>
                                <div class="h-2.5 bg-gray-200 rounded-full w-28 mb-2"></div>
                                <div class="w-28 h-2 bg-gray-200 rounded-full"></div>
                            </div>
                        </div>
                        <span class="sr-only">Loading...</span>
                    </div>
                    <div role="status" class="max-w-sm p-3 border border-gray-100 rounded shadow animate-pulse md:p-3">
                        <div class="flex items-center justify-center h-36 w-38 mb-4 bg-gray-300 rounded">
                            <svg class="w-10 h-10 text-gray-200 dark:text-gray-600" aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 20">
                                <path
                                    d="M14.066 0H7v5a2 2 0 0 1-2 2H0v11a1.97 1.97 0 0 0 1.934 2h12.132A1.97 1.97 0 0 0 16 18V2a1.97 1.97 0 0 0-1.934-2ZM10.5 6a1.5 1.5 0 1 1 0 2.999A1.5 1.5 0 0 1 10.5 6Zm2.221 10.515a1 1 0 0 1-.858.485h-8a1 1 0 0 1-.9-1.43L5.6 10.039a.978.978 0 0 1 .936-.57 1 1 0 0 1 .9.632l1.181 2.981.541-1a.945.945 0 0 1 .883-.522 1 1 0 0 1 .879.529l1.832 3.438a1 1 0 0 1-.031.988Z" />
                                <path d="M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.98 2.98 0 0 0 .13 5H5Z" />
                            </svg>
                        </div>
                        <div class="h-2.5 bg-gray-200 rounded-full w-28 mb-4"></div>
                        <div class="h-2 bg-gray-200 rounded-full mb-2.5"></div>
                        <div class="h-2 bg-gray-200 rounded-full mb-2.5"></div>
                        <div class="h-2 bg-gray-200 rounded-full"></div>
                        <div class="flex items-center mt-4 space-x-3">
                            <svg class="w-10 h-10 text-gray-200 dark:text-gray-700" aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                <path
                                    d="M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z" />
                            </svg>
                            <div>
                                <div class="h-2.5 bg-gray-200 rounded-full w-28 mb-2"></div>
                                <div class="w-28 h-2 bg-gray-200 rounded-full"></div>
                            </div>
                        </div>
                        <span class="sr-only">Loading...</span>
                    </div>
                    <div role="status" class="max-w-sm p-3 border border-gray-100 rounded shadow animate-pulse md:p-3">
                        <div class="flex items-center justify-center h-36 w-38 mb-4 bg-gray-300 rounded">
                            <svg class="w-10 h-10 text-gray-200 dark:text-gray-600" aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 20">
                                <path
                                    d="M14.066 0H7v5a2 2 0 0 1-2 2H0v11a1.97 1.97 0 0 0 1.934 2h12.132A1.97 1.97 0 0 0 16 18V2a1.97 1.97 0 0 0-1.934-2ZM10.5 6a1.5 1.5 0 1 1 0 2.999A1.5 1.5 0 0 1 10.5 6Zm2.221 10.515a1 1 0 0 1-.858.485h-8a1 1 0 0 1-.9-1.43L5.6 10.039a.978.978 0 0 1 .936-.57 1 1 0 0 1 .9.632l1.181 2.981.541-1a.945.945 0 0 1 .883-.522 1 1 0 0 1 .879.529l1.832 3.438a1 1 0 0 1-.031.988Z" />
                                <path d="M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.98 2.98 0 0 0 .13 5H5Z" />
                            </svg>
                        </div>
                        <div class="h-2.5 bg-gray-200 rounded-full w-28 mb-4"></div>
                        <div class="h-2 bg-gray-200 rounded-full mb-2.5"></div>
                        <div class="h-2 bg-gray-200 rounded-full mb-2.5"></div>
                        <div class="h-2 bg-gray-200 rounded-full"></div>
                        <div class="flex items-center mt-4 space-x-3">
                            <svg class="w-10 h-10 text-gray-200 dark:text-gray-700" aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                <path
                                    d="M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z" />
                            </svg>
                            <div>
                                <div class="h-2.5 bg-gray-200 rounded-full w-28 mb-2"></div>
                                <div class="w-28 h-2 bg-gray-200 rounded-full"></div>
                            </div>
                        </div>
                        <span class="sr-only">Loading...</span>
                    </div>
                    <div role="status" class="max-w-sm p-3 border border-gray-100 rounded shadow animate-pulse md:p-3">
                        <div class="flex items-center justify-center h-36 w-38 mb-4 bg-gray-300 rounded">
                            <svg class="w-10 h-10 text-gray-200 dark:text-gray-600" aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 20">
                                <path
                                    d="M14.066 0H7v5a2 2 0 0 1-2 2H0v11a1.97 1.97 0 0 0 1.934 2h12.132A1.97 1.97 0 0 0 16 18V2a1.97 1.97 0 0 0-1.934-2ZM10.5 6a1.5 1.5 0 1 1 0 2.999A1.5 1.5 0 0 1 10.5 6Zm2.221 10.515a1 1 0 0 1-.858.485h-8a1 1 0 0 1-.9-1.43L5.6 10.039a.978.978 0 0 1 .936-.57 1 1 0 0 1 .9.632l1.181 2.981.541-1a.945.945 0 0 1 .883-.522 1 1 0 0 1 .879.529l1.832 3.438a1 1 0 0 1-.031.988Z" />
                                <path d="M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.98 2.98 0 0 0 .13 5H5Z" />
                            </svg>
                        </div>
                        <div class="h-2.5 bg-gray-200 rounded-full w-28 mb-4"></div>
                        <div class="h-2 bg-gray-200 rounded-full mb-2.5"></div>
                        <div class="h-2 bg-gray-200 rounded-full mb-2.5"></div>
                        <div class="h-2 bg-gray-200 rounded-full"></div>
                        <div class="flex items-center mt-4 space-x-3">
                            <svg class="w-10 h-10 text-gray-200 dark:text-gray-700" aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                <path
                                    d="M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z" />
                            </svg>
                            <div>
                                <div class="h-2.5 bg-gray-200 rounded-full w-28 mb-2"></div>
                                <div class="w-28 h-2 bg-gray-200 rounded-full"></div>
                            </div>
                        </div>
                        <span class="sr-only">Loading...</span>
                    </div>
                </div>
            </div>
        </section>
    </div>
    <section class="bg-gray-800 ml-4 mr-4">
        <div class="max-w-screen-xl px-4 py-8 mx-auto text-center lg:py-16 lg:px-6">
            <figure class="max-w-screen-md mx-auto">
                <svg class="h-12 mx-auto mb-3 text-gray-400" viewBox="0 0 24 27" fill="none"
                    xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M14.017 18L14.017 10.609C14.017 4.905 17.748 1.039 23 0L23.995 2.151C21.563 3.068 20 5.789 20 8H24V18H14.017ZM0 18V10.609C0 4.905 3.748 1.038 9 0L9.996 2.151C7.563 3.068 6 5.789 6 8H9.983L9.983 18L0 18Z"
                        fill="currentColor" />
                </svg>
                <blockquote>
                    <p class="text-2xl font-medium text-gray-100">"Flowbite is just awesome. It contains
                        tons of predesigned components and pages starting from login screen to complex dashboard. Perfect
                        choice for your next SaaS application."</p>
                </blockquote>
                <figcaption class="flex items-center justify-center mt-6 space-x-3">
                    <img class="w-6 h-6 rounded-full"
                        src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/michael-gouch.png"
                        alt="profile picture">
                    <div class="flex items-center divide-x-2 divide-gray-500">
                        <div class="pr-3 font-medium text-gray-100">Micheal Gough</div>
                        <div class="pl-3 text-sm font-light text-gray-300">CEO at Google</div>
                    </div>
                </figcaption>
            </figure>
        </div>
    </section>
</template>

