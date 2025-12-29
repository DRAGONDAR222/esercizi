import { useEffect, useState } from "react";

export default function App() {
  const [post, setPost] = useState(null);

  useEffect(() => {
    async function fetchPost() {
      const res = await fetch("https://jsonplaceholder.typicode.com/posts/1");
      const data = await res.json();
      setPost(data);
    }

    fetchPost();
  }, []);

  return (
    <div>
      <h1>Fetch con async/await</h1>

      {post ? (
        <>
          <h2>{post.title}</h2>
          <p>{post.body}</p>
        </>
      ) : (
        <p>Caricamento...</p>
      )}
    </div>
  );
}

