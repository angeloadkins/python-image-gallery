#!/usr/bin/bash

if ["$#" != "1"]; then
	echo "Usage: deploy <version-number>"
	exit 1
fi

aws s3 ec2-scripts/ec2-prod-$1.sh s3://adkins-bucket
