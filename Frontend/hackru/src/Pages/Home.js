import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useTypewriter, Cursor } from 'react-simple-typewriter';

function Home() {
    const navigate = useNavigate();
    const [file, setFile] = useState(null);
    const [message, setMessage] = useState('');  // Feedback message for user

    function handleFile(event) {
        const selectedFile = event.target.files[0];
        if (selectedFile && ["image/jpeg", "image/png", "image/gif"].includes(selectedFile.type)) {
            setFile(selectedFile);
            setMessage('');
        } else {
            console.log("Invalid file type selected.");
            setMessage('Please upload a valid image file (JPEG, PNG, GIF).');
            setFile(null);
        }
    }

    function handleUpload(event) {
        event.preventDefault();
        if (!file) {
            setMessage('Please select an image file before submitting.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        fetch('http://localhost:5000/imageRetrieval', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(result => {
            console.log("Success:", result);
            setMessage('Image uploaded successfully!');
            navigate('/DisplayPage_Vitamins');
        })
        .catch(error => {
            console.error('Error:', error);
            setMessage('Failed to upload the image. Please try again.');
        });
    }

    const [welcome] = useTypewriter({
        words: ['nutrition', 'recipes', 'eating', 'deliciousness'],
        typeSpeed: 120,
        loop:{}
    });

    return (
        <div className='Home'>
            <div className='left-half'>
                <h1>
                    Welcome to better {welcome} 
                    <span style={{ color: 'white'}}>
                        <Cursor cursortStyle='|'/>
                    </span>
                </h1>
            </div>
            
            <div className='right-half'>
                <h1>What's in your fridge?</h1>
                <form onSubmit={handleUpload} method='POST' encType='multipart/form-data'>
                    <h2>{message}</h2>
                <label class="custom-file-upload">
                    <input type="file" onChange={handleFile} accept=".jpg,.jpeg,.png,.gif" id="fileInput" />
                    <span>Choose a file...</span>
                </label>
                    <button>Submit</button>
                </form>
            </div>
        </div>
    );
}

export default Home;
