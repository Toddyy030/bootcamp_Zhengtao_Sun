## Cleaning Strategy:<br>
- drop column extra data first since only two row are non-Nan value in that columns<br>
- drop rows if number of none values exceed 10% in that row<br>
- filling rest of none value using median value in their columns<br>
- normalize the data by leveraging standard scaler from scikit learn package
