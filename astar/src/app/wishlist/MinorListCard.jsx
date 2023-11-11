import React from "react";
import "../../css/minorcard.css";
import "bootstrap/dist/css/bootstrap.css";

function MinorListCard(props) {

        return (
            <div className={"minor-card"}>
                {props.minor_name}
            </div>
        )
}


export default MinorListCard;
