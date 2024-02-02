import classes from "./MainContent.module.css"
import InputVideoColumn from "../InputVideoColumn/InputVideoColumn"
import ProcessVideoSettings from "../ProcessVideoSettings/ProcessVideoSettings"
import ProcessedVideoColumn from "../ProcessedVideoColumn/ProcessedVideoColumn"
import {useState} from "react"

const MainContent = () => {
    const [uploadedVideo, setUploadedVideo] = useState();
    const [processedVideo, setProcessedVideo] = useState();

    const handleUploadedVideo = (video) => {
        setUploadedVideo(video);
    }

    const handleProcessedVideo = (video) => {
        console.log("handle processed video: ", video);
        setProcessedVideo(video);
    }

    return(
        <div className={classes.MainContent}>
            <InputVideoColumn onVideoUploaded={handleUploadedVideo}/>
            <div style={{width: "5%"}}></div>
            <ProcessVideoSettings uploadedVideo={uploadedVideo} onVideoProcessed={handleProcessedVideo}/>
            <div style={{width: "5%"}}></div>
            <ProcessedVideoColumn processedVideo={processedVideo}/>
        </div>
    )
}

export default MainContent;