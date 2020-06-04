<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>{{ title }}</h1>
        <div>

          <a href="#" @click="getPostsType('posts')">posts</a>
          <a class="ml-1" href="#" @click="getPostsType('bets')">bets</a>
          <a class="ml-1" href="#" @click="getPostsType('trash')">ALL POSTs</a>
        </div>
        <hr />
        <div v-if="title == 'bets'">
          <a href="#" @click="getPostsType('csgo', false)">csgo</a>
          <a class="ml-1" href="#" @click="getPostsType('dota', false)">dota 2</a>
        </div>
        <br />
        <br />
        <div class="table-responsive">
          <table class="table">
            <thead>
              <tr>
                <th scope="col">author</th>
                <th scope="col">content</th>
                <th scope="col">time</th>
                <th scope="col">other</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="post in posts" v-bind:key="post.time">
                <td>
                  <a :href="post.vk_link">{{ post.author }}</a><br><p v-if="post.bet != 'null'">{{post.bet}}</p>
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
                    class="btn btn-warning btn-sm"
                    @click="changePostType(post.id, 'win')"
                  >
                    win
                  </button>
                  <button
                    v-if="post.zahod == 0 && post.game != 0"
                    type="button"
                    class="btn btn-danger btn-sm ml-1"
                    @click="changeBetType(post.id, 'lose')"
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

                <span v-if="post.type == '1' && post.bet == 'null'" class="float-md-right">

                  <button
                    type="button"
                    class="btn btn-info btn-sm"
                    v-b-modal.addbet-modal
                    @click="betamountform(post.id)"
                  >
                  bet
                  </button>

                </span>
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
            </tbody>
          </table>
        </div>
        </div>
      </div>

    <b-modal ref="addHltvLinkModal" id="hltv-modal" title="Add hltv link" hide-footer>
      <b-form @submit="onSubmitHltvLink" @reset="onResetHltvLink" class="w-100">
        <b-form-group id="form-title-group" label="Link:" label-for="form-link-input">
          <b-form-input
            id="form-link-input"
            type="text"
            v-model="addHltvLinkForm.link"
            required
            placeholder="Enter link"
          >
          </b-form-input>
          <b-form-input
            id="form-postid-input"
            class="invisible"
            type="text"
            v-model="addHltvLinkForm.postid"
          >
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

    <b-modal ref="addBetAmountModal" id="addbet-modal" title="add bet amount" hide-footer>
      <b-form @submit="onSubmitBetAmount" @reset="onResetBetAmount" class="w-100">
        <b-form-group id="form-title-group" label="Bet amount:" label-for="form-bet-input">
          <b-form-input
            id="form-betamount-input"
            type="text"
            v-model="addBetAmountForm.amount"
            required
            placeholder="Enter Amount"
          >
          </b-form-input>
          <b-form-input
            id="form-postid-input"
            class="invisible"
            type="text"
            v-model="addBetAmountForm.postid"
          >
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  <!-- </div> -->
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      title: '',
      game_type: '',
      posts: [],
      addHltvLinkForm: {
        postid: '',
        link: '',
      },
      addBetAmountForm: {
        postid: '',
        amount: '',
      },
    };
  },
  methods: {
    initForm() {
      this.addHltvLinkForm.link = '';
      this.addHltvLinkForm.postid = '';
      this.addBetAmountForm.postid = '';
      this.addBetAmountForm.amount = '';
    },
    hltvform(postid) {
      this.addHltvLinkForm.postid = postid;
    },
    betamountform(postid) {
      this.addBetAmountForm.postid = postid;
    },
    onSubmitBetAmount(evt) {
      evt.preventDefault();
      this.$refs.addBetAmountModal.hide()
      const payload = {
        post_id: this.addBetAmountForm.postid,
        amount: this.addBetAmountForm.amount,
      }
      this.addBetAmount(payload);
      this.initForm();
    },
    addBetAmount(payload) {
      const path = 'http://127.0.0.1:5000/posts/bet/amount'
      axios
        .post(path, payload)
        .then(() => {
          this.getPostsType("bets")
        })
        .catch((error) => {
          console.log(error);
          this.getPostsType("trash");
        })
    },
    onSubmitHltvLink(evt) {
      evt.preventDefault();
      this.$refs.addHltvLinkModal.hide();
      const payload = {
        post_id: this.addHltvLinkForm.postid,
        hltv_link: this.addHltvLinkForm.link
      };
      this.addLink(payload);
      this.initForm();
    },
    addLink(payload) {
      const path = "http://127.0.0.1:5000/posts/bet/csgo/hltv";
      axios
        .post(path, payload)
        .then(() => {
          this.getPostsType("csgo");
        })
        .catch((error) => {
          console.log(error);
          this.getPostsType("trash");
        });
    },
    onResetBetAmount(evt) {
      evt.preventDefault();
      this.$refs.addBetAmountModal.hide();
      this.initForm();
    },
    onResetHltvLink(evt) {
      evt.preventDefault();
      this.$refs.addHltvLinkModal.hide();
      this.initForm();
    },
    getPostsType(type, changetype = true) {
      const path = `http://127.0.0.1:5000/${type}`;
      axios
        .get(path)
        .then(res => {
          if (changetype == true) {
            this.title = type;
          }
          if (type == "dota" || type == "csgo") {
            this.game_type = type;
            this.title = 'bets'
          }
          else {
            this.game_type = '';
          }
          this.posts = res.data.posts;
          console.log(path);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    changeGameType(postID, type) {
      const path = `http://127.0.0.1:5000/posts/bet/${type}/${postID}`;
      axios
        .get(path)
        .then(() => {
          this.getPostsType("bets");
        })
        .catch((error) => {
          console.error(error);
          this.getPostsType("bets");
        });
    },
    changePostType(postID, type) {
      const path = `http://127.0.0.1:5000/posts/${type}/${postID}`;
      axios
        .get(path)
        .then(() => {
          this.getPostsType("trash");
        })
        .catch((error) => {
          console.error(error);
          this.getPostsType("trash");
        });
    },
    changeBetType(postID, type) {
      const path = `http://127.0.0.1:5000/posts/${type}/${postID}`;
      axios
        .get(path)
        .then(() => {
          this.getPostsType("bets");
        })
        .catch((error) => {
          console.error(error);
          this.getPostsType("bets");
        });
    },
  },
  created() {
    this.getPostsType("trash");
    this.title = "trash";
  }
};
</script>
