#!/usr/bin/env python3.7

# AWS Service Inventory

# This script will do the following:

# Create a list of services using Python. IE: S3, Lambda, EC2, etc
# The list should be empty initially.
# Populate the list using append or insert.
# Print the list and the length of the list.
# Remove two specific services from the list by name or by index.
# Print the new list and the new length of the list.

# The list should be empty initially
awsservices = []

# Populate the list using append or insert
awsservices.append('DynamoDB')
awsservices.append('EC2')

# Print the list and the length of the list
print("List of services:", awsservices)
print("Lenght of the list:", (len(awsservices)))
