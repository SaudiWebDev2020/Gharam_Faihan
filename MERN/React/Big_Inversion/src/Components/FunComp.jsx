import React from 'react';

const Person = (props) =>{
    
    const person1 = { firstName: "Jane", lastname: "Doe" , age: 45, hairColor : "Black"};
    const person2 = { firstName: "John", lastname: "Smith" , age : 88, hairColor : "Brown"};
    const person3 = { firstName: "Millard", lastname: "Fillmore" , age: 50, hairColor : "Brown"};
    const person4 = { firstName: "Maria", lastname: "Smith" , age: 62, hairColor: "Brown"};
    
    return (
        <div className='d-flex-flex-row'>
            <span> First Name : {Person1.firstname} </span>
        </div>
    );
}

export default Person;