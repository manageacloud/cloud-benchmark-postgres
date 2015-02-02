# Cloud Postgres Benchmark

The goal of the project is to compute performance and cost figures for a
variety of cloud suppliers and configurations when running PostgreSQL.
This will include the intersection of:

 - The following cloud providers: 
  -  Heroku cloud
  -  Google cloud
  -  Amazon Web Services
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
  
## Benchmarking PostgreSQL 9.4 default configuration

1. Install mac cli tool

  ```
  pip install mac
  ```

2. Create the PostgreSQL server with the default configuration
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
 
3. Create the Pgbench server
 ```
 mac instance create -c pgbench -e DBNAME=pgbench PGUSER=benchuser IP=123.456.79.90 BENCH_CREATION="-i -s 70" BENCH_TEST="-c 4 -j 2 -T 10" -p rackspaceus
 ```
 Creates a server with the pgbench tool installed, and runs the benchmark test agains the postgres server running in the given IP.
 
 Configurable parameters
 * DBNAME: name of the database.
 * PGUSER: user that has access to the benchmark database
 * IP: PostgreSQL server IP
 * BENCH_CREATION: Additional parameters needed for the benchmark database creation. 
 The command for the creation of the benchmark database is:
 ```
 pgbench -h $IP -U $PGUSER -q $BENCH_CREATION $DBNAME
 ```
 * BENCH_TEST: Additional parameters for the benchmark test itself.
 The command for the benchmark tests is:
 ```
 pgbench -h $IP -U $PGUSER $BENCH_TEST $DBNAME
 ```
 
 - /tmp/output_benchmark contains the benchmark output
 - /tmp/pgbenchlog contains how long was needed to create the database and the benchmark
 
