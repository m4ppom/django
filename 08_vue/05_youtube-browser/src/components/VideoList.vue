<template>

    <ul class="col-lg-4 list-group">
        <VideoListItem v-for="video in videos" :key="video.etag" :video="video" @videoSelect="onVideoSelect">


        </VideoListItem>
    </ul>

        <!-- <li v-for="video in videos" :key="video.etag">
            {{ video.snippet.title }}
        </li> -->
        <!-- {{ videos.length }} -->

</template>

<script>
import VideoListItem from './VideoListItem';

export default {
    name: 'VideoList',
    // properties 넘어온다고 알려주기
    props: {
        // 배열로 써도 되고 객체로 써도됨
        videos : Array, // 유효성검사
    },
    // 여러개 넘어올수있음 prop는 data랑 똑같이 쓸 수 있음
    components: {
        VideoListItem,
    },
    methods: {
        onVideoSelect (video) {
            this.$emit('videoSelect', video)
        }
    },
}
</script>

<style>

</style>
