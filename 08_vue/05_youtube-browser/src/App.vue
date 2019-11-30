<template>
    <div class="container">
        <!-- step 3. template 에 보여주기 -->
        <SearchBar @inputChange="onInputChange"></SearchBar>
        <!-- v-on:[자식cpmnt에서 emit하는 이벤트 이름]="" -->

        <div class="row">
            <VideoDetail :video="selectedVideo"></VideoDetail>

            <!-- 'v-bind:' 는 줄여서 ':' -->
            <!-- props 쓰기: step0. bind 로 데이터를 넘긴다. -->
            <VideoList 
                :videos="videos"
                @videoSelect="onVideoSelect"
            >
            </VideoList>
        </div>
        
    </div>
</template>

<script>
    import SearchBar from './components/SearchBar';  // step 1. import
    import VideoList from './components/VideoList';
    import VideoDetail from './components/VideoDetail';

    import axios from 'axios';

    const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY;

    export default {
        // 컴포넌트 만들면
        // 0. 이름 적기
        name: 'App',
        components: {
            SearchBar,  // step 2. 부모에게 자식들 등록하기
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
                axios.get('https://www.googleapis.com/youtube/v3/search', {
                    params: {
                        key: API_KEY,
                        type: 'video',
                        part: 'snippet',
                        q: inputValue,
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