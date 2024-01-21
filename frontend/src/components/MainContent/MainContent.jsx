import classes from "./MainContent.module.css"
import InputVideoColumn from "../InputVideoColumn/InputVideoColumn"
import ProcessVideoSettings from "../ProcessVideoSettings/ProcessVideoSettings"
import ProcessedVideoColumn from "../ProcessedVideoColumn/ProcessedVideoColumn"

const MainContent = () => {
    return(
        <div className={classes.MainContent}>
            <InputVideoColumn/>
            <div style={{width: "5%"}}></div>
            <ProcessVideoSettings/>
            <div style={{width: "5%"}}></div>
            <ProcessedVideoColumn/>
        </div>
    )
}

export default MainContent;