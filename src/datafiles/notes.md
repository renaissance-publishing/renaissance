```
sed 's/^- \*\*\(\w\+\)\:\*\*/- \1:/' < powers.mostlymd.dat | sed 's/^- \(\w\+\)\:/\%\1\%\n/' > powers.dat
```

God *damn* it, Alexis.

```
sed 's/\[\(.*\)\]/[[Powers]]\nname = "\1"/' < powers.orig.toml | sed 's/Special = /[[Powers.Section]]\nLabel = Special\nContent = /' | sed 's/Effect = /[[Powers.Section]]\nLabel = "Effect"\nContent = /' > powers.toml 
```

This *thing* from [this so](https://stackoverflow.com/questions/9999934/sed-joining-lines-depending-on-the-second-one), which helped merge the """ lines.

```
sed 'N;s/\n"""/"""/;P;D' < powers.bad.toml > powers.toml
```
