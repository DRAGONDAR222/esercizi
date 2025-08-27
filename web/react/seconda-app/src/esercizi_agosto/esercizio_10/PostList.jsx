import React from 'react';

const PostList = ({ posts }) => {
    return (
        <div className="mt-3">
            {posts.map((post, index) => (
                <div key={index} className="mb-3">
                    <h5 className="fw-bold">{post.titolo}</h5>
                    <p>{post.contenuto}</p>
                    <hr />
                </div>
            ))}
        </div>
    );
};

export default PostList;
