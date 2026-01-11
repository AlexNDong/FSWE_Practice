#!/bin/bash
# 1st step is to create "bash_script_file.sh" ".sh is the file of bash script"
# 2nd step is to allow the file to be executed, run "sudo chmod +x test.sh", check the permission "ls -la"
your_file=$0
first_arg=$1

echo "Your first file is $your_file Your first variable is $first_arg"

# Condition for number
if (( $first_arg>0 )); then
    echo "First argument is positive"
elif (($first_arg==0)); then
    echo "First argument is zero"
else
    echo "First argument is negative"
fi
# Condition for string

str1="HELLO"
str2="WORLD"

if [[ $str1 = $str2 ]]; then
    echo "String is the same"
else
    echo "String is different"
fi

# Looping
for ((i=0; i<$first_arg; i++)); do
    echo $i
done

# User input
# Note: Use == for string comparison, not -eq which is for numbers
echo -n "Do you want to install me? [y/n]: "
read -r answer
if [[ "${answer,,}" == "y" ]]; then
    echo "Installed the package successfully!"
else
    echo "Cancelled installing the package!"
fi

# Read CSV file
# Reads a CSV file and prints the last column of each row using a while loop
# Example CSV file: ../data/Employees.csv
filepath="Employees.csv"
my_readfile_func() {
    while read -r line; do
        # Split line into array using IFS=',' # internal field seperator
        IFS=',' read -ra my_record <<EOF
$line
EOF
        # Print last element using portable indexing
        echo "${my_record[$(( ${#my_record[@]} - 2 ))]}" # @ means ALL, #my_record[@] means size n, index from 0 to n-1
    done < "$1"
}
# Run the function with filepath to print out the first column
my_readfile_func "$filepath"