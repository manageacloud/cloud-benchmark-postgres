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
  

    
  
