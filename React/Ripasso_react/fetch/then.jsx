import { useEffect, useState } from "react";

export default function App() {
  const [post, setPost] = useState(null);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts/1")
      .then(res => res.json())
      .then(data => {
        setPost(data); // aggiorno lo stato
      });
  }, []); // eseguito solo una volta

  return (
    <div>
      <h1>Fetch con .then()</h1>

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
