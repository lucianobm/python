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
awsservices.extend(['ECS', 'EKS', 'Lambda', 'RDS', 'S3'])
awsservices.insert(0, 'Cloud9')
awsservices.insert(1, 'CloudWatch')
awsservices += ['VPC', 'WAF', 'X-Ray']

# Print the list and the length of the list
print("List of services:", awsservices)
print("Lenght of the list:", (len(awsservices)))

# Remove two specific services from the list by name or by index.
awsservices.remove('ECS')
del awsservices[4]

# Remove the last item from the list
del awsservices[-1]

# Print the new list and the new length of the list
print("New list of services:", awsservices)
print("Lenght of the new list:", (len(awsservices)))
