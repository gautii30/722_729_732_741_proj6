#!/bin/bash
set -e # Exit on error

# Copy .env files within the Jenkins workspace
cp /var/jenkins_home/workspace/proj6/uc1/.env /var/jenkins_home/workspace/proj6/uc1/
cp /var/jenkins_home/workspace/proj6/uc2/.env /var/jenkins_home/workspace/proj6/uc2/
cp /var/jenkins_home/workspace/proj6/uc3/.env /var/jenkins_home/workspace/proj6/uc3/
