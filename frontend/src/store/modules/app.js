import Cookies from 'js-cookie'
import {getLanguage} from "@/lang";
import {getChannels} from "@/api/global";

const state = {
    device: 'desktop',
    language: getLanguage(),
    document_width: document.documentElement.clientWidth,
    document_height: document.documentElement.clientHeight,
    channels: []
}

const mutations = {
    SET_LANGUAGE: (state, language) => {
        state.language = language
        Cookies.set('language', language)
    },
    TOGGLE_DEVICE: (state, device) => {
        state.device = device
    },
    SET_DOCUMENTWIDTH: (state, document_width) => {
        state.document_width = document_width
    },
    SET_DOCUMENTHEIGHT: (state, document_height) => {
        state.document_height = document_height
    },
    SET_CHANNELS: (state, channels) => {
        state.channels = channels
    }
}

const actions = {
    setLanguage({commit}, language) {
        commit('SET_LANGUAGE', language)
    },
    toggleDevice({commit}, device) {
        commit('TOGGLE_DEVICE', device)
    },
    setDocument({commit}, {document_width, document_height}) {
        commit('SET_DOCUMENTWIDTH', document_width)
        commit('SET_DOCUMENTHEIGHT', document_height)
    },
    getChannels({commit}) {
        getChannels().then(res => {
            commit('SET_CHANNELS', res)
        })
    }
}

const getters = {}

export default {
    namespaced: true,
    state,
    mutations,
    actions,
    getters
}
