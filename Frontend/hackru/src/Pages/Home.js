import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {useTypewriter, Cursor } from 'react-simple-typewriter';
import { uploadFile } from 'react-s3';

const S3_BUCKET ='hackru';
const REGION ='us-east-1';
const ACCESS_KEY ="AKIASXA4X4ZE7TLPOTB6";
const SECRET_ACCESS_KEY ="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";

const config = {
    bucketName: S3_BUCKET,
    region: REGION,
    accessKeyId: ACCESS_KEY,
    secretAccessKey: SECRET_ACCESS_KEY,

}

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

    // function handleUpload(event) {
    //     event.preventDefault();
    
    //     if(file != null) {
    //         const reader = new FileReader();
    //         reader.onloadend = function() {
    //             const base64String = reader.result;
    //             // Sending the base64 string to the backend
    //             fetch('http://localhost:5000/imageRetrieval', {
    //                 method: 'POST',
    //                 headers: {
    //                     'Content-Type': 'application/json'
    //                 },
    //                 body: JSON.stringify({ image: base64String })
    //             })
    //             .then(response => response.json())
    //             .then(result => {
    //                 console.log("Success:", result);
    //             })
    //             .catch(error => {
    //                 console.error('Error:', error);
    //             });
    //         }
    //         reader.readAsDataURL(file);
    //     }
    // }

    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileInput = (e) => {
        setSelectedFile(e.target.files[0]);
    }

    const handleUpload = async (file) => {
        uploadFile(file, config)
            .then(data => console.log(data))
            .catch(err => console.error(err))
    }

    const [welcome]  = useTypewriter({
        words: ['Welcome to _____'],
        typeSpeed: 120
    })


    return (<div className='Home'>
        <div className='left-half'>
            <h1> {welcome} 
            <span style={{ color: 'white'}}>
                <Cursor cursortStyle = '|'/>
            </span>
            </h1>
        </div>
        
        <div className='right-half'>
            <h1> Find out what you are missing in your diet!!! :D</h1>
            <form onSubmit = { handleUpload }>
                <h2>What's in your Fridge?</h2>
                <input type = 'file' onChange={handleFileInput}/>
                <button  onClick={() => handleUpload(selectedFile)}>Submit</button>
            </form>
        </div>
        
        </div>)
}

export default Home;