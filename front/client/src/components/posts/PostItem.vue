<template>
    <tr>
    <td>
      <a :href="post.vk_link">{{ post.author }}</a>
        <p v-if="post.bet != 'null'">{{post.bet}}</p>
        <p v-if="post.coef != 'null'">{{post.coef}}</p>
      <div v-if="post.bet == 'null' && post.type == 1">
        <label-edit :text="betChange.bet" id="labeledit2" v-on:text-updated-blur="betUpdated" placeholder="click to enter bet"></label-edit>

        <button
        class = "btn btn-success btn-sm"
        @click="betupdate(post.id)"
        >enter bet</button>
      </div>
      <div v-if="post.coef == 'null' && post.type == 1">
        <label-edit :text="coefChange.coef" id="labeledit1" v-on:text-updated-blur="coefUpdated" placeholder="click to enter coef"></label-edit>

        <button
        class = "btn btn-success btn-sm"
        @click="coefupdate(post.id)"
        >enter coef</button>
      </div>
    </td>
    <td>
      {{ post.content }}
      <br />
      <img
        v-if="post.attachment_link != ''"
        v-bind:src="post.attachment_link"
        class="img-fluid"
        style="max-width: 320px; max-height:240px;"
      />
      <hr>
      

    <span v-if="title == 'bets'">
      <button
        v-if="post.zahod == 0 && post.game != 0"
        type="button"
        class="btn btn-success btn-sm"
        @click="changePostType(post.id, 'win')"
      >
        win
      </button>
      <button
        v-if="post.zahod == 0 && post.game != 0"
        type="button"
        class="btn btn-danger btn-sm ml-1"
        @click="changePostType(post.id, 'lose')"
      >
        lose
      </button>
      <span>
        <button
          v-if="post.game == 0"
          type="button"
          class="btn btn-danger btn-sm"
          @click="changeGameType(post.id, 'dota')"
        >
          dota
        </button>
        <button
          v-if="post.game == 0"
          type="button"
          class="btn btn-danger btn-sm ml-1"
          @click="changeGameType(post.id, 'csgo')"
        >
          csgo
        </button>
      </span>
    </span>
    <span v-if="title == 'trash'">
      <button
        v-if="post.type == 0"
        type="button"
        class="btn btn-danger btn-sm"
        @click="changePostType(post.id, 'post')"
      >
        post
      </button>
      <button
        v-if="post.type == 0"
        type="button"
        class="btn btn-warning btn-sm ml-1"
        @click="changePostType(post.id, 'bet')"
      >
        bet
      </button>
      <!-- {{ post.type }} -->
    </span>
    <span v-if="post.hltv_link == 'null' && post.type == '1' && game_type == 'csgo'" class="float-md-right">
      <button
        type="button"
        class="btn btn-info btn-sm ml-1"
        v-b-modal.hltv-modal
        @click="hltvform(post.id)"
      >
      hltv 
      </button>
    </span>
    <!-- <span v-else-if="post.hltv_link != 'null'">
      <a :href="post.hltv_link">hltv</a>
    </span> -->

    </td>
    <td>{{ post.time }}</td>
    <td>
    <!-- Картинка для ставки которая выиграла -->
    <div v-if="title == 'bets'">
      <svg
        v-if="post.zahod == '1'"
        class="bi bi-plus-square"
        width="2em"
        height="2em"
        viewBox="0 0 16 16"
        fill="green"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          fill-rule="evenodd"
          d="M8 3.5a.5.5 0 01.5.5v4a.5.5 0 01-.5.5H4a.5.5 0 010-1h3.5V4a.5.5 0 01.5-.5z"
          clip-rule="evenodd"
        />
        <path
          fill-rule="evenodd"
          d="M7.5 8a.5.5 0 01.5-.5h4a.5.5 0 010 1H8.5V12a.5.5 0 01-1 0V8z"
          clip-rule="evenodd"
        />
        <path
          fill-rule="evenodd"
          d="M14 1H2a1 1 0 00-1 1v12a1 1 0 001 1h12a1 1 0 001-1V2a1 1 0 00-1-1zM2 0a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V2a2 2 0 00-2-2H2z"
          clip-rule="evenodd"
        />
      </svg>

      <!-- Картинка для ставки которая проиграла -->
      <svg
        v-if="post.zahod == '2'"
        class="bi bi-x-circle"
        width="2em"
        height="2em"
        viewBox="0 0 16 16"
        fill="red"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          fill-rule="evenodd"
          d="M8 15A7 7 0 108 1a7 7 0 000 14zm0 1A8 8 0 108 0a8 8 0 000 16z"
          clip-rule="evenodd"
        />
        <path
          fill-rule="evenodd"
          d="M11.854 4.146a.5.5 0 010 .708l-7 7a.5.5 0 01-.708-.708l7-7a.5.5 0 01.708 0z"
          clip-rule="evenodd"
        />
        <path
          fill-rule="evenodd"
          d="M4.146 4.146a.5.5 0 000 .708l7 7a.5.5 0 00.708-.708l-7-7a.5.5 0 00-.708 0z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    
    <div v-if="post.hltv_link != 'null'">
      <a :href="post.hltv_link">hltv</a>
    </div>
    <!-- <td>{{ post.zahod }}</td> -->

    </td>
    </tr>
</template>

<script>
import axios from 'axios';
import LabelEdit from 'label-edit';
export default {
  props: {
    post: {
      type: Object,
      required: true,
    },
    title:{},
    game_type:{},
    getPostsType: {},
    game_type: {},
  },
  data () {
    return {
      coefChange: {
        coef: '',
        id: '',
      },
      betChange: {
        bet: '',
        id: '',
      }
    }
  },
  methods: {
    // isInt(n) {
    //   return Number(n) === n && n % 1 == 0; 
    // },
    initForm(){
      this.coefChange.coef='';
      this.coefChange.id='';
      this.betChange.bet='';
      this.betChange.id='';
    },
    coefUpdated: function(text){
      this.coefChange.coef = text;
    },
    betUpdated: function(text){
      this.betChange.bet = text;
    },
    coefupdate(id) { 
      this.coefChange.id = id;
      if (this.coefChange.coef != ''){
        console.log(parseFloat(this.coefChange.coef))
        const qwe = parseFloat(this.coefChange.coef)
        if (!isNaN(qwe)){
          console.log('asdded')
          const payload = {
            post_id: this.coefChange.id,
            coef: this.coefChange.coef,
          }
          this.addCoef(payload)
        }
      }
      else {
        console.log("empty coef")
      }
      this.initForm()
    },
    betupdate(id) { 
      this.betChange.id = id;
      if (this.betChange.bet != ''){
        if (Number.isSafeInteger(parseInt(this.betChange.bet)) == true){
          console.log(this.betChange.bet)
          const payload = {
            post_id: this.betChange.id,
            amount: this.betChange.bet,
          }
          this.addBetAmount(payload)
        }
      }
      else {
        console.log("err with bet")
      }
      this.initForm()
    },
    addBetAmount(payload) {
      const path = 'http://127.0.0.1:5000/posts/bet/amount'
      axios
        .post(path, payload)
        .then(() => {
          if (this.game_type == ''){
          this.getPostsType("bets")
          }
          else {
            this.getPostsType(this.game_type)
          }
        })
        .catch((error) => {
          console.log(error);
          this.getPostsType("trash");
        })
    },
    addCoef(payload) {
      const path = 'http://127.0.0.1:5000/posts/bet/coef'
      axios
        .post(path, payload)
        .then(() => {
          if (this.game_type == ''){
          this.getPostsType("bets")
          }
          else {
            this.getPostsType(this.game_type)
          }
        })
        .catch((error) => {
          console.log(error);
          this.getPostsType("trash");
        })
    },
    changeGameType(postID, type) {
      const path = `http://127.0.0.1:5000/posts/bet/${type}/${postID}`;
      axios
        .get(path)
        .then(() => {
          this.getPostsType("bets");
        })
        .catch((error) => {
          console.log(error);
          this.getPostsType("bets");
        });
    },
    
    changePostType(postID, type) {
      const path = `http://127.0.0.1:5000/posts/${type}/${postID}`;
      axios
        .get(path)
        .then(() => {
          if (type == "post" || type == "bet"){
            this.getPostsType("trash");
          }
          else if (type == "win" || type == "lose" ) {
            this.getPostsType("bets");
          }
        })
        .catch((error) => {
          console.log(error);
          this.getPostsType("trash");
        });
    },
  },
  components:{
    LabelEdit,
  },
}
</script>