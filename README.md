# graph-relational-benchmark

This project enables you to benchmark graph and relational databases to compare their performance.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
To be able to connect to the Microsoft SQL database that will be created using the creation scripts below, there is a need to set up a Microsoft SQL Server on your local computer.

Neo4j Desktop Client also needs to be installed to be able to query the created Neo4j database.
```

# Running scripts manually
> **! Important**: Remove (comment out) the config option: `dbms.directories.import=import` from Neo4j -> Database -> Settings before population the graph database with fake data.

To populate the databases with fake data, run the following scripts while standing in the backend/api/db directory

```
./reset_cypher.sh -u
./reset_sql.sh
```

> **Note**: Only the first data population command needs the argument -u, as it creates the data which will be used to populate both databases. Nothing bad will happen if -u is provided to both scripts, it will just take a very long time.

# frontend

## Project setup

```
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

### Installing

A step by step series of examples that tell you how to get a development env running

Install required dependencies for both python and node

```
pip install -r requirements.txt
npm install
```

Add environment variables into a .env file

```
# .env
SQL_SERVER=XXXXXX (e.g. 8ZC5G31)
```

## Starting the web app and the django server

To start the development server, run 

```
npm start
```

which will start the web app at http://localhost:8080 as well as starting the backend server.

End with an example of getting some data out of the system or using it for a little demo

## Query Complexity Analysis

To analyse the complexity of the queries that are used for the benchmark, run the following command:

```
./complexity_analyzer.sh cypher_argument sql_argument
```

Where cypher_argument and sql_argument are the queries that are to be compared, e.g. cypher_argument = 'match' and sql_argument = 'select' will compare the complexity of the cypher match queries that correspond to the select queries in SQL.

## Built With

- [Vue.js](https://vuejs.org/) - The front-end web framework used
- [Django](https://www.djangoproject.com/) - The back-end web framework used

## Authors

- **Jan Zubac** - [JanZubac](https://github.com/JanZubac)
- **Victor Winberg** - [VictorWinberg](https://github.com/VictorWinberg)

See also the list of [contributors](https://github.com/VictorWinberg/graph-relational-benchmark/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Oskar Damkjaer, for helping with the readme.
