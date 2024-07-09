import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLogin: false,
    user: 'guest',
  },
  getters: {
    isLogin: state => state.isLogin,
    user: state => state.user
  },
  mutations: {
    userStatus (state, user) {
      state.user = user
    }
  },
  //dispatcher
  actions: {
    setUser ({commit}, user) {
      commit('userStatus', user)
    }
  }
})
