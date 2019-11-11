<template>
    <div>
        <!-- method 내가 인자를 추가로 넘기면() 붙이고 아니면 안붙임 -->
        <!--  v-on: 을 줄여서 @로 씀 -->
       <input v-on:keypress.enter="onInput" type="text">

    </div>
</template>

<script>

export default {
    // component 만들면 
    // 이름적기 0)
    name: 'SearchBar',
    methods: {
        onInput (e) {
            // this.$emit('이벤트이름', 전송할 값)  ==> 자식컴포넌트->부모 data올려보낼때
            this.$emit('inputChange', e.target.value);
        }
    }
}
</script>

<style scoped>
/* 해당 컴포넌트의 태그들만 영향 받는다. */
    input {
        width: 75%;
    }
    div {
        text-align: center;
        margin: 20px;
    }
</style>