import sys, re, subprocess, os

mac = os.environ.get('MAC_PATH', "mac")

#
# Parameters
#   1 - directory number
#   2 - provider (rackspace, aws or gce)
#   4 - size type

benchmarks = ["ro-memory", "rw-memory", "rw-disk" ]
types = ["custom", "default" ]

if sys.argv is None or len(sys.argv) < 4:
    print "More arguments are needed"
    exit(1)

directory = sys.argv[1]
provider = sys.argv[2]
size = sys.argv[3]

for benchmark in benchmarks:
    for type in types:
        filename = "%s-%s-%s.%s" % (provider, size, benchmark, type)
        full_path = "../config/%s/%s.macfile" % (provider, filename)
        cmd_create = "%s macfile %s" % (mac, full_path)
        print "[+] Creating " + cmd_create
        p = subprocess.Popen(['python', '/home/tk421/code/manageacloud-cli/maccli/mac_cli.py', 'macfile', full_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        ids = re.findall( "^Instance '([a-zA-Z0-9]+)' status 'Ready'$", out, re.MULTILINE)
        last_id = ids.pop()
        cmd_fetch = "%s instance ssh -c 'cat /tmp/pgbenchlog /tmp/output_benchmark' -i %s > ../data/%s/%s/%s.`date +%%d%%m%%y`" % (mac, last_id, provider, directory, filename)
        print "[+] Fetching " + cmd_fetch
        os.system(cmd_fetch)
        for id in ids:
            cmd_destroy =  "%s instance destroy -i %s " % (mac, id)
            print "[+] Destroying " + cmd_destroy

        cmd_destroy =  "%s instance destroy -i %s " % (mac, last_id)
        print "[+] Destroying " + cmd_destroy
        os.system(cmd_destroy)
