import classes from "./ProcessedVideoColumn.module.css"
import amongUsPlaceholder from "../../img/YellowAmongUsCharacterPNGImage.png"
import {useState, useEffect} from "react"

const ProcessedVideoColumn = ({processedVideo}) => {
    const [processedVideoUrl, setProcessedVideoUrl] = useState(null);

    useEffect(() => {
        if (processedVideo) {
            console.log("Processed video: ", processedVideo);

            const fileData = processedVideo.file._file;
            const arrayBuffer = fileData._file;

            // Create a Uint8Array from the array buffer
            const uint8Array = new Uint8Array(arrayBuffer);

            // Create a Blob from the Uint8Array
            const blob = new Blob([uint8Array], { type: processedVideo.headers['content-type'] });

            // Create a File object from the Blob
            const file = new File([blob], processedVideo.filename, { type: processedVideo.headers['content-type'] });

            console.log("File: ", file)

            const videoObjectUrl = URL.createObjectURL(file);
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