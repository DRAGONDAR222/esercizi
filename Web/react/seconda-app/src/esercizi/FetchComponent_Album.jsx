import React, { useEffect, useState } from 'react';

const albumsUrl = "https://jsonplaceholder.typicode.com/albums";

const FetchAlbums = () => {
  const [albums, setAlbums] = useState([]);

  const getAlbums = async () => {
    const data = await fetch(albumsUrl).then(res => res.json());
    setAlbums(data);
  };

  useEffect(() => {
    getAlbums();
  }, []);

  return (
    <select className="albums form-select">
      {albums.map(album => {
        const { id, title } = album;
        return (
          <option key={id} value={id}>
            {title}
          </option>
        );
      })}
    </select>
  );
};

export default FetchAlbums;
