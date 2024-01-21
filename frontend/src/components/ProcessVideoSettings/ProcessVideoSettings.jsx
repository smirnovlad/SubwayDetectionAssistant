import classes from "./ProcessVideoSettings.module.css"

const ProcessVideoSettings = () => {
    return (
        <div className={classes.ProcessVideoSettings}>
            <div style={{display: "flex", alignItems: "center", justifyContent: "space-between"}}>
                <text style={{fontSize: 32, fontFamily: "Inter"}}>FPS</text>
                <select id="fps" style={{padding: "5%", width: "72px", height: "48px", fontSize: "24px"}}>
                    <option value={16}>16</option>
                    <option value={32}>32</option>
                    <option value={48}>48</option>
                    <option value={64}>64</option>
                </select>
            </div>
            <div style={{height: "10%"}}></div>
            <button className={classes.ProcessVideoButton}>Process</button>
        </div>
    )
}

export default ProcessVideoSettings;