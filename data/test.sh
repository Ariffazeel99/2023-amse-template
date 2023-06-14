#!/bin/sh
echo "Execute the pipeline"
python ./data/pipeline.py

# testing the working of pipeline
echo "Test if pipeline works correctly"
python test_pipeline.py
#pytest ./data/test_pipeline.py