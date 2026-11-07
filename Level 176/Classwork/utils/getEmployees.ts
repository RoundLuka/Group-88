import database from '../data/employees.json' with {type: "json"};

const getEmployees = () => {
    if(database.privateKey === process.env.DB_PRIVATE_KEY) {
        return database.employees;
    }
}

export default getEmployees;