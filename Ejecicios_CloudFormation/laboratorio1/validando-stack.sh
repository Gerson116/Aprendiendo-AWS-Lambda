#!/bin/bash
aws iam get-user --user-name groot

aws iam list-groups-for-user --user-name groot

aws iam get-group-policy --group-name Vengadores --policy-name ListAllMyBuckets
