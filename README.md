# IG-Followers-Check
Here is a `README.md` file you can use for your GitHub repository. It clearly explains the purpose of the script and the steps a user needs to follow, from downloading their Instagram data to running the Python code.

-----

## Prerequisites

To run this script, you need:

1.  **Python 3** installed on your system.
2.  Your **Instagram Data** package (specifically, the `followers.html` and `following.html` files).

## 📥 Getting Your Instagram Data

Before running the script, you must download your Instagram information archive:

1.  Go to **Instagram Settings**.
2.  Navigate to **Your Activity** (or **Privacy and Security** if using a web browser).
3.  Select **Download your information** (Data Download).
4.  Request a **JSON** or **HTML** copy of your data. **Request the HTML format** for this script to work easily.
5.  Once the archive is ready (it may take a few hours), download the **ZIP file**.

## ⚙️ Setup and Execution

Follow these steps after downloading and extracting your Instagram data:

### Step 1: Extract and Locate Files

1.  **Extract** the downloaded ZIP file from Instagram (e.g., `your_username_date.zip`).
2.  Inside the extracted folder, navigate to the **`followers_and_following/`** directory.
3.  You will find two key files:
      * `followers.html`
      * `following.html`

### Step 2: Place the Script

1.  Save the Python script (e.g., `auditor.py`) in the **same directory** as the `followers.html` and `following.html` files.

### Step 3: Run the Script

1.  **Open your terminal** or command prompt.
2.  Navigate to the directory where you placed the files using the `cd` command.
    ```bash
    # Example command, replace path with your actual directory
    cd /path/to/your/instagram/data/followers_and_following
    ```
3.  Execute the script using Python:
    ```bash
    python auditor.py
    ```

## 💻 Code Output

The script will read the HTML files and print a list of profile links for every user that appears in your `following.html` but *not* in your `followers.html`.

```
Users not following back:
 https://www.instagram.com/example_user_1
 https://www.instagram.com/another_profile_2
 ...
```

If everyone you follow is following you back, the output will be:

```
Users not following back:
 All users are following back.
```

-----

## ⚠️ Important Note

This script relies on the exact structure of the HTML files provided by Instagram's "Download Your Information" tool. If Instagram changes the file format or the URL structure, the regular expression in the script may need to be updated.
