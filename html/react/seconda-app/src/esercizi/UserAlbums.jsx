import React, { useEffect, useState } from 'react';

const UserAlbums = () => {
    const usersUrl = "https://jsonplaceholder.typicode.com/users";

    const [users, setUsers] = useState([]);
    const [albums, setAlbums] = useState([]);
    const [photos, setPhotos] = useState([]);
    const [selectedUser, setSelectedUser] = useState('');
    const [selectedAlbum, setSelectedAlbum] = useState('');
    const [selectedPhoto, setSelectedPhoto] = useState('');



    useEffect(() => {
        const getUsers = async () => {
            const res = await fetch(usersUrl);
            const data = await res.json();
            setUsers(data);
        };
        getUsers();
    }, []);


    useEffect(() => {
        if (!selectedUser) {
            setAlbums([]);
            return;
        }

        const getAlbums = async () => {
            const albumsUrl = `https://jsonplaceholder.typicode.com/albums?userId=${selectedUser}`;
            const res = await fetch(albumsUrl);
            const data = await res.json();
            setAlbums(data);
        };

        getAlbums();
    }, [selectedUser]);


    useEffect(() => {
        if (!selectedAlbum) {
            setPhotos([]);
            return;
        }

        const getPhotos = async () => {
            const photosUrl = `https://jsonplaceholder.typicode.com/photos?albumId=${selectedAlbum}`;
            const res = await fetch(photosUrl);
            const data = await res.json();
            setPhotos(data);
        };

        getPhotos();
    }, [selectedAlbum]);


    const handleUsersChange = (e) => {
        setSelectedUser(e.target.value);
        setSelectedAlbum('');
    };

    const handleAlbumsChange = (e) => {
        setSelectedAlbum(e.target.value);
    };

    return (
        <div className="container">
            <div className="row">
                <div className="col-6">
                    <select className="form-select mb-3" value={selectedUser} onChange={handleUsersChange}>
                        <option value="">Seleziona utente</option>
                        {users.map(({ id, name, username }) => (
                            <option key={id} value={id}>
                                {id} - {name} - {username}
                            </option>
                        ))}
                    </select>

                    <select className="form-select" value={selectedAlbum} onChange={handleAlbumsChange}>
                        <option value="">Seleziona album</option>
                        {albums.map(({ id, title }) => (
                            <option key={id} value={id}>
                                {title}
                            </option>
                        ))}
                    </select>
                </div>
                <div className="col-6">
                    <div className="photo-list">
                        {photos.map((photo) => {
                            const { albumId, id, title } = photo;
                            return (
                                <div className="photo-card" key={id}>
                                    <p>
                                        <b>ID:</b> {id} <br />
                                        <b>Title:</b> {title}
                                    </p>
                                </div>
                            );
                        })}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default UserAlbums;
