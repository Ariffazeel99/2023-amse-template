#!/bin/sh
echo "Execute the pipeline"
python ./data/pipeline.py

# testing the working of pipeline
echo "Test if pipeline works correctly"
pytest ./data/Unittest.py