import React, { useEffect, useState } from "react";

const PostGrid = () => {
  const URL_POSTS = "https://jsonplaceholder.typicode.com/posts";
  const URL_USERS = "https://jsonplaceholder.typicode.com/users/";
  const URL_COMMENTS = "https://jsonplaceholder.typicode.com/comments";
  const [posts, setPosts] = useState([]);

async function fetchPostDetails(post) {
  try {
    const userPromise = fetch(URL_USERS + post.userId).then(resp => resp.json());
    const commentsPromise = fetch(URL_COMMENTS + "?postId=" + post.id).then(resp => resp.json());

    const [user, comments] = await Promise.all([userPromise, commentsPromise]);

    return {
      ...post,
      user: user.name, 
     
      comments: comments//.slice(0, 5) 
    };
  } catch (error) {
    console.error(`Errore nel caricamento dettagli post ${post.id}:`, error);
    return { ...post, user: 'Sconosciuto', comments: [] };
  }
}
  useEffect(() => {
    fetch(URL_POSTS)
      .then((response) => response.json())
      .then((allPosts) => {

        const postsArricchitiPromise=allPosts.map(fetchPostDetails)
        console.log(postsArricchitiPromise)
        Promise.all(postsArricchitiPromise).then(allPostsArricchiti=>setPosts(allPostsArricchiti))
        


      });
  }, []);
  return (
    <div>
      {posts.map((p) => (
        <div><p>{p.title}</p>
         <p>Nome {p.user}</p>
         </div>
      ))}
    </div>
  );
};

export default PostGrid;