#------------------------------------------------------------------------------
# Hands-On Lab: Data Engineering with Snowpark
# Script:       05_fahrenheit_to_celsius_udf/app.py
# Author:       Jeremiah Hansen, Caleb Baechtold
# Last Updated: 1/9/2023
#------------------------------------------------------------------------------

# SNOWFLAKE ADVANTAGE: Snowpark Python programmability
# SNOWFLAKE ADVANTAGE: Python UDFs (with third-party packages)
# SNOWFLAKE ADVANTAGE: SnowCLI (PuPr)



# course step 5
#import sys

#def main(temp_f: float) -> float:
#    return (float(temp_f) - 32) * (5/9)

#course step 10
import sys
from scipy.constants import convert_temperature

def main(temp_f: float) -> float:
    return convert_temperature(float(temp_f), 'F', 'C')


# For local debugging
# Be aware you may need to type-convert arguments if you add input parameters
if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(main(*sys.argv[1:]))  # type: ignore
    else:
        print(main())  # type: ignore
