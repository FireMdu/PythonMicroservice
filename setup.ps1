###########################################################
## This file will setup python and the dependant modules ##
###########################################################

if (-Not (Test-Path -Path "python_local"))
{
    Write-Host "Installing local python virtual environment"

    # Display the installed python versions
    py -0p
    # Assuming 3.9 and install virtualenv
    py -3.9 -m pip install virtualenv
    # Create a virtual environment
    virtualenv python_local
}
else {
    Write-Host "Python virtual environment already exist, skipped."
}

# Ensure scripts can be run - Only uncomment if there is a error on the following step
# Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser
# Activate the environment
python_local\scripts\activate

# Update pip
python -m pip install --upgrade pip

# Update all PIP modules
pip install -r requirements.txt

