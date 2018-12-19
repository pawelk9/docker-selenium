#!/bin/bash
ls -l
pwd
exec behave --verbose features "$@"
