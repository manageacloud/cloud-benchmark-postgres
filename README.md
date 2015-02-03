# Cloud Postgres Benchmark

The goal of the project is to compute performance and cost figures for a
variety of cloud suppliers and configurations when running PostgreSQL.
This will include the intersection of:

 - The following cloud providers: 
  -  Heroku cloud
  -  Google cloud
  -  Amazon Web Services (and RDS)
  -  Rackspace
  -  DigitalOcean
  -  OpenShift


-  Optimized vs default Postgres configuration
-  Different workloads
-  Postgres version 9.4 or 9.3

Benchmarking types:
 - pgbench read-only
 - pgbench read-write, small database size 0.5X RAM
 - pgbench read-write, database 2X size RAM
 - OLTPBench "[webapp](http://oltpbenchmark.com/wiki/index.php?title=Main_Page)" workload (Epinions, SEATS or Wikipedia)
  
## Create a PostgreSQL 9.4 database

1. Install mac cli tool

  ```
  pip install mac
  ```

2. Create the PostgreSQL server with the [default configuration](https://alpha.manageacloud.com/configuration/postgres_94_default)
 ```
 mac instance create -c postgres_94_default -e DBNAME=pgbench PGUSER=benchuser -p rackspaceus
 ```
 You will be guided to add the hardware type and the location. -p (--provider) can be digitalocean, rackspaceus, amazon and gce. 
 
 Configurable parameters:
 * DBNAME is the name of the database
 * PGUSER is the user with database access

 Use the following command to confirm if the server is Ready:
 ```
 mac instance list
 ```

 Please note that by default the server lifetime is 90 minutes (access to the [full documentation](https://alpha.manageacloud.com/article/orchestration/cli/instance/create) )
 
## Heroku

Create the application
```
heroku apps:create appname
```

Add PostgreSQL 9.4
```
heroku addons:add heroku-postgresql --version=9.4 --app appname
```

Get the connection string
```
$ heroku config:get DATABASE_URL --app appname
postgres://pihtadsfzzjsoq:KEwOJJNJBn_htuOKx_wwAwZJXT@ec2-54-243-187-192.compute-1.amazonaws.com:5432/d94kb6edmh5ntt
```
The output of this value is the one to use in the parameter CONN_STRING for the PG_BENCH server.

## Create the PGBench server 

[Creates server with PgBench](https://alpha.manageacloud.com/configuration/pgbench) and runs the benchmarking tests.

 ```
 mac instance create -c pgbench -e DBNAME=pgbench PGUSER=benchuser IP=123.456.79.90 BENCH_CREATION="-i -s 70" BENCH_TEST="-c 4 -j 2 -T 10" -p rackspaceus
 ```
 or
 ```
 mac instance create -c pgbench -e CONN_STRING="postgres://username:password@server:5432/database" BENCH_CREATION="-i -s 70" BENCH_TEST="-c 4 -j 2 -T 10" -p rackspaceus
 ```
 Creates a server with the pgbench tool installed, and runs the benchmark test agains the postgres server running in the given IP.
 
 Configurable parameters
 * DBNAME: name of the database.
 * PGUSER: user that has access to the benchmark database
 * IP: PostgreSQL server IP
 * CONN_STRING: If present, substitutes DBNAME, PGUSER and IP
 * BENCH_CREATION: Additional parameters needed for the benchmark database creation. 
 The command for the creation of the benchmark database is:
 ```
 pgbench -h $IP -U $PGUSER -q $BENCH_CREATION $DBNAME
 ```
 or 
 ```
 pgbench $CONN_STRING -q $BENCH_CREATION $DBNAME
 ```

 * BENCH_TEST: Additional parameters for the benchmark test itself.
 The command for the benchmark tests is:
 ```
 pgbench -h $IP -U $PGUSER $BENCH_TEST $DBNAME
 ```
 or 
 ```
 pgbench $CONN_STRING $BENCH_TEST $DBNAME
 ```
 
 - /tmp/output_benchmark contains the benchmark output
 - /tmp/pgbenchlog contains how long was needed to create the database and the benchmark
 
