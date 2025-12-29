const Post = ({ title, body }) => {
  return (
    <div>
      <h2>{title}</h2>
      <p>{body}</p>
    </div>
  );
};

//--------------------

const App = () => {
  const posts = [
    { id: 1, title: "Post 1", body: "Contenuto 1" },
    { id: 2, title: "Post 2", body: "Contenuto 2" }
  ];

  return (
    <div>
      {posts.map(post => (
        <Post key={post.id} title={post.title} body={post.body} />
      ))}
    </div>
  );
};

export default App;
