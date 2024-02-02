import classes from "./ProcessVideoSettings.module.css"
import {useState, useEffect} from "react";

const ProcessVideoSettings = ({uploadedVideo, onVideoProcessed}) => {
    const [Mode, setMode] = useState();
    const [FPS, setFPS] = useState();
    const [processButtonDisabled, setProcessButtonDisabled] = useState(true);

    useEffect(() => {
        setProcessButtonDisabled(!(uploadedVideo && Mode && FPS))
    }, [uploadedVideo, Mode, FPS]);

    const handleModeSelectChange = (e) => {
        const newValue = e.target.value;
        setMode(newValue);
    }

    const handleFPSSelectChange = (e) => {
        const newValue = parseInt(e.target.value, 10);
        setFPS(newValue);
    };

    const requestVideoProcess = async () => {
        console.log("Uploaded video: ", uploadedVideo);

        let formData = new FormData();
        formData.append('video', uploadedVideo);
        console.log("Mode: ", Mode);
        formData.append("mode", Mode);
        console.log("FPS: ", FPS);
        formData.append('fps', FPS);

        setProcessButtonDisabled(true);
        try {
            let url = `http://127.0.0.1:8000/upload`;

            const response = await fetch(url, {
                method: 'POST',
                body: formData,
            });

            console.log("Response: ", response);

            let videoData = await response.arrayBuffer();

            console.log("Result: ", videoData);

            const videoBlob = new Blob([videoData], { type: 'video/mp4' });
            const videoFile = new File([videoBlob], uploadedVideo.name, { type: 'video/mp4' });
            console.log("Video file: ", videoFile);

            onVideoProcessed(videoFile);
        } catch (error) {
            console.error('Error uploading video:', error.message);
        }
        setProcessButtonDisabled(false);
    }

    return (
        <div className={classes.ProcessVideoSettings}>
            <div style={{display: "flex", alignItems: "center", justifyContent: "space-between"}}>
                <text style={{fontSize: 32, fontFamily: "Inter"}}>Mode</text>
                <select id="ModeSelect" style={{padding: "5%", width: "100px", height: "48px", fontSize: "24px"}}
                        onChange={handleModeSelectChange}>
                    <option value={""}></option>
                    <option value={"Fragmentation"}>FRAG (Just fragmentation)</option>
                    <option value={"Segmentation"}>SEG (Segmentation)</option>
                    <option value={"HPE"}>HPE (Human pose estimation)</option>
                    <option value={"HPE, SEG"}>HPE + SEG</option>
                    <option value={"Detection"}>DET (Detection)</option>
                </select>
            </div>
            <div style={{height: "10%"}}></div>
            <div style={{display: "flex", alignItems: "center", justifyContent: "space-between"}}>
                <text style={{fontSize: 32, fontFamily: "Inter"}}>FPS</text>
                <select id="fpsSelect" style={{padding: "5%", width: "100px", height: "48px", fontSize: "24px"}}
                        onChange={handleFPSSelectChange}>
                    <option value={""}></option>
                    <option value={1}>1</option>
                    <option value={2}>2</option>
                    <option value={4}>4</option>
                    <option value={8}>8</option>
                    <option value={16}>16</option>
                    <option value={32}>32</option>
                </select>
            </div>
            <div style={{height: "10%"}}></div>
            <button id="processButton" className={classes.ProcessVideoButton} onClick={requestVideoProcess} disabled={processButtonDisabled}>Process</button>
        </div>
    )
}

export default ProcessVideoSettings;