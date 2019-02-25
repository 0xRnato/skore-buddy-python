<template>
<div>
    <beautiful-chat
      :participants="participants"
      :titleImageUrl="titleImageUrl"
      :onMessageWasSent="onMessageWasSent"
      :messageList="messageList"
      :newMessagesCount="newMessagesCount"
      :isOpen="isChatOpen"
      :close="closeChat"
      :open="openChat"
      :showEmoji="true"
      :showFile="true"
      :showTypingIndicator="showTypingIndicator"
      :colors="colors"
      :alwaysScrollToBottom="alwaysScrollToBottom"
      :messageStyling="messageStyling" />
  </div>
</template>

<script>
import $backend from '../backend'
import messageHistory from './messageHistory'
import chatParticipants from './chatProfiles'
import availableColors from './colors'

export default {
  name: 'ChatComponent',
  data () {
    return {
      participants: chatParticipants,
      titleImageUrl: 'https://a.slack-edge.com/66f9/img/avatars-teams/ava_0001-34.png',
      messageList: messageHistory,
      newMessagesCount: 0,
      isChatOpen: false,
      showTypingIndicator: '',
      colors: null,
      availableColors,
      chosenColor: null,
      alwaysScrollToBottom: false,
      messageStyling: true
    }
  },
  created () {
    this.colors = this.availableColors['green']
    this.chosenColor = 'green'
  },
  methods: {
    sendMessage (text) {
      console.log('sendMessage', text)
      if (text.length > 0) {
        this.newMessagesCount = this.isChatOpen ? this.newMessagesCount : this.newMessagesCount + 1
        this.onMessageWasSent({ author: 'chatbot', type: 'text', data: { text } })
      }
    },
    onMessageWasSent (message) {
      console.log('onMessageWasSent', message)
      this.messageList = [ ...this.messageList, message ]
      if (message.author === 'me') {
        $backend.fetchResponse({ text: message.data.text })
          .then((responseData) => {
            this.sendMessage({ author: 'chatbot', type: 'text', data: { text: responseData.result.fulfillment.messages[0].speech } })
          }).catch(err => console.error(err))
      }
    },
    openChat () {
      this.isChatOpen = true
      this.newMessagesCount = 0
    },
    closeChat () {
      this.isChatOpen = false
    }
  }
}
</script>

<style lang="scss">
.sc-header--img {
  max-width: 15%;
}
</style>
