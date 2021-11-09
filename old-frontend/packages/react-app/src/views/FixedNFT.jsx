import React, { useState } from "react";
import { Button, Input, DatePicker } from "antd";
export default function FixedNFT() {
  const [Name, setName] = useState("loading...");
  const [Amount, setAmount] = useState("loading... amnt");
  const [UTS, setUTS] = useState("loading... date");


  return (
    <>
      <div style={{ margin: 32 }}>
        <h1>Make your FIRB imposter</h1>
        <span
          className="highlight"
          style={{
            fontSize: 20,
            marginLeft: 4,
            /* backgroundColor: "#f9f9f9", */ padding: 4,
            borderRadius: 4,
            fontWeight: "bolder",
          }}
        >
          Name
        </span>
        <div style={{ margin: 8 }}>
          <Input
            style={{ width: 600 }}
            onChange={e => {
              setName(e.target.value);
            }}
          />
        </div>

        <span
          className="highlight"
          style={{
            fontSize: 20,
            marginLeft: 4,
            /* backgroundColor: "#f9f9f9", */ padding: 4,
            borderRadius: 4,
            fontWeight: "bolder",
          }}
        >
          Amount
        </span>
        <div style={{ margin: 8 }}>
          <Input
            style={{ width: 600 }}
            onChange={e => {
              setAmount(e.target.value);
            }}
          />
        </div>

        <span
          className="highlight"
          style={{
            fontSize: 20,
            marginLeft: 4,
            /* backgroundColor: "#f9f9f9", */ padding: 4,
            borderRadius: 4,
            fontWeight: "bolder",
          }}
        >
          Final Date
        </span>
        <div style={{ margin: 8 }}>
          <Input
            style={{ width: 600 }}
            onChange={e => {
              setUTS(e.target.value);
            }}
          />
        </div>

        <Button
          style={{ marginTop: 8 }}
          onClick={async () => {
            /* look how you call setPurpose on your contract: */
            /* notice how you pass a call back for tx updates too */

            //console.log(Name);
            //console.log(Amount);
            console.log(UTS);
            const timestamp = Date.now();
            console.log(timestamp)
            let finalTS = ( timestamp + (UTS * 86400000) );
            console.log(finalTS)

            
          }}
        >
          Make FIRB!
        </Button>
      </div>
    </>
  );
}
