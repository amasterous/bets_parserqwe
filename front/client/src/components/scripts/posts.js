
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

      addCoefForm: {
        postid: '',
        coef: '',
      }
    };
  },

  methods: {
    initForm() {
      this.addHltvLinkForm.link = '';
      this.addHltvLinkForm.postid = '';
      this.addBetAmountForm.postid = '';
      this.addBetAmountForm.amount = '';
      this.addCoefForm.postid = '';
      this.addCoefForm.coef = '';
    },

    hltvform(postid) {
      this.addHltvLinkForm.postid = postid;
    },

    betamountform(postid) {
      this.addBetAmountForm.postid = postid;
    },

    addcoefform(postid) {
      this.addCoefForm.postid = postid;
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

    onSubmitAddCoef(evt) {
      evt.preventDefault();
      this.$refs.addCoefModal.hide()
      const payload = {
        post_id: this.addCoefForm.postid,
        coef: this.addCoefForm.coef,
      }
      this.addCoef(payload);
      this.initForm();
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

    addCoef(payload) {
      const path = 'http://127.0.0.1:5000/posts/bet/coef'
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

    onResetAddCoef(evt) {
      evt.preventDefault();
      this.$refs.addCoefModal.hide();
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
          if (type == "post" || type == "bet"){
            this.getPostsType("trash");
          }
          else if (type == "win" || type == "lose" ) {
            this.getPostsType("bets");
          }
        })
        .catch((error) => {
          console.error(error);
          this.getPostsType("trash");
        });
    },

  },
  created() {
    this.getPostsType("trash");
    this.title = "trash";
  }
};