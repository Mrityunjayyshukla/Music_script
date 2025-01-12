To add FFmpeg to your system on Windows, macOS, and Linux, you need to install it and make sure it's available globally in your system's PATH. Here’s a step-by-step guide for each platform:

---

### **Windows:**

1. **Download FFmpeg**:
   - Go to the official FFmpeg download page: [FFmpeg Official Website](https://ffmpeg.org/download.html).
   - Under "Windows", select the link to download the **Windows builds** from sites like `Gyan.dev` or `BtbN` (recommended for Windows).

2. **Extract the ZIP file**:
   - Once downloaded, extract the ZIP file to a folder on your computer (e.g., `C:\ffmpeg`).

3. **Add FFmpeg to PATH**:
   - Right-click on the **This PC** or **Computer** icon on the desktop or Start menu and select **Properties**.
   - Click on **Advanced system settings** and then **Environment Variables**.
   - Under **System variables**, find the variable `Path`, select it, and click **Edit**.
   - Add the full path to the `bin` directory inside the extracted FFmpeg folder. For example: `C:\ffmpeg\bin`.
   - Click **OK** to close all the dialogs.

4. **Verify the installation**:
   - Open a new **Command Prompt** window (important to open a new one to refresh the PATH).
   - Type `ffmpeg` and press **Enter**. If everything is set up correctly, FFmpeg's version information will be displayed.

---

### **macOS:**

#### **Using Homebrew** (recommended):

1. **Install Homebrew** (if not already installed):
   - Open **Terminal** and paste the following command to install Homebrew:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Follow the prompts to finish the installation.

2. **Install FFmpeg** using Homebrew:
   - In the **Terminal**, run the following command:
     ```bash
     brew install ffmpeg
     ```

3. **Verify the installation**:
   - Once the installation is complete, type `ffmpeg` in the **Terminal** and press **Enter**.
   - You should see FFmpeg’s version information and other details.

#### **Alternative (Manual Installation)**:

1. **Download FFmpeg**:
   - Visit [FFmpeg Download](https://ffmpeg.org/download.html).
   - For macOS, choose a build from a site like [FFmpeg macOS builds](https://evermeet.cx/ffmpeg/).

2. **Extract and Install**:
   - Extract the downloaded file and place it in a directory of your choice.
   - Add FFmpeg to the `PATH` by following these steps:
     - Open **Terminal** and edit your shell profile (e.g., `~/.bash_profile` or `~/.zshrc` for zsh) by running:
       ```bash
       nano ~/.zshrc
       ```
     - Add the following line at the end of the file:
       ```bash
       export PATH="/path/to/ffmpeg/bin:$PATH"
       ```
       Replace `/path/to/ffmpeg` with the actual directory path where you extracted FFmpeg.
     - Save and exit (`Ctrl + X`, then press `Y` to confirm).
     - Reload the shell profile:
       ```bash
       source ~/.zshrc
       ```

3. **Verify**:
   - Type `ffmpeg` in the Terminal to check if it's properly installed.

---

### **Linux:**

#### **Using Package Manager (Ubuntu/Debian)**:

1. **Update the package list**:
   ```bash
   sudo apt update
   ```

2. **Install FFmpeg**:
   ```bash
   sudo apt install ffmpeg
   ```

3. **Verify the installation**:
   - After installation, type `ffmpeg` in the terminal to check the version and confirm that it’s installed.

#### **For other Linux distributions** (e.g., Fedora, Arch):

- **Fedora**:
   ```bash
   sudo dnf install ffmpeg
   ```

- **Arch Linux**:
   ```bash
   sudo pacman -S ffmpeg
   ```

#### **Manual Installation (if FFmpeg isn't in the repositories)**:

1. **Download the FFmpeg source code** from the [FFmpeg Download page](https://ffmpeg.org/download.html).
2. **Follow the build instructions** on the website to compile FFmpeg from source.

3. **Verify the installation**:
   - Type `ffmpeg` in the terminal to confirm it’s properly installed.

---

After completing the installation on your platform, you should be able to use FFmpeg from the command line globally.
