for f in *.so.82; do
 ln -s "$f" "${f%.82}";
done
