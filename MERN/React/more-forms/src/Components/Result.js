import React from 'react';

const Result = props =>{
    const {firstname , lastname ,email , password } = props.user;


    return (
        <div>
        <h1> name : {firstname} {lastname} </h1>
        <h1> email : {email} </h1>
        <h1> password :{password} </h1>

        </div>
    )
}

export default Result;