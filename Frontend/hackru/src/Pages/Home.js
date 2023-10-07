import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';


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
            fetch('url',  //change to URL of API later
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


    return (<div>
        <form onSubmit = { handleUpload }>
            <input type = 'file' name = 'picture' onChange={handleFile}/>
            <button onClick={ routeChangeLogin } >Submit</button>
        </form>
        
        </div>)
}

export default Home;