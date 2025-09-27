import React, { useEffect, useState } from 'react'
import axios from 'axios'

const useFetch = (url) => {
    const [data, setData] = useState([])
    const [isLoading, setIsLoading] = useState(true)

    useEffect(() => {
        (async () => {
            try {
                const response =await axios.get(url);
                setData(response.data)
            } catch (err) {
                console.log(err) 
            }
            setIsLoading(false)
        })()
    },[url])

    return {data,isLoading}
}

export default useFetch