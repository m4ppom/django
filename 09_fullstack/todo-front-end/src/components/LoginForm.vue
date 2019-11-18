<template>
    <div class="login-form">
        <div v-if="isLoading" class="spinner-border" role="status">
            <span class="sr-only">Loading</span>
        </div>

        <form v-else class="login-input" @submit.prevent="login">
            <div v-if="errors.length" class="error-list alert alert-danger">
                <h4>아래의 오류를 해결해 주세요</h4>
                <ul>
                    <li v-for="(error, idx) in errors" :key="idx">
                        {{ error }}
                    </li>
                </ul>
            </div>
            <div class="form-group">
                <label for="username">ID</label>
                <input v-model="credentials.username" type="text" class="form-control" id="username"
                    placeholder="아이디를 입력해주세요">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input v-model="credentials.password" type="password" class="form-control" id="password"
                    placeholder="비밀번호를 입력해주세요">
            </div>
            <button class="btn btn-primary">로그인</button>
        </form>
    </div>
</template>

<script>
    const axios = require('axios');
    export default {
        name: 'LoginForm',
        data() {
            return {
                credentials: {}, // id/password 에 해당하는 data
                isAuthenticated: false, // 인증 여부
                isLoading: false,
                errors: [],
            }
        },
        methods: {
            login() {
                this.isLoading = true;
                if (this.checkUserInput()) {
                    console.log('django 서버로 데이터를 보냅니다.');
                    axios.get('http://localhost:8000', this.credentials)
                        .then(res => console.log(res))
                        .catch(err => console.error(err));
                }
                else {
                    console.log('검증실패. 다시 작성하세요.')
                    this.isLoading = false;
                }

            },
            checkUserInput() {
                this.errors = [];
                if (!this.credentials.username) this.errors.push("username 을 입력하세요.");
                if (this.credentials.password.length < 8) this.errors.push('password 는 8 자 이상이어야 합니다.');
                if (!this.errors.length) return true;
            },
        }
    }
</script>

<style>

</style>