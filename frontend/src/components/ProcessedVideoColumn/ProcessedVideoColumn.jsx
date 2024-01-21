import classes from "./ProcessedVideoColumn.module.css"
import amongUsPlaceholder from "../../img/YellowAmongUsCharacterPNGImage.png"

const ProcessedVideoColumn = () => {
    return (
        <div className={classes.ProcessedVideoColumn}>
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
        </div>
    )
}

export default ProcessedVideoColumn;