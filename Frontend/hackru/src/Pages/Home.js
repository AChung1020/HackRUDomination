import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {useTypewriter, Cursor } from 'react-simple-typewriter';


function Home() {
    const navigate = useNavigate();
    const [file, setFile]  = useState(null);

    const routeChangeLogin = () => {
        if(file != null) {
            let path = `/DisplayPage_Vitamins`;
            navigate(path);
        } else {
            console.log("need a picture please!")
        }
        
      };

    
    function handleFile(event) {
        if (event.target.files.length > 0) {
            setFile(event.target.files[0]);
            console.log(event.target.files[0]);
        } else {
            console.log("No file selected.");
            setFile(null);
        }
    }

    function handleUpload(event) {
        event.preventDefault();
        const formData = new FormData()
        formData.append('file', file)
        
        if(file != null) {
            fetch('http://localhost:5000/imageRetrieval',  //change to URL of API later
            {  method: 'POST',
            body: formData
            }).then((response) => response.json())
            .then((result) => {
                console.log("Success", result)
            })
            .catch(error => {
                console.error('error', error)
            })
        }
        
    };

    const [welcome]  = useTypewriter({
        words: ['Welcome to _____'],
        typeSpeed: 120
    })


    return (
        <div className='Home'>
            <div className='left-half'>
                <h1>
                    {welcome} 
                    <span style={{ color: 'white'}}>
                        <Cursor cursortStyle='|'/>
                    </span>
                </h1>
            </div>
            
            <div className='right-half'>
                <h1>Find out what you are missing in your diet!!! :D</h1>
                <form onSubmit={handleUpload} method='POST' encType='multipart/form-data'>
                    <React.Fragment>
                        <h2>What's in your Fridge?</h2>
                        <input type='file' onChange={handleFile}/>
                    </React.Fragment>
                    <button>Submit</button>
                </form>
            </div>
        </div>
    );
}

export default Home;