function attachEvents() {
  let btnLoadPosts = document.getElementById("btnLoadPosts");
  let postsSelectHTML = document.getElementById("posts");
  let btnViewPost = document.getElementById("btnViewPost");
  let postTitleHTML = document.getElementById("post-title");
  let postBodyHTML = document.getElementById("post-body");
  let postCommentsUlHTML = document.getElementById("post-comments");

  btnLoadPosts.addEventListener("click", loadHandler);
  btnViewPost.addEventListener("click", vewPostsHandler);

  const BASE_URL = "http://localhost:3030/jsonstore/blog/";

  function loadHandler(e) {
    postsSelectHTML.innerHTML = "";

    fetch(BASE_URL + "posts")
      .then((response) => response.json())
      .then((result) => {
        let posts = Object.values(result);

        for (const post of posts) {
          let id = post.id;
          let body = post.body;
          let title = post.title;

          // console.log(id, title, body)

          let newOptionHTML = document.createElement("option");
          newOptionHTML.value = id;
          newOptionHTML.textContent = title;

          postsSelectHTML.appendChild(newOptionHTML);
        }
      });
  }

  function vewPostsHandler(e) {
    postCommentsUlHTML.innerHTML = "";

    let selectedOption = postsSelectHTML.value;
    let title = "";
    let body = "";

    fetch(BASE_URL + "posts/" + selectedOption)
      .then((response) => response.json())
      .then((result) => {
        body = result.body;
        title = result.title;

        // console.log(body);
        // console.log(title);

        postBodyHTML.textContent = body;
        postTitleHTML.textContent = title;
      });

    fetch(BASE_URL + "comments")
      .then((response) => response.json())
      .then((result) => Object.values(result))
      .then((comments) => {
        for (const comment of comments) {
          if (comment.postId === selectedOption) {
            newLiHTML = document.createElement("li");
            newLiHTML.textContent = comment.text;
            postCommentsUlHTML.appendChild(newLiHTML);
          }
        }
      });
  }
}

attachEvents();
