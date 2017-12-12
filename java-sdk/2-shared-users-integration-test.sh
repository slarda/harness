#!/usr/bin/env bash

echo
echo "Usage: 2-shared-users-integration-test.sh run from harness/java-sdk"
echo
# point to the harness host, use https://... for SSL and set the credentials if using Auth
# export "HARNESS_CLIENT_USER_ID"=xyz
# export "HARNESS_CLIENT_USER_SECRET"=abc
host=localhost
engine_1=test_resource
engine_2=test_resource_2
test_queries=data/2-user-query.json
engine_1_events=data/joe-context-tags-2.json
engine_2_events=data/john-context-tags-2.json
sleep_seconds=1

export HARNESS_CA_CERT=/Users/pat/harness/rest-server/server/src/main/resources/keys/harness.pem

harness delete test_resource
sleep $sleep_seconds
harness add ../rest-server/data/test_resource.json
#sleep $sleep_seconds
harness delete test_resource_2
sleep $sleep_seconds
harness add ../rest-server/data/test_resource_2.json

cd example
mvn clean install
echo
echo "Sending events to create testGroup: 1, user: joe, and one conversion event with contextualTags to test_resource"
echo
mvn exec:java -Dexec.mainClass="EventsClientExample" -Dexec.args="$host $engine_1 $engine_1_events" -Dexec.cleanupDaemonThreads=false
echo
echo "Sending events to create testGroup: 1, user: john, and one conversion event with contextualTags to test_resource_2"
echo
mvn exec:java -Dexec.mainClass="EventsClientExample" -Dexec.args="$host $engine_2 $engine_2_events" -Dexec.cleanupDaemonThreads=false
echo
echo "Sending queries for joe and john to test_resource"
echo
mvn exec:java -Dexec.mainClass="QueriesClientExample" -Dexec.args="$host $engine_1 $test_queries" -Dexec.cleanupDaemonThreads=false
echo
echo "Sending queries for joe and john to test_resource_2"
echo
mvn exec:java -Dexec.mainClass="QueriesClientExample" -Dexec.args="$host $engine_2 $test_queries" -Dexec.cleanupDaemonThreads=false
cd ..
echo "Ending directory"
pwd
