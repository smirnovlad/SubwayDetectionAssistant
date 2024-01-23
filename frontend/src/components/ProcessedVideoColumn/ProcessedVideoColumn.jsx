import classes from "./ProcessedVideoColumn.module.css"
import amongUsPlaceholder from "../../img/YellowAmongUsCharacterPNGImage.png"
import {useState, useEffect} from "react"

const ProcessedVideoColumn = ({processedVideo}) => {
    const [processedVideoUrl, setProcessedVideoUrl] = useState(null);

    useEffect(() => {
        if (processedVideo) {
            const videoObjectUrl = URL.createObjectURL(processedVideo);
            setProcessedVideoUrl(videoObjectUrl);
        }
    }, [processedVideo])

    return (
        <div className={classes.ProcessedVideoColumn}>
            {
                !processedVideoUrl &&
                <div style={{
                    height: "80%",
                    width: "100%",
                    borderStyle: "solid",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    flexDirection: "column"
                }}>
                    <img src={amongUsPlaceholder} style={{ width: "50%"}} />
                </div>
            }
            {
                processedVideoUrl &&
                <video width="100%" height="80%" style={{ objectFit: 'cover' }} controls>
                  <source src={processedVideoUrl} type="video/mp4" />
                  Your browser does not support the video tag.
                </video>
            }
        </div>
    )
}

export default ProcessedVideoColumn;