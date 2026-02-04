# Java Decompiler

Unzips JARs and converts `.class` to `.java` using Fernflower (mimicking IntelliJ).

### Requirements
*   Python 3.12+
*   Java 17+

### Setup
1.  `git clone https://github.com/bckuo/java-decompiler.git`
2.  `pip install -r requirements.txt`
3.  Place `fernflower.jar` in the `bin/` folder. (Build it from [source](https://github.com/JetBrains/intellij-community/tree/master/plugins/java-decompiler/engine)).

### Configuration (.env)
Create a `.env` file in the project root with your paths:
```ini
ROOT_PATH=D:\path\to\jars
JAVA=C:\path\to\java.exe
```
### Run
```
python java_decompiler.py
```
