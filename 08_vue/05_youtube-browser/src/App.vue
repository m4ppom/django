<template>
<!-- HTML -->
    <div class="container">
        <SearchBar @inputChange="onInputChange"></SearchBar>
        <!-- <button @click="doSomething">aa</button>
        자식 컴포넌트에서 emit하는 이벤트 이름. -->
        <div class="row">
            <VideoDetail :video="selectedVideo"></VideoDetail>

            <VideoList :videos="videos" @videoSelect="onVideoSelect"> </VideoList>
        <!-- v-bind: 줄여서 : -->
        </div>
    </div>
</template>

<script>
    import SearchBar from './components/SearchBar';
    import axios from 'axios';
    import VideoList from './components/VideoList';
    import VideoDetail from './components/videoDetail';

    const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY;

    export default {
        // component 만들면 
        // 이름적기 0)
        name: 'App',
        components: {
            SearchBar,
            VideoList,
            VideoDetail,
        },
        data() {
            return {
                videos: [],
                selectedVideo: null,
            }
        },
        methods: {
            onInputChange (inputValue) {
                // console.log(inputValue)
                axios.get('https://www.googleapis.com/youtube/v3/search', {
                    params: {
                        key: API_KEY,
                        type: 'video',
                        part: 'snippet',
                        q: inputValue
                    }
                })
                .then(res => this.videos = res.data.items)
            },
            onVideoSelect (video) {
                this.selectedVideo = video;
            }
        },
    }
</script>

<style>
    
</style>