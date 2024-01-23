import classes from "./ProcessVideoSettings.module.css"
import {useState} from "react";

const ProcessVideoSettings = ({uploadedVideo, onVideoProcessed}) => {
    const [FPS, setFPS] = useState(16);

    const handleSelectChange = (e) => {
        const newValue = parseInt(e.target.value, 10);
        setFPS(newValue);
    };

    const requestVideoProcess = async () => {
        console.log(uploadedVideo);

        const formData = new FormData();
        formData.append('file', uploadedVideo);

        try {
            let url = `http://127.0.0.1:8000/upload`;

            const response = await fetch(url, {
                method: 'POST',
                body: formData,
            });

            let result = await response.json();
            onVideoProcessed(result.processed_video);
        } catch (error) {
            console.error('Error uploading video:', error.message);
        }
    }

    return (
        <div className={classes.ProcessVideoSettings}>
            <div style={{display: "flex", alignItems: "center", justifyContent: "space-between"}}>
                <text style={{fontSize: 32, fontFamily: "Inter"}}>FPS</text>
                <select id="fps" style={{padding: "5%", width: "72px", height: "48px", fontSize: "24px"}}
                        onChange={handleSelectChange}>
                    <option value={16}>16</option>
                    <option value={32}>32</option>
                    <option value={48}>48</option>
                    <option value={64}>64</option>
                </select>
            </div>
            <div style={{height: "10%"}}></div>
            <button className={classes.ProcessVideoButton} onClick={requestVideoProcess}>Process</button>
        </div>
    )
}

export default ProcessVideoSettings;