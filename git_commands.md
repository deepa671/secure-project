
# Git Commands for Secure Project

## Upload Files
1. Initialize the repository:
   ```bash
   git init
   ```
2. Add the files:
   ```bash
   git add .
   ```
3. Commit the changes:
   ```bash
   git commit -m "Initial commit"
   ```
4. Add the remote repository:
   ```bash
   git remote add origin <your-repository-url>
   ```
5. Push the files:
   ```bash
   git push -u origin main
   ```

## Download Files
1. Clone or pull the repository:
   ```bash
   git pull origin main
   ```
2. Use `decrypt_files.py` to decrypt the files after download.
