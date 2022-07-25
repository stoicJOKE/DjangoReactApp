import React, {useState, useEffect} from 'react'
import axios from 'axios'

const Index = () => {
    const [musician, setMusician] = useState([])

    useEffect(() => {
        async function loadMusician(){
            try{
            const response = await axios.get('http://localhost:8000/api/musicians/')
            setMusician(response.data)
        }catch (e){
            console.log(e)
        }
        }
        loadMusician()
        
    }, [])

  return (
    <div>
        {console.log(musician)}
        {musician.map(data => {
            return <h2 key={data.id}>{data.first_name}</h2>
        })}
    </div>
  )
}

export default Index;