# phone-convesation-test-portal
The file `tester.py` contains the extraction logic testing in standalone Python script.

The file `test-doc.txt` is a text file containing the data in the given format for extracting the data
in the required order by the portal

To run the portal,
  * in `terminal`, `cd` into `convo_test` folder.
  * execute: `python3 manage.py migrate`
  * execute: `python3 manage.py runserver`
  * open a browser and goto the link `localhost:8000/conversations`
  * select the txt file containing the information in the required format and press **OK** button.
