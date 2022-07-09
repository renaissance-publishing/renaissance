sed 's/^- \*\*\(\w\+\)\:\*\*/- \1:/' < powers.mostlymd.dat | sed 's/^- \(\w\+\)\:/\%\1\%\n/' > powers.dat
