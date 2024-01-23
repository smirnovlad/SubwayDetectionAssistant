import classes from "./InputVideoColumn.module.css"
import React, { useState } from 'react';
import cameraPlaceholder from "../../img/SecurityCameraPNGImage.png"

const InputVideoColumn = (props) => {
    const [videoUrl, setVideoUrl] = useState(null);

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        const videoObjectUrl = URL.createObjectURL(file);
        setVideoUrl(videoObjectUrl);
        props.onVideoUploaded(file);
    };

    return (
        <div className={classes.InputVideoColumn}>
            {
                !videoUrl &&
                <div style={{
                    height: "80%",
                    width: "100%",
                    borderStyle: "solid",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    flexDirection: "column"
                }}>
                    <img src={cameraPlaceholder} style={{ width: "50%"}}/>
                </div>
            }
            {
                videoUrl &&
                <video width="100%" height="80%" style={{ objectFit: 'cover' }} controls>
                  <source src={videoUrl} type="video/mp4" />
                  Your browser does not support the video tag.
                </video>
            }
            <div style={{height: "5%"}}></div>
            <label className={classes.ChooseVideoButton}>
                <input type="file" accept="video/*" onChange={handleFileChange} />
                Choose video
            </label>
        </div>
)
}

export default InputVideoColumn;