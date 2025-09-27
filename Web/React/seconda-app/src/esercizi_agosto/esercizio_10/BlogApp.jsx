import React from 'react'
import { useState } from 'react'
import PostForm from './PostForm';
import PostList from './PostList';

const BlogApp = () => {

    const [posts, setPosts] = useState([]);

    const aggiungiPost = (nuovoPost) => {
        setPosts(prevPosts => [...prevPosts, nuovoPost]);

    };

    return (
        <div
            className="
                container
                d-flex
                justify-content-center
                flex-column
                align-items-center
        "
        >
            <PostForm aggiungiPost={aggiungiPost} />
            <PostList posts={posts} />
        </div>
    )
}

export default BlogApp