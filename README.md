# Install

    sudo apt install python3 -y
    sudo apt install python3-pip -y


# Create a venv and use it

https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments

* Create a venv

  
    python3 -m venv venv

* Activate it:


    source .venv/bin/activate

* Install requirements in venv:


    pip install -r requirements.txt
    # or
    python3 -m pip install -r requirements.txt

* to deactivate just call
 

    deactivate

Once done you can import the venv in Intellij.