import React, { useState } from 'react';

const PostForm = ({ aggiungiPost }) => {
    const [formData, setFormData] = useState({
        titolo: '',
        contenuto: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: value
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        aggiungiPost(formData);
        setFormData({ titolo: '', contenuto: '' });
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className="mb-2">
                <label className="form-label">Titolo</label>
                <input
                    type="text"
                    className="form-control"
                    id="titolo"
                    name="titolo"
                    value={formData.titolo}
                    onChange={handleChange}
                />
            </div>
            <div className="mb-2">
                <label className="form-label">Contenuto</label>
                <textarea
                    className="form-control"
                    id="contenuto"
                    name="contenuto"
                    rows="3"
                    value={formData.contenuto}
                    onChange={handleChange}
                ></textarea>
            </div>
            <button type="submit" className="btn btn-primary">Invia</button>
        </form>
    );
};

export default PostForm;
