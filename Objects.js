var users = [
    {
        name: "Michael",
        age: 37
    },
    {
        name: "John",
        age: 30
    },
    {
        name: "David",
        age: 27
    }
];

console.log(users[1].age);
console.log(users[0].name);

for (let index = 0; index < users.length; index++) {
    console.log(users[index].name+" - "+users[index].age)
}